@Subroutine
def ExSkillInit():
    Unknown11091(10)
    Unknown30065(0)

@Subroutine
def InvSkillInit():
    Unknown30065(100)

@Subroutine
def PartnerSkillInit():
    AttackP1(70)
    Unknown11042(1)

@State
def Invincible_Obj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown4007(3)
        callSubroutine('InvSkillInit')
        Unknown11108('03000000')
        AttackLevel_(4)
        Damage(1500)
        AirUntechableTime(30)
        Unknown9168(30)
        AttackP1(48)
        AttackP2(100)
        Unknown11084(1)
        Unknown11044(1)
        Unknown1096(4000)
        Unknown1099(250)
        Unknown23027()
        Unknown2035(1)

        def upon_STATE_END():
            SLOT_8 = 0

        def upon_3():
            if SLOT_8:
                Unknown13(25)
    sprite('vr_ahe_magicol', 10)
    sprite('vr_ahe_magicol', 5)
    Unknown4007(0)
    RefreshMultihit()
    sprite('vr_ahe_magicol', 10)
    StartMultihit()

@State
def UltimateUpper_Obj():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown4007(3)
        AttackLevel_(4)
        AttackP1(48)
        AttackP2(100)
        Unknown1096(4000)
        Unknown1099(250)
        Unknown23027()
        Unknown2035(1)
    sprite('vr_ahe_magicol', 10)
    sprite('vr_ahe_magicol', 5)
    Unknown4007(0)
    StartMultihit()
    sprite('vr_ahe_magicol', 10)
    StartMultihit()

@State
def Shot_Obj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        teleportRelativeX(50000)
        AttackLevel_(3)
        Hitstop(9)
        AirUntechableTime(27)
        Unknown1056(4000)
        Unknown1064(4000)
        Unknown23027()
        Unknown2035(1)
        Unknown53(1)

        def upon_43():
            if (SLOT_48 == 4031):
                Unknown30070('53686f74415f4f626a0000000000000000000000000000000000000000000000')
            if (SLOT_48 == 4032):
                Damage(1200)
                Unknown30070('53686f74425f3173744f626a0000000000000000000000000000000000000000')
            if (SLOT_48 == 4033):
                Damage(1200)
                Unknown30070('53686f74425f326e644f626a0000000000000000000000000000000000000000')
                Unknown1007(50000)
            if (SLOT_48 == 4034):
                Damage(1200)
                Unknown30070('53686f74425f3372644f626a0000000000000000000000000000000000000000')
                Unknown1007(-50000)
            if (SLOT_48 == 4035):
                Unknown30070('53686f745265665f4f626a000000000000000000000000000000000000000000')
                Unknown11084(1)
                physicsXImpulse(5000)
            if (SLOT_48 == 4036):
                Damage(1800)
                AirUntechableTime(60)
                AirPushbackY(23000)
                GroundedHitstunAnimation(1)
                callSubroutine('PartnerSkillInit')
                Unknown30070('53686f744173736973745f4f626a000000000000000000000000000000000000')
            if (SLOT_48 == 4037):
                sendToLabel(1)

        def upon_3():
            Unknown1019(105)
            SLOT_51 = 0
            SLOT_13 = 0
            if SLOT_2:
                Unknown48('190000000200000033000000160000000200000017000000')
                Unknown47('01000000020000001700000002000000330000000200000033000000')
                SLOT_51 = (SLOT_51 + (-141000))
                Unknown47('03000000020000003300000000000000ceffffff020000000d000000')
                if (SLOT_13 <= (-4000)):
                    SLOT_13 = (-4000)
                if (SLOT_13 >= 4000):
                    SLOT_13 = 4000

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            clearUponHandler(3)
            Unknown1019(25)
            YAccel(25)
            sendToLabel(1)
    sprite('vr_ahe_magicol', 2)
    GFX_0('ahe403_shot_eff', 100)
    Unknown38(4, 1)
    StartMultihit()
    sprite('vr_ahe_magicol', 30)
    Unknown1015(250)
    StartMultihit()
    sprite('vr_ahe_magicol', 100)
    RefreshMultihit()
    Unknown1015(1800)
    Unknown11084(0)
    Unknown2037(1)
    sprite('vr_ahe_magicol', 200)
    Unknown2037(0)
    label(1)
    sprite('vr_ahe_magicol', 6)
    clearUponHandler(43)
    Unknown13(4)
    StartMultihit()

@State
def ShotEx_Obj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        AttackLevel_(4)
        Damage(2400)
        GroundedHitstunAnimation(1)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        callSubroutine('ExSkillInit')
        Hitstop(9)
        Unknown1056(60000)
        Unknown1064(4000)
        teleportRelativeX(900000)
        Unknown23027()
        Unknown2035(1)

        def upon_43():
            if (SLOT_48 == 4036):
                callSubroutine('PartnerSkillInit')
                Unknown30065(50)
                Unknown11091(5)
                Damage(2000)
    sprite('vr_ahe_magicol', 2)
    sprite('vr_ahe_magicol', 6)
    RefreshMultihit()
    sprite('vr_ahe_magicol', 6)
    StartMultihit()

@State
def ahe_homing_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        GFX_2('aheef_hmgdash')
        Unknown1096(1250)
        Unknown1072(-45000)
    sprite('null', 4)
    GFX_0('ahe_homing_3D_eff', 100)
    Unknown3007(74)
    Unknown3013(189)
    Unknown3019(255)
    sprite('null', 30)
    Unknown4007(0)

@State
def ahe_homing_3D_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('61686565665f686d675f6d67636972636c655f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 13)
    Unknown3007(79)
    Unknown3013(191)
    Unknown3019(255)
    Unknown1099(75)
    sprite('null', 7)
    Unknown3022(-151)
    Unknown3004(-51)

@State
def ahe_homing_wind_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f686d675f6d67636972636c655f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown1096(1200)
    sprite('null', 7)
    GFX_0('ahe_homing_windbst_eff', 100)
    Unknown3001(180)
    Unknown3007(74)
    Unknown3013(189)
    Unknown3019(255)
    sprite('null', 5)
    Unknown3004(-30)

@State
def ahe_homing_windbst_eff():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown4003('61686565665f686d675f6d6762757273745f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown1096(3500)
    sprite('null', 6)
    Unknown3001(180)
    teleportRelativeX(-20000)
    Unknown3007(74)
    Unknown3013(189)
    Unknown3019(255)
    sprite('null', 1)
    sprite('null', 5)
    Unknown3004(-20)

@State
def ahe_homing_add_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 3)
    GFX_1('aheef_hmgdash_pt', 100)
    gotoLabel(0)

@State
def ahe_DDD():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4022(2)
        Unknown4009(2)
        Unknown2055(30)
    label(0)
    sprite('null', 2)
    GFX_1('aheef430_dust', -1)
    gotoLabel(0)

@State
def ahe_DDD_End():

    def upon_IMMEDIATE():
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown2055(210)
    label(0)
    sprite('null', 1)
    GFX_1('aheef_DDD_end_d', -1)
    gotoLabel(0)

@Subroutine
def ahe273_color():
    Unknown3007(246)
    Unknown3019(174)
    Unknown3013(68)

@Subroutine
def ahe430_color():
    Unknown3007(233)
    Unknown3019(123)
    Unknown3013(47)

@Subroutine
def ahe403_color():
    Unknown3007(255)
    Unknown3019(169)
    Unknown3013(26)

@State
def ahe201_Charge_Loop_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
    label(1)
    sprite('null', 8)
    GFX_0('ahe201_Charge_Circle_Eff', 100)
    GFX_0('ahe201_Charge_RoundCircle_Eff', 100)
    GFX_0('ahe201_Charge_RoundCircle2_Eff', 100)
    GFX_1('aheef_charge_dust', 100)
    gotoLabel(1)

@State
def ahe201_Charge_Circle_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('aheef_charge')
        Unknown1007(200000)
    sprite('null', 20)

@State
def ahe201_Charge_RoundCircle_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('61686565665f666f6f74617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
    sprite('null', 3)
    Unknown1096(1250)
    Unknown1099(166)
    Unknown3007(255)
    Unknown3019(135)
    Unknown3013(89)
    Unknown3022(2)
    Unknown3016(2)
    Unknown3001(0)
    Unknown3004(85)
    sprite('null', 9)
    Unknown3004(-28)

@State
def ahe201_Charge_RoundCircle2_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('61686565665f666f6f74617572615f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(0)
    sprite('null', 3)
    Unknown1096(1250)
    Unknown1099(166)
    Unknown3007(255)
    Unknown3019(135)
    Unknown3013(89)
    Unknown3022(2)
    Unknown3016(2)
    Unknown3001(0)
    Unknown3004(85)
    sprite('null', 9)
    Unknown3004(-28)

@State
def ahe201_move_dust_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
    label(0)
    sprite('null', 1)
    GFX_1('aheef_charge_dust_b', 100)
    gotoLabel(0)

@State
def ahe231_Charge_Loop_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
    label(1)
    sprite('null', 8)
    GFX_0('ahe231_Charge_Circle_Eff', 100)
    GFX_0('ahe201_Charge_RoundCircle_Eff', 100)
    GFX_0('ahe201_Charge_RoundCircle2_Eff', 100)
    GFX_1('aheef_charge_dust', 100)
    gotoLabel(1)

@State
def ahe231_Charge_Circle_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('aheef_charge')
        Unknown1007(115000)
    sprite('null', 12)

@State
def ahe273_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(0)
    sprite('null', 2)
    GFX_0('ahe273_attack_hand_eff', 100)
    GFX_0('ahe273_attack_bg_eff', 100)
    GFX_0('ahe273_attack1_eff', 100)
    GFX_0('ahe273_attack1b_eff', 100)
    GFX_0('ahe273_attack2_eff', 100)
    GFX_0('ahe273_attack_flash_eff', 100)
    sprite('null', 15)

@State
def ahe273_attack1_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('61686565665f726962626f6e6265616d5f68656172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        callSubroutine('ahe273_pos')

        def upon_43():
            if (SLOT_48 == 5033):
                Unknown13(25)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 8)
    Unknown3001(255)
    Unknown1099(250)
    sprite('null', 5)
    Unknown3004(-46)

@State
def ahe273_attack1b_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('61686565665f726962626f6e6265616d5f68656172745f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        callSubroutine('ahe273_pos')

        def upon_43():
            if (SLOT_48 == 5033):
                Unknown13(25)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 9)
    Unknown1099(250)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    sprite('null', 3)
    Unknown1099(0)
    Unknown3004(20)
    sprite('null', 3)
    Unknown3004(-30)
    Unknown3022(-50)
    Unknown3016(-50)

@State
def ahe273_attack2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('61686565665f726962626f6e6265616d5f68656172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        callSubroutine('ahe273_pos')

        def upon_43():
            if (SLOT_48 == 5033):
                Unknown13(25)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 8)
    Unknown3001(255)
    Unknown1096(200)
    Unknown1099(150)
    sprite('null', 5)
    Unknown3004(-46)

@State
def ahe273_attack_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('61686565665f726962626f6e6265616d5f68656172745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        callSubroutine('ahe273_pos')
        Unknown3032()

        def upon_43():
            if (SLOT_48 == 5033):
                Unknown13(25)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 8)
    Unknown1099(250)
    Unknown3001(180)
    callSubroutine('ahe273_color')
    sprite('null', 5)
    Unknown3004(-36)

@State
def ahe273_attack_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('61686565665f726962626f6e6265616d5f68656172745f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        callSubroutine('ahe273_pos')

        def upon_43():
            if (SLOT_48 == 5033):
                Unknown13(25)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 3)
    Unknown3001(255)
    Unknown1099(250)
    sprite('null', 5)
    Unknown3004(-36)
    sprite('null', 5)
    Unknown1099(-250)

@State
def ahe273_attack_hand_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('61686565665f726962626f6e6265616d2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        teleportRelativeX(20000)
        Unknown1007(230000)

        def upon_43():
            if (SLOT_48 == 5033):
                Unknown13(25)
    sprite('null', 2)
    Unknown1096(2800)
    Unknown1072(-30000)
    Unknown1074(2500)
    sprite('null', 2)
    Unknown1073(10000)
    sprite('null', 2)
    Unknown1073(70000)
    Unknown1097(100)
    Unknown1075(-500)
    sprite('null', 2)
    Unknown1097(300)
    sprite('null', 2)
    Unknown3016(-40)
    sprite('null', 3)
    Unknown3004(-66)

@Subroutine
def ahe273_pos():
    teleportRelativeX(100000)
    Unknown1007(185000)

@Subroutine
def ahe400_posY():
    Unknown1007(200000)

@State
def ahe400_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f69726f6e666973742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(254000)
        callSubroutine('ahe400_posY')

        def upon_43():
            if (SLOT_48 == 5031):
                GFX_0('ahe400_hit_eff', 100)
                sendToLabel(0)
    sprite('null', 3)
    Unknown1059(30)
    Unknown1067(20)
    sprite('null', 7)
    Unknown1067(30)
    Unknown1064(1080)
    Unknown1067(-68)
    sprite('null', 8)
    Unknown3022(-16)
    Unknown3016(-16)
    GFX_1('aheef400_end', 100)
    loopRest()
    ExitState()
    label(0)
    sprite('null', 1)
    sprite('null', 32767)
    Unknown13(25)

@State
def ahe400_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 7)
    GFX_0('ahe400_dust1_eff', 100)
    sprite('null', 50)
    GFX_0('ahe400_dust2_eff', 100)

@State
def ahe400_dust1_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(130000)
        Unknown1007(200000)
        Unknown2055(7)
    label(0)
    sprite('null', 1)
    GFX_1('aheef400_particle', 100)
    gotoLabel(0)

@State
def ahe400_dust2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(130000)
        callSubroutine('ahe400_posY')
        Unknown2055(5)
    label(0)
    sprite('null', 1)
    GFX_1('aheef400_particle_00', 100)
    gotoLabel(0)

@State
def ahe401_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 8)
    GFX_0('ahe401_dust1_eff', 100)
    sprite('null', 50)
    GFX_0('ahe401_dust2_eff', 100)

@State
def ahe401_dust1_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(130000)
        callSubroutine('ahe400_posY')
        Unknown2055(8)
    label(0)
    sprite('null', 1)
    GFX_1('aheef401_particle', 100)
    gotoLabel(0)

@State
def ahe401_dust2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(130000)
        callSubroutine('ahe400_posY')
        Unknown2055(5)
    label(0)
    sprite('null', 1)
    GFX_1('aheef401_particle_00', 100)
    gotoLabel(0)

@State
def ahe402_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(100000)
        callSubroutine('ahe400_posY')

        def upon_43():
            if (SLOT_48 == 5032):
                sendToLabel(0)
    sprite('null', 4)
    GFX_0('ahe402_ring_eff', 100)
    GFX_0('ahe402_line1_eff', 100)
    sprite('null', 4)
    GFX_0('ahe402_ring_eff', 100)
    sprite('null', 8)
    GFX_0('ahe402_ring_eff', 100)
    GFX_0('ahe402_line2_eff', 100)
    sprite('null', 8)
    GFX_0('ahe402_ring_eff', 100)
    loopRest()
    ExitState()
    label(0)
    sprite('null', 1)
    sprite('null', 32767)
    Unknown13(25)

@State
def ahe402_ring_eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 30)
    GFX_2('aheef402_ring')
    Unknown1072(-45000)
    physicsXImpulse(-8000)

@State
def ahe402_line1_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f69726f6e666973745f6c6f6375732e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(90000)
    sprite('null', 7)
    Unknown1056(1700)
    Unknown1064(270)
    Unknown1059(850)
    sprite('null', 1)
    Unknown1059(-560)
    sprite('null', 2)
    Unknown1067(-20)
    sprite('null', 3)
    Unknown3022(-21)
    Unknown3016(-21)
    sprite('null', 5)
    Unknown1067(-34)
    Unknown1059(0)

@State
def ahe402_line2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_2('aheef402_line')
        teleportRelativeX(-370000)
    sprite('null', 13)
    physicsXImpulse(-20000)

@State
def ahe400_hit_eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
    sprite('null', 60)
    GFX_0('ahe400_hit02_eff', 100)
    GFX_0('ahe400_hit01b_eff', 100)
    GFX_0('ahe400_hit04_eff', 100)
    GFX_0('ahe400_hit01_eff', 100)
    GFX_0('ahe400_hit03_eff', 100)

@State
def ahe400_hit01_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f3430305f68697430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-3500)
        Unknown1007(-1200)
    sprite('null', 9)
    Unknown1096(880)
    Unknown1099(120)
    sprite('null', 9)
    Unknown3004(-28)

@State
def ahe400_hit02_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f3430305f68697430322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
    sprite('null', 9)
    Unknown1099(330)
    Unknown3001(200)
    Unknown3007(255)
    Unknown3013(63)
    Unknown3019(191)
    sprite('null', 9)
    Unknown3004(-22)

@State
def ahe400_hit03_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f3430305f68697430332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
    sprite('null', 1)
    Unknown1096(2000)
    Unknown1099(330)
    sprite('null', 9)
    Unknown3004(-16)

@State
def ahe400_hit01b_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f3430305f68697430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
    sprite('null', 9)
    Unknown1099(330)
    sprite('null', 9)
    Unknown3004(-28)

@State
def ahe400_hit04_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f3430305f68697430342e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
    sprite('null', 10)
    Unknown1099(330)
    Unknown3001(0)
    Unknown3007(255)
    Unknown3013(63)
    Unknown3019(191)
    sprite('null', 4)
    Unknown1099(0)
    Unknown3004(32)
    sprite('null', 4)
    Unknown3004(-32)
    Unknown3016(-32)
    Unknown3022(-32)

@State
def ahe430_hold_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(-50000)
        Unknown1007(205000)
        Unknown4003('61686565665f7377696e6761726d2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown23015(15)
    sprite('null', 25)
    Unknown3001(0)
    sprite('null', 25)
    Unknown1096(3000)
    Unknown3004(10)
    sprite('null', 26)
    sprite('null', 12)
    Unknown4007(0)
    Unknown3004(-21)
    Unknown1099(166)

@State
def ahe430_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4015()
        Unknown4009(2)
    sprite('null', 27)
    GFX_0('ahe430_attack_02_eff', 100)
    GFX_0('ahe430_attack_01_eff', 100)
    GFX_0('ahe430_attack_03_eff', 100)

@State
def ahe430_attack_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f6c6f76655f69726f6e666973742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(300000)
        Unknown1007(185000)
    sprite('null', 13)
    Unknown1056(2500)
    Unknown1064(2400)
    sprite('null', 10)
    Unknown3004(-19)
    Unknown3022(-15)
    Unknown3016(-15)

@State
def ahe430_attack_02_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(320000)
        Unknown1007(185000)
    sprite('null', 19)
    Unknown1056(2400)
    Unknown1064(2300)
    callSubroutine('ahe430_color')
    sprite('null', 8)
    Unknown3004(-25)

@State
def ahe430_attack_03_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(20000)
        Unknown1007(185000)
    sprite('null', 19)
    Unknown1056(2500)
    Unknown1064(2000)
    callSubroutine('ahe430_color')
    Unknown3001(80)
    sprite('null', 8)
    Unknown3004(-8)

@State
def ahe430_magical_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4015()
        Unknown4009(2)
    sprite('null', 5)
    GFX_0('ahe430_heart_eff', 100)
    GFX_0('ahe430_particle_eff', 100)
    sprite('null', 5)
    GFX_0('ahe430_heart_eff', 100)
    sprite('null', 15)
    GFX_0('ahe430_heart_eff', 100)

@Subroutine
def ahe430_heart():
    Unknown4009(2)
    Unknown4007(2)
    Unknown4015()

@State
def ahe430_heart_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        callSubroutine('ahe430_heart')
    sprite('null', 15)
    GFX_0('ahe430_heart_flash_eff', 100)
    GFX_0('ahe430_heart_bg_eff', 100)
    GFX_0('ahe430_heart_a2_eff', 100)
    GFX_0('ahe430_heart_a_eff', 100)

@Subroutine
def ahe430_transform():
    teleportRelativeX(100000)
    Unknown1007(185000)

@State
def ahe430_heart_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        callSubroutine('ahe430_heart')
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f68656172742e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ahe430_transform')
    sprite('null', 11)
    Unknown1096(4640)
    Unknown4007(0)
    Unknown3001(210)
    physicsXImpulse(-8000)
    Unknown1099(342)
    Unknown3004(-15)

@State
def ahe430_heart_a2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        callSubroutine('ahe430_heart')
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f68656172745f30322e4449000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ahe430_transform')
    sprite('null', 7)
    Unknown1096(4640)
    callSubroutine('ahe273_color')
    physicsXImpulse(-8000)
    Unknown4007(0)
    Unknown1099(342)
    Unknown3001(0)
    sprite('null', 3)
    Unknown3004(36)
    sprite('null', 3)
    Unknown3004(-30)
    Unknown3022(-50)
    Unknown3016(-50)

@State
def ahe430_heart_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        callSubroutine('ahe430_heart')
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f68656172745f30302e4449000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ahe430_transform')
        Unknown3032()
    sprite('null', 6)
    Unknown1096(4640)
    callSubroutine('ahe273_color')
    Unknown3001(180)
    physicsXImpulse(-8000)
    Unknown4007(0)
    Unknown1099(342)
    sprite('null', 5)
    Unknown3004(-36)

@State
def ahe430_heart_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        callSubroutine('ahe430_heart')
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f68656172745f30312e4449000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ahe430_transform')
    sprite('null', 11)
    Unknown1096(4640)
    physicsXImpulse(-8000)
    Unknown4007(0)
    Unknown3001(146)
    Unknown3004(-36)
    Unknown1099(342)

@State
def ahe430_particle_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(200000)
        Unknown1007(140000)
        Unknown2055(13)
    label(0)
    sprite('null', 1)
    GFX_1('aheef430_dust', 100)
    gotoLabel(0)

@State
def ahe320_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(-10000)
        Unknown1007(112000)
        Unknown4003('61686565665f69726f6e666973742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown1056(400)
    Unknown1064(500)

@State
def ahe320_attack2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(82000)
        Unknown1007(190000)
        Unknown4003('61686565665f686561727466756c6c70756e63685f68616e642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 2)
    Unknown1096(3500)
    sprite('null', 2)
    teleportRelativeX(1000)
    Unknown1007(12000)
    sprite('null', 2)
    Unknown1073(-3000)
    Unknown1096(4000)
    teleportRelativeX(10000)
    Unknown1007(60000)

@State
def ahe320_attack3_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(8000)
        Unknown1007(44000)
        Unknown4003('61686565665f69726f6e666973742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 12)
    Unknown1056(800)
    Unknown1064(500)
    Unknown1072(-75000)
    sprite('null', 3)
    Unknown3004(-85)

@State
def ahe320_airattack_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(15000)
        Unknown1007(200000)
        Unknown4003('61686565665f69726f6e666973742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)
    Unknown1056(400)
    Unknown1064(500)

@State
def ahe320_airattack2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(90000)
        Unknown1007(278000)
        Unknown4003('61686565665f686561727466756c6c70756e63685f68616e642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 3)
    Unknown1096(3500)
    sprite('null', 3)
    Unknown1007(10000)
    sprite('null', 3)
    Unknown1073(-3000)
    Unknown1096(4000)
    teleportRelativeX(10000)
    Unknown1007(60000)

@State
def ahe320_wing_eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 4038):
                sendToLabel(1)
    sprite('null', 15)
    GFX_0('ahe320_wing_a_eff', 100)
    GFX_0('ahe320_wing_b_eff', 100)
    label(1)
    sprite('null', 1)
    Unknown26('ahe320_wing_a_eff')
    Unknown26('ahe320_wing_b_eff')

@State
def ahe320_wing_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(10000)
        Unknown1007(55000)
    sprite('null', 15)
    Unknown1056(1500)
    Unknown1064(2900)
    Unknown1072(15000)
    Unknown1059(93)

@State
def ahe320_wing_b_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(-40000)
        Unknown1007(-125000)
    sprite('null', 5)
    Unknown1056(700)
    Unknown1064(2000)
    Unknown1072(15000)
    callSubroutine('ahe430_color')
    Unknown3001(60)
    Unknown1059(40)
    sprite('null', 7)
    Unknown3004(0)
    sprite('null', 3)

@State
def ahe320_heart_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 3)
    sprite('null', 6)
    GFX_0('ahe320_heart_wing_eff', 100)
    sprite('null', 40)
    GFX_0('ahe320_heart_bg_eff', 100)
    GFX_0('ahe320_heart_a2_eff', 100)
    GFX_0('ahe320_heart_a_eff', 100)
    GFX_0('ahe320_heart_b2_eff', 100)
    GFX_0('ahe320_heart_b_eff', 100)
    GFX_0('ahe320_heart_flash_eff', 100)

@State
def ahe320_heart_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(4400)
    Unknown1064(4000)
    Unknown3001(0)
    Unknown3004(42)
    callSubroutine('ahe320_speed')
    sprite('null', 12)
    callSubroutine('ahe320_speed_01')
    sprite('null', 8)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown1099(100)
    Unknown3004(-25)

@State
def ahe320_heart_a2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(4180)
    Unknown1064(3800)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    callSubroutine('ahe320_speed')
    sprite('null', 7)
    callSubroutine('ahe320_speed_01')
    sprite('null', 6)
    callSubroutine('ahe320_speed_02')
    sprite('null', 7)
    Unknown3004(5)
    sprite('null', 9)
    Unknown1099(100)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe320_heart_b_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(1375)
    Unknown1064(1250)
    Unknown3001(0)
    Unknown1059(51)
    Unknown1067(46)
    Unknown3004(42)
    callSubroutine('ahe320_speed')
    sprite('null', 12)
    callSubroutine('ahe320_speed_01')
    sprite('null', 8)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown3004(-25)
    Unknown1099(80)

@State
def ahe320_heart_b2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(1265)
    Unknown1064(1150)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    Unknown1059(44)
    Unknown1067(40)
    callSubroutine('ahe320_speed')
    sprite('null', 7)
    callSubroutine('ahe320_speed_01')
    sprite('null', 6)
    callSubroutine('ahe320_speed_02')
    sprite('null', 7)
    Unknown3004(5)
    sprite('null', 9)
    Unknown1099(100)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe320_heart_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(4400)
    Unknown1064(4000)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    Unknown3004(30)
    callSubroutine('ahe320_speed')
    sprite('null', 12)
    callSubroutine('ahe320_speed_01')
    Unknown3004(0)
    sprite('null', 8)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown1099(100)
    Unknown3004(-18)

@State
def ahe320_heart_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 2)
    Unknown1056(4400)
    Unknown1064(4000)
    Unknown3014(-48)
    Unknown3020(-1)
    Unknown3001(220)
    callSubroutine('ahe320_speed')
    sprite('null', 4)
    Unknown3004(-15)
    sprite('null', 11)
    callSubroutine('ahe320_speed_01')
    sprite('null', 15)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown1099(-400)

@State
def ahe320_heart_wing_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
        Unknown23015(10)
    sprite('null', 2)
    Unknown1056(3600)
    Unknown1064(3600)
    teleportRelativeX(-10000)
    physicsXImpulse(1666)
    Unknown1007(-70000)
    physicsYImpulse(15000)
    sprite('null', 4)
    physicsYImpulse(10000)
    sprite('null', 6)
    Unknown1099(0)
    Unknown3004(-10)
    Unknown4007(0)
    callSubroutine('ahe320_speed')
    sprite('null', 7)
    callSubroutine('ahe320_speed_01')
    sprite('null', 13)
    callSubroutine('ahe320_speed_02')
    sprite('null', 2)
    Unknown1099(200)
    sprite('null', 12)
    Unknown3022(-8)
    Unknown3016(-8)

@State
def ahe320_airheart_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
    sprite('null', 3)
    sprite('null', 6)
    GFX_0('ahe320_airheart_wing_eff', 100)
    sprite('null', 40)
    GFX_0('ahe320_airheart_bg_eff', 100)
    GFX_0('ahe320_airheart_a2_eff', 100)
    GFX_0('ahe320_airheart_a_eff', 100)
    GFX_0('ahe320_airheart_b2_eff', 100)
    GFX_0('ahe320_airheart_b_eff', 100)
    GFX_0('ahe320_airheart_flash_eff', 100)

@State
def ahe320_airheart_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(4400)
    Unknown1064(4000)
    Unknown3001(0)
    Unknown3004(42)
    callSubroutine('ahe320_air_speed')
    sprite('null', 12)
    callSubroutine('ahe320_air_speed_01')
    sprite('null', 8)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown1099(100)
    Unknown3004(-25)

@State
def ahe320_airheart_a2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(4180)
    Unknown1064(3800)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    callSubroutine('ahe320_air_speed')
    sprite('null', 7)
    callSubroutine('ahe320_air_speed_01')
    sprite('null', 6)
    callSubroutine('ahe320_speed_02')
    sprite('null', 7)
    Unknown3004(5)
    sprite('null', 9)
    Unknown1099(100)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe320_airheart_b_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(1375)
    Unknown1064(1250)
    Unknown3001(0)
    Unknown1059(51)
    Unknown1067(46)
    Unknown3004(42)
    callSubroutine('ahe320_air_speed')
    sprite('null', 12)
    callSubroutine('ahe320_air_speed_01')
    sprite('null', 8)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown3004(-25)
    Unknown1099(80)

@State
def ahe320_airheart_b2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(1265)
    Unknown1064(1265)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    Unknown1059(44)
    Unknown1067(40)
    callSubroutine('ahe320_air_speed')
    sprite('null', 7)
    callSubroutine('ahe320_air_speed_01')
    sprite('null', 6)
    callSubroutine('ahe320_speed_02')
    sprite('null', 7)
    Unknown3004(5)
    sprite('null', 9)
    Unknown1099(100)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe320_airheart_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        callSubroutine('ahe320_heart')
    sprite('null', 6)
    Unknown1056(4400)
    Unknown1064(4000)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    Unknown3004(30)
    callSubroutine('ahe320_air_speed')
    sprite('null', 12)
    callSubroutine('ahe320_air_speed_01')
    Unknown3004(0)
    sprite('null', 8)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown1099(100)
    Unknown3004(-18)

@State
def ahe320_airheart_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
    sprite('null', 2)
    Unknown1056(4400)
    Unknown1064(4000)
    Unknown3014(-48)
    Unknown3020(-1)
    Unknown3001(220)
    callSubroutine('ahe320_air_speed')
    sprite('null', 4)
    Unknown3004(-15)
    sprite('null', 11)
    callSubroutine('ahe320_air_speed_01')
    sprite('null', 15)
    callSubroutine('ahe320_speed_02')
    sprite('null', 10)
    Unknown1059(-440)
    Unknown1067(-400)

@State
def ahe320_airheart_wing_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe320_heart')
        Unknown23015(10)
    sprite('null', 2)
    Unknown1056(3600)
    Unknown1064(3600)
    teleportRelativeX(-10000)
    physicsXImpulse(1666)
    Unknown1007(-70000)
    physicsYImpulse(15000)
    sprite('null', 4)
    physicsYImpulse(10000)
    sprite('null', 6)
    Unknown1099(0)
    Unknown3004(-10)
    Unknown4007(0)
    callSubroutine('ahe320_air_speed')
    sprite('null', 7)
    callSubroutine('ahe320_air_speed_01')
    sprite('null', 13)
    callSubroutine('ahe320_speed_02')
    sprite('null', 2)
    Unknown1099(200)
    sprite('null', 12)
    Unknown3022(-8)
    Unknown3016(-8)

@Subroutine
def ahe320_heart():
    teleportRelativeX(0)
    Unknown1007(10000)
    Unknown1072(12000)

@Subroutine
def ahe320_speed():
    physicsXImpulse(1000)
    physicsYImpulse(6000)

@Subroutine
def ahe320_speed_01():
    physicsXImpulse(500)
    physicsYImpulse(2000)

@Subroutine
def ahe320_speed_02():
    physicsXImpulse(0)
    physicsYImpulse(1)

@Subroutine
def ahe320_air_speed():
    physicsXImpulse(500)
    physicsYImpulse(3000)

@Subroutine
def ahe320_air_speed_01():
    physicsXImpulse(250)
    physicsYImpulse(1000)

@State
def ahe431_wing_eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4015()

        def upon_43():
            if (SLOT_48 == 4038):
                sendToLabel(1)
    sprite('null', 15)
    GFX_0('ahe320_wing_a_eff', 100)
    GFX_0('ahe320_wing_b_eff', 100)
    GFX_0('ahe431_dust_eff', 100)
    label(1)
    sprite('null', 1)
    Unknown26('ahe320_wing_a_eff')
    Unknown26('ahe320_wing_b_eff')
    Unknown26('ahe431_dust_eff')

@State
def ahe431_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(2)
        teleportRelativeX(10000)
        Unknown1007(50000)
        Unknown2055(15)
    label(0)
    sprite('null', 1)
    GFX_1('aheef431_dust', 100)
    GFX_0('ahe431_dust_01_eff', 100)
    gotoLabel(0)

@State
def ahe431_dust_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        GFX_2('aheef431_dust_00')
    sprite('null', 50)
    Unknown1096(1700)
    physicsYImpulse(-7000)
    Unknown1026(-2000, -6000)
    Unknown1010(10000, -15000)
    Unknown1025(7000, -20000)

@State
def ahe431_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f68616e642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(82000)
        Unknown1007(190000)
        sendToLabelUpon(32, 1)
        Unknown2054(1)
    sprite('null', 3)
    Unknown1096(3500)
    sprite('null', 2)
    teleportRelativeX(2000)
    Unknown1007(10000)
    sprite('null', 2)
    Unknown1073(-3000)
    Unknown1096(4000)
    teleportRelativeX(5000)
    Unknown1007(60000)
    sprite('null', 0)
    Unknown13(25)
    label(1)
    sprite('null', 3)
    Unknown1007(8000)
    sprite('null', 3)
    Unknown1073(-3000)
    Unknown1096(4000)
    teleportRelativeX(5000)
    Unknown1007(60000)

@State
def ahe431_hit_wing_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4015()
    sprite('null', 45)
    GFX_0('ahe431_hit_wing_a_eff', 100)
    GFX_0('ahe431_hit_wing_b_eff', 100)
    GFX_0('ahe431_hit_dust_eff', 100)

@State
def ahe431_hit_wing_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f6c6f6e672e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(20000)
        Unknown1007(90000)
    sprite('null', 45)
    Unknown1056(5220)
    Unknown1064(5220)
    Unknown1072(15000)

@State
def ahe431_hit_wing_b_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(-30000)
        Unknown1007(-90000)
    sprite('null', 45)
    Unknown1056(2340)
    Unknown1064(3600)
    Unknown1072(15000)
    callSubroutine('ahe430_color')

@State
def ahe431_attack_upper_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4015()
    sprite('null', 65)
    GFX_0('ahe431_attack_upper_02_eff', 100)
    GFX_0('ahe431_attack_upper_01_eff', 100)

@State
def ahe431_attack_upper_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4015()
        Unknown2054(1)
        teleportRelativeX(20000)
        Unknown1007(90000)
        Unknown4003('61686565665f6c6f76655f69726f6e666973742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 59)
    Unknown1056(2500)
    Unknown1064(2400)
    Unknown1072(-75000)
    sprite('null', 6)
    Unknown1067(-400)

@State
def ahe431_attack_upper_02_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4015()
        Unknown2054(1)
        teleportRelativeX(25000)
        Unknown1007(100000)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 59)
    Unknown1056(2400)
    Unknown1064(2300)
    Unknown1072(-75000)
    callSubroutine('ahe430_color')
    sprite('null', 6)
    Unknown1067(-383)

@State
def ahe431_hit_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        teleportRelativeX(10000)
        Unknown1007(50000)
        Unknown2055(53)
    label(0)
    sprite('null', 1)
    GFX_1('aheef431_dust', 100)
    GFX_1('aheef431_dust', 100)
    GFX_0('ahe431_dust_01_eff', 100)
    GFX_0('ahe431_dust_01_eff', 100)
    gotoLabel(0)

@State
def ahe431_heart_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
    sprite('null', 3)
    sprite('null', 6)
    GFX_0('ahe431_heart_wing_eff', 100)
    sprite('null', 20)
    GFX_0('ahe431_heart_bg_eff', 100)
    GFX_0('ahe431_heart_a2_eff', 100)
    GFX_0('ahe431_heart_a_eff', 100)
    GFX_0('ahe431_heart_b2_eff', 100)
    GFX_0('ahe431_heart_b_eff', 100)
    GFX_0('ahe431_heart_flash_eff', 100)

@Subroutine
def ahe431_transform():
    Unknown1072(12000)

@Subroutine
def ahe431_speed():
    physicsXImpulse(500)
    physicsYImpulse(3000)

@Subroutine
def ahe431_speed_01():
    physicsXImpulse(250)
    physicsYImpulse(1000)

@Subroutine
def ahe431_speed_02():
    physicsXImpulse(0)
    physicsYImpulse(1)

@State
def ahe431_heart_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe431_transform')
    sprite('null', 6)
    Unknown1056(7040)
    Unknown1064(6400)
    Unknown3001(0)
    Unknown3004(42)
    callSubroutine('ahe431_speed')
    sprite('null', 12)
    callSubroutine('ahe431_speed_01')
    sprite('null', 8)
    callSubroutine('ahe431_speed_02')
    sprite('null', 10)
    Unknown1099(200)
    Unknown3004(-25)

@State
def ahe431_heart_a2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe431_transform')
    sprite('null', 6)
    Unknown1056(6688)
    Unknown1064(6080)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    callSubroutine('ahe431_speed')
    sprite('null', 12)
    callSubroutine('ahe431_speed_01')
    sprite('null', 8)
    Unknown3004(5)
    callSubroutine('ahe431_02')
    sprite('null', 8)
    Unknown1099(200)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe431_heart_b_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe431_transform')
    sprite('null', 6)
    Unknown1056(2200)
    Unknown1064(2000)
    Unknown1059(60)
    Unknown1067(55)
    Unknown3001(0)
    Unknown3004(42)
    callSubroutine('ahe431_speed')
    sprite('null', 12)
    callSubroutine('ahe431_speed_01')
    sprite('null', 8)
    callSubroutine('ahe431_speed_02')
    sprite('null', 10)
    Unknown1099(160)
    Unknown3004(-25)

@State
def ahe431_heart_b2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe431_transform')
    sprite('null', 6)
    Unknown1056(2024)
    Unknown1064(1839)
    Unknown1059(49)
    Unknown1067(45)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    callSubroutine('ahe431_speed')
    sprite('null', 12)
    callSubroutine('ahe431_speed_01')
    sprite('null', 8)
    Unknown3004(5)
    callSubroutine('ahe431_speed_02')
    sprite('null', 8)
    Unknown1099(160)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe431_heart_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe431_transform')
        Unknown3032()
    sprite('null', 6)
    Unknown1056(7040)
    Unknown1064(6400)
    Unknown3001(0)
    Unknown3004(30)
    callSubroutine('ahe273_color')
    callSubroutine('ahe431_speed')
    sprite('null', 12)
    Unknown3004(0)
    callSubroutine('ahe431_speed_01')
    sprite('null', 8)
    callSubroutine('ahe431_speed_02')
    sprite('null', 10)
    Unknown1099(200)
    Unknown3004(-18)

@State
def ahe431_heart_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe431_transform')
    sprite('null', 2)
    Unknown1056(7040)
    Unknown1064(6400)
    Unknown3014(-48)
    Unknown3020(-1)
    Unknown3001(255)
    callSubroutine('ahe431_speed')
    sprite('null', 4)
    Unknown3004(-15)
    sprite('null', 12)
    callSubroutine('ahe431_speed_01')
    sprite('null', 8)
    callSubroutine('ahe431_speed_02')
    sprite('null', 10)
    Unknown1059(-704)
    Unknown1067(-640)

@State
def ahe431_heart_wing_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(0)
        callSubroutine('ahe431_transform')
    sprite('null', 2)
    Unknown1056(5760)
    Unknown1064(5760)
    teleportRelativeX(-10000)
    physicsXImpulse(1666)
    Unknown1007(-70000)
    physicsYImpulse(15000)
    sprite('null', 4)
    physicsYImpulse(10000)
    sprite('null', 6)
    Unknown1099(0)
    Unknown3004(-10)
    Unknown4007(0)
    callSubroutine('ahe431_speed')
    sprite('null', 7)
    callSubroutine('ahe431_speed_01')
    sprite('null', 13)
    callSubroutine('ahe431_speed_02')
    sprite('null', 2)
    Unknown1099(200)
    sprite('null', 12)
    Unknown3022(-8)
    Unknown3016(-8)

@State
def ahe406_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f69726f6e666973742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(37000)
        Unknown1007(100000)
        sendToLabelUpon(32, 0)
    label(1)
    sprite('null', 2)
    Unknown1072(80000)
    Unknown1056(500)
    Unknown1064(700)
    Unknown1099(50)
    sprite('null', 32767)
    Unknown1056(1400)
    Unknown1064(1100)
    Unknown1099(7)
    teleportRelativeX(18000)
    Unknown1007(-130000)
    gotoLabel(1)
    label(0)
    sprite('null', 8)
    Unknown1059(50)
    Unknown1067(-125)
    Unknown3022(-18)
    Unknown3016(-18)
    Unknown4007(0)
    GFX_0('ahe406_impact_eff', 100)

@State
def ahe406_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(35000)
        Unknown1007(80000)
        sendToLabelUpon(32, 0)
    sprite('null', 2)
    label(1)
    sprite('null', 1)
    GFX_0('ahe406_dust1_eff', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 1)

@State
def ahe406_dust1_eff():

    def upon_IMMEDIATE():
        GFX_2('aheef400_particle')
    sprite('null', 30)
    Unknown1072(82000)

@State
def ahe407_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(35000)
        Unknown1007(80000)
        sendToLabelUpon(32, 0)
    sprite('null', 2)
    label(1)
    sprite('null', 1)
    GFX_0('ahe407_dust1_eff', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 1)

@State
def ahe407_dust1_eff():

    def upon_IMMEDIATE():
        GFX_2('aheef401_particle')
    sprite('null', 30)
    Unknown1072(82000)

@State
def ahe408_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(35000)
        Unknown1007(20000)
        sendToLabelUpon(32, 0)
    sprite('null', 2)
    sprite('null', 0)
    GFX_0('ahe408_line_eff', 100)
    label(1)
    sprite('null', 4)
    GFX_0('ahe408_dust1_eff', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 8)
    Unknown21012('6168653430385f6c696e655f656666000000000000000000000000000000000020000000')

@State
def ahe408_dust1_eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 30)
    GFX_2('aheef402_ring')
    Unknown1072(82000)
    physicsXImpulse(-1000)
    physicsYImpulse(8000)

@State
def ahe408_line_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('61686565665f69726f6e666973745f6c6f6375732e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(0)
        Unknown1007(80000)
        sendToLabelUpon(32, 0)
        Unknown23015(11)
    sprite('null', 32767)
    Unknown1056(100)
    Unknown1064(270)
    Unknown1059(620)
    Unknown1072(84000)
    label(0)
    sprite('null', 8)
    Unknown1059(0)
    Unknown1067(-33)
    Unknown3022(-21)
    Unknown3016(-21)

@State
def ahe406_impact_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        GFX_2('aheef406_impact')
        Unknown23015(15)
        Unknown1007(20000)
    sprite('null', 24)

@State
def ahe432_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 2)
    GFX_0('ahe432_attack_01_eff', 100)
    sprite('null', 32767)
    GFX_0('ahe432_attack_02_eff', 100)
    GFX_0('ahe432_attack_03_eff', 100)
    GFX_0('ahe432_shockwave_01_eff', 100)
    GFX_0('ahe432_shockwave_eff', 100)
    GFX_0('ahe432_foot_eff', 100)
    label(0)
    sprite('null', 12)
    Unknown21012('6168653433325f61747461636b5f30315f65666600000000000000000000000020000000')
    Unknown21012('6168653433325f61747461636b5f30325f65666600000000000000000000000020000000')
    Unknown21012('6168653433325f61747461636b5f30335f65666600000000000000000000000020000000')
    Unknown21012('6168653433325f7061727469636c655f6566660000000000000000000000000020000000')
    Unknown21012('6168653433325f647573745f656666000000000000000000000000000000000020000000')
    Unknown21012('6168653433325f666f6f745f656666000000000000000000000000000000000020000000')
    GFX_0('ahe432_impact_eff', 100)
    GFX_0('ahe432_impact_02_eff', 100)
    GFX_0('ahe432_impact_01_eff', 100)

@State
def ahe432_foot_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        GFX_2('aheef432_kick')
        teleportRelativeX(35000)
        Unknown1007(99000)
        Unknown1072(-10000)
        Unknown1096(880)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 4)
    Unknown3004(-64)

@State
def ahe432_attack_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown4003('61686565665f6c6f76655f69726f6e666973742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(40000)
        Unknown1007(90000)
        Unknown23015(11)
    sprite('null', 2)
    Unknown1072(72000)
    Unknown1056(800)
    Unknown1064(800)
    Unknown1059(100)
    Unknown1067(75)
    sprite('null', 32767)
    Unknown1056(2200)
    Unknown1064(1700)
    Unknown1059(0)
    Unknown1067(0)
    teleportRelativeX(15000)
    Unknown1007(-110000)
    label(0)
    sprite('null', 8)
    Unknown1072(80000)
    Unknown1059(50)
    Unknown1067(-212)
    Unknown3022(-18)
    Unknown3016(-18)

@State
def ahe432_attack_02_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(50000)
        Unknown1007(-30000)
    sprite('null', 32767)
    Unknown1072(80000)
    Unknown1056(2400)
    Unknown1064(1700)
    callSubroutine('ahe430_color')
    label(0)
    sprite('null', 8)
    Unknown1072(80000)
    Unknown1067(-187)
    Unknown3004(-28)

@State
def ahe432_attack_03_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(10000)
        Unknown1007(225000)
    sprite('null', 32767)
    Unknown1072(75000)
    Unknown1056(2600)
    Unknown1064(1700)
    callSubroutine('ahe430_color')
    Unknown3001(80)
    label(0)
    sprite('null', 8)
    Unknown1072(80000)
    teleportRelativeX(10000)
    Unknown1067(-162)
    Unknown3004(-10)

@State
def ahe432_shockwave_eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('61686565665f6465617468626c6f776b69636b5f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(10)
        teleportRelativeX(50000)
        Unknown1007(-150000)
    sprite('null', 10)
    Unknown1096(3000)
    Unknown1064(2000)
    Unknown1099(375)
    Unknown1067(250)
    Unknown1072(-8000)
    Unknown3001(191)
    Unknown3020(-47)
    Unknown3014(-71)

@State
def ahe432_shockwave_01_eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('61686565665f6465617468626c6f776b69636b5f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        teleportRelativeX(50000)
        Unknown1007(-150000)
    sprite('null', 10)
    Unknown1096(3000)
    Unknown1064(2000)
    Unknown1099(375)
    Unknown1067(250)
    Unknown1072(-8000)
    Unknown3001(191)
    Unknown3020(-63)
    Unknown3014(-95)

@State
def ahe432_impact_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        GFX_2('aheef406_impact')
        Unknown23015(15)
        teleportRelativeX(50000)
        Unknown1096(1500)
    sprite('null', 24)

@State
def ahe432_impact_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('61686565665f6465617468626c6f776b69636b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(50000)
    sprite('null', 3)
    Unknown1096(1500)
    Unknown1099(250)
    Unknown4007(0)
    sprite('null', 9)
    Unknown3004(-28)
    Unknown3022(-16)
    Unknown3016(-16)

@State
def ahe432_impact_02_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('61686565665f6465617468626c6f776b69636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        teleportRelativeX(50000)
    sprite('null', 3)
    Unknown1096(1500)
    Unknown1099(250)
    Unknown4007(0)
    sprite('null', 9)
    Unknown3004(-28)
    Unknown3022(-16)
    Unknown3016(-16)

@State
def ahe432_particle_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        sendToLabelUpon(32, 0)
        teleportRelativeX(30000)
        Unknown1007(80000)
    sprite('null', 2)
    label(1)
    sprite('null', 1)
    GFX_0('ahe432_particle_01_eff', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 1)

@State
def ahe432_particle_01_eff():

    def upon_IMMEDIATE():
        GFX_2('aheef401_particle')
    sprite('null', 30)
    Unknown1072(82000)
    Unknown1096(1200)

@State
def ahe432_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        sendToLabelUpon(32, 0)
        teleportRelativeX(35000)
        Unknown1007(20000)
    sprite('null', 2)
    sprite('null', 0)
    GFX_0('ahe432_line_eff', 100)
    label(1)
    sprite('null', 4)
    GFX_0('ahe432_dust_01_eff', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 7)
    Unknown21012('6168653433325f6c696e655f656666000000000000000000000000000000000020000000')

@State
def ahe432_dust_01_eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 30)
    GFX_2('aheef402_ring')
    Unknown1096(1200)
    Unknown1072(82000)
    physicsXImpulse(-1000)
    physicsYImpulse(12000)

@State
def ahe432_line_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown4003('61686565665f69726f6e666973745f6c6f6375732e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
        teleportRelativeX(0)
        Unknown1007(80000)
    sprite('null', 32767)
    Unknown1056(1000)
    Unknown1064(460)
    Unknown1059(620)
    Unknown1072(84000)
    label(0)
    sprite('null', 7)
    Unknown1059(0)
    Unknown1067(-65)
    Unknown3022(-21)
    Unknown3016(-21)

@State
def ahe403_shot_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('aheef403_shot')

        def upon_STATE_END():
            GFX_1('aheef403_hit', 100)
    sprite('null', 300)
    GFX_0('ahe403_shot_dust_eff', 100)
    SFX_3('ahese_52')

@State
def ahe403_shot_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2055(300)
    label(0)
    sprite('null', 3)
    GFX_1('aheef403_dust', 100)
    gotoLabel(0)

@State
def ahe403_circle_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown2055(100)
    sprite('null', 32767)
    GFX_0('ahe403_circle2_eff', 100)
    GFX_0('ahe403_circle1_eff', 100)
    label(0)
    sprite('null', 25)
    Unknown4007(0)
    Unknown21012('6168653430335f636972636c65315f656666000000000000000000000000000020000000')
    Unknown21012('6168653430335f636972636c65325f656666000000000000000000000000000020000000')

@State
def ahe403_circle1_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a737068616572615f6d616769637371756172655f3030000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        sendToLabelUpon(32, 0)
        Unknown2055(100)
    sprite('null', 5)
    Unknown1096(1560)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)
    label(0)
    sprite('null', 13)
    Unknown3004(-19)

@State
def ahe403_circle2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a737068616572615f6d616769637371756172655f3031000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        sendToLabelUpon(32, 0)
        Unknown2055(100)
    sprite('null', 5)
    Unknown1096(1560)
    callSubroutine('ahe403_color')
    Unknown3001(0)
    Unknown3004(10)
    sprite('null', 32767)
    Unknown3004(0)
    label(0)
    sprite('null', 13)
    Unknown3004(-3)

@State
def ahe403_footcircle_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown2055(100)
    sprite('null', 32767)
    GFX_0('ahe403_footcircle2_eff', 100)
    GFX_0('ahe403_footcircle1_eff', 100)
    GFX_0('ahe403_footparticle_eff', 100)
    SFX_3('ahese_55')
    label(0)
    sprite('null', 1)
    Unknown4007(0)
    Unknown21012('6168653430335f666f6f74636972636c65315f6566660000000000000000000020000000')
    Unknown21012('6168653430335f666f6f74636972636c65325f6566660000000000000000000020000000')
    Unknown26('ahe403_footparticle_eff')

@State
def ahe403_footcircle1_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a737068616572615f666f6f745f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        Unknown1007(-10000)
        sendToLabelUpon(32, 0)
        Unknown2055(100)
    sprite('null', 15)
    Unknown1096(0)
    Unknown1099(300)
    Unknown3001(255)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 15)
    Unknown1099(0)
    Unknown3004(-17)

@State
def ahe403_footcircle2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a737068616572615f666f6f745f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        Unknown3032()
        Unknown1007(-10000)
        sendToLabelUpon(32, 0)
        Unknown2055(100)
    sprite('null', 15)
    Unknown1096(0)
    Unknown1099(300)
    callSubroutine('ahe403_color')
    Unknown3001(50)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 15)
    Unknown1099(0)
    Unknown3004(-3)

@State
def ahe403_footparticle_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown1007(-30000)
        Unknown2055(100)
    label(0)
    sprite('null', 7)
    GFX_0('ahe403_footparticle1_eff', 100)
    sprite('null', 6)
    GFX_0('ahe403_footparticle2_eff', 100)
    sprite('null', 7)
    GFX_0('ahe403_footparticle3_eff', 100)
    sprite('null', 6)
    GFX_0('ahe403_footparticle4_eff', 100)
    gotoLabel(0)

@State
def ahe403_footparticle1_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4022(3)
        GFX_2('aheef403_footparticle')
    sprite('null', 20)
    callSubroutine('ahe403_footparticle')
    Unknown1010(150000, 100000)

@State
def ahe403_footparticle2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4022(3)
        GFX_2('aheef403_footparticle')
    sprite('null', 20)
    callSubroutine('ahe403_footparticle')
    Unknown1010(-100000, -150000)

@State
def ahe403_footparticle3_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4022(3)
        GFX_2('aheef403_footparticle')
    sprite('null', 20)
    callSubroutine('ahe403_footparticle')
    Unknown1010(100000, -100000)

@State
def ahe403_footparticle4_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4022(3)
        GFX_2('aheef403_footparticle')
    sprite('null', 20)
    callSubroutine('ahe403_footparticle')
    Unknown1010(100000, -100000)

@Subroutine
def ahe403_footparticle():
    Unknown1011(30000, 0)
    Unknown1096(700)
    Unknown1077(360000, 0)
    physicsYImpulse(7000)
    Unknown1026(6000, 0)

@State
def ahe405_shot_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
    sprite('null', 18)
    GFX_0('ahe405_shot_beam_eff', 100)
    GFX_0('ahe405_shot_sphere1_eff', 100)
    SFX_3('ahese_51')

@State
def ahe405_shot_beam_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a746f786f5f6d616769636265616d2e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(35000)
    sprite('null', 10)
    Unknown1056(10000)
    Unknown1064(3500)
    Unknown3001(0)
    Unknown3004(51)
    GFX_1('aheef405_bloom', 100)
    sprite('null', 5)
    Unknown3004(-6)
    Unknown1067(-300)
    sprite('null', 3)
    GFX_1('aheef405_residue', 100)
    sprite('null', 0)
    Unknown4007(0)

@State
def ahe405_shot_sphere1_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(15000)
    sprite('null', 30)
    GFX_2('aheef405_core')

@State
def ahe405_circle_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        sendToLabelUpon(32, 0)
    sprite('null', 28)
    GFX_0('ahe403_circle_eff', 100)
    GFX_0('ahe405_circle1b_eff', 100)
    GFX_0('ahe405_circle1a_eff', 100)
    GFX_0('ahe405_circle2b_eff', 100)
    GFX_0('ahe405_circle2a_eff', 100)
    label(0)
    sprite('null', 1)

@State
def ahe405_circle1a_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a746f786f5f6d616769637371756172652e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(55000)
        Unknown2055(40)
    sprite('null', 5)
    Unknown1096(2000)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 6)
    sprite('null', 4)
    Unknown3004(-19)
    physicsXImpulse(-750)
    sprite('null', 9)
    Unknown4007(0)

@State
def ahe405_circle1b_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a746f786f5f6d616769637371756172655f30302e4449000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        teleportRelativeX(55000)
        Unknown2055(40)
    sprite('null', 5)
    Unknown1096(2000)
    callSubroutine('ahe403_color')
    Unknown3001(0)
    Unknown3004(24)
    sprite('null', 6)
    Unknown3004(0)
    sprite('null', 4)
    Unknown3004(-9)
    physicsXImpulse(-750)
    sprite('null', 9)
    Unknown4007(0)

@State
def ahe405_circle2a_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a746f786f5f6d61676963737175617265322e44494700000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(130000)
        Unknown2055(40)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 6)
    sprite('null', 4)
    Unknown3004(-19)
    physicsXImpulse(-2000)
    sprite('null', 9)
    Unknown4007(0)

@State
def ahe405_circle2b_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('61686565665f726f7a746f786f5f6d61676963737175617265325f30302e44000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        teleportRelativeX(130000)
        Unknown2055(40)
    sprite('null', 5)
    callSubroutine('ahe403_color')
    Unknown3001(0)
    Unknown3004(24)
    sprite('null', 6)
    Unknown3004(0)
    sprite('null', 4)
    Unknown3004(-9)
    physicsXImpulse(-2000)
    sprite('null', 9)
    Unknown4007(0)

@State
def ahe450_hold_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f7377696e6761726d2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
        teleportRelativeX(-130000)
        Unknown1007(145000)
    sprite('null', 18)
    Unknown1072(-15000)
    Unknown3001(0)
    sprite('null', 25)
    Unknown1096(3000)
    Unknown3004(10)
    sprite('null', 36)
    sprite('null', 12)
    Unknown4007(0)
    Unknown3004(-21)
    Unknown1099(166)

@State
def ahe450_impact_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('61686565665f6465617468626c6f776b69636b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(-65000)
    sprite('null', 3)
    GFX_0('ahe450_impact_01_eff', 100)
    Unknown1096(3000)
    Unknown1099(250)
    sprite('null', 9)
    Unknown3004(-28)
    Unknown3022(-16)
    Unknown3016(-16)

@State
def ahe450_impact_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4003('61686565665f6465617468626c6f776b69636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
    sprite('null', 3)
    sprite('null', 9)
    Unknown3004(-28)
    Unknown3022(-16)
    Unknown3016(-16)

@State
def ahe450_impact_02_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('61686565665f61737472616c686561745f696d706163742e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(6)
    sprite('null', 3)
    Unknown1056(2812)
    Unknown1064(1687)
    Unknown1059(625)
    Unknown1067(250)
    Unknown3001(100)
    callSubroutine('ahe273_color')
    sprite('null', 9)
    Unknown3004(-11)

@State
def ahe450_punch_eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4008(2)
        Unknown4009(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 21)
    GFX_0('ahe450_punch_02_eff', 100)
    GFX_0('ahe450_punch_04_eff', 100)
    GFX_0('ahe450_punch_01_eff', 100)
    GFX_0('ahe450_punch_03_eff', 100)
    label(0)
    sprite('null', 31)
    Unknown21012('6168653435305f70756e63685f30315f6566660000000000000000000000000020000000')
    Unknown21012('6168653435305f70756e63685f30325f6566660000000000000000000000000020000000')
    Unknown21012('6168653435305f70756e63685f30335f6566660000000000000000000000000020000000')
    Unknown21012('6168653435305f70756e63685f30345f6566660000000000000000000000000020000000')

@State
def ahe450_punch_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4008(3)
        Unknown4009(3)
        Unknown2054(1)
        Unknown4003('61686565665f6c6f76655f69726f6e666973742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
        teleportRelativeX(200000)
        Unknown1007(370000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    GFX_0('ahe450_dust_eff', 100)
    GFX_0('ahe450_cone_eff', 100)
    Unknown1072(-35000)
    Unknown1056(2500)
    Unknown1064(2400)
    sprite('null', 2)
    Unknown3022(-30)
    Unknown3016(-30)
    Unknown1067(-500)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1059(-333)
    Unknown1067(0)
    sprite('null', 0)
    Unknown21012('6168653435305f647573745f656666000000000000000000000000000000000020000000')
    Unknown13(25)
    label(0)
    sprite('null', 4)
    Unknown21012('6168653435305f72696e675f656666000000000000000000000000000000000020000000')
    sprite('null', 2)
    Unknown1067(-300)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1059(-200)
    Unknown1067(0)
    Unknown3022(-66)
    Unknown3016(-66)
    sprite('null', 1)
    Unknown21012('6168653435305f647573745f656666000000000000000000000000000000000020000000')
    Unknown1056(2500)
    Unknown1064(2400)
    Unknown1099(0)
    Unknown3001(0)
    Unknown3004(0)
    Unknown3022(0)
    Unknown3016(0)
    Unknown3023(200)
    Unknown3017(200)
    teleportRelativeX(400000)
    sprite('null', 12)
    Unknown3001(255)
    GFX_0('ahe450_cone2_eff', 100)
    GFX_0('ahe450_dust_eff', 100)
    sprite('null', 5)
    Unknown1059(-240)
    Unknown1067(-240)
    Unknown3004(-51)
    Unknown3022(-40)
    Unknown3016(-40)
    sprite('null', 3)
    Unknown3001(0)
    sprite('null', 0)
    Unknown21012('6168653435305f647573745f656666000000000000000000000000000000000020000000')

@State
def ahe450_punch_02_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4008(3)
        Unknown4009(3)
        Unknown2054(1)
        Unknown4003('61686565665f6c6f76655f69726f6e666973745f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(210000)
        Unknown1007(390000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Unknown1072(-35000)
    Unknown1056(2400)
    Unknown1064(2300)
    callSubroutine('ahe430_color')
    Unknown1059(160)
    Unknown1067(100)
    sprite('null', 2)
    Unknown1059(0)
    Unknown1067(-900)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1059(-666)
    Unknown1067(0)
    sprite('null', 0)
    Unknown13(25)
    label(0)
    sprite('null', 4)
    Unknown1059(0)
    Unknown1067(0)
    sprite('null', 2)
    Unknown1059(0)
    Unknown1067(-450)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1059(-466)
    Unknown1067(0)
    sprite('null', 1)
    Unknown1056(2400)
    Unknown1064(2300)
    Unknown1099(0)
    Unknown3001(0)
    Unknown3004(0)
    teleportRelativeX(400000)
    sprite('null', 12)
    Unknown3001(255)
    Unknown1059(133)
    Unknown1067(83)
    sprite('null', 2)
    Unknown1059(0)
    Unknown1067(-550)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1067(0)
    Unknown1059(-533)

@State
def ahe450_punch_03_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4008(3)
        Unknown4009(3)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f6261636b2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown23015(15)
        teleportRelativeX(280000)
        Unknown1007(440000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Unknown1072(-35000)
    Unknown1056(45000)
    Unknown1064(22000)
    Unknown3007(230)
    Unknown3019(169)
    Unknown3013(2)
    Unknown3001(200)
    sprite('null', 2)
    Unknown1059(0)
    Unknown1067(-1000)
    Unknown3004(-40)
    sprite('null', 3)
    Unknown1059(-8333)
    Unknown1067(0)
    sprite('null', 0)
    Unknown13(25)
    label(0)
    sprite('null', 4)
    sprite('null', 2)
    Unknown1059(0)
    Unknown1067(-1000)
    Unknown3004(-40)
    sprite('null', 3)
    Unknown1059(-8333)
    Unknown1067(0)
    sprite('null', 1)
    Unknown1056(45000)
    Unknown1064(22000)
    teleportRelativeX(560000)
    Unknown1007(-20000)
    Unknown1099(0)
    Unknown3001(0)
    Unknown3004(0)
    sprite('null', 8)
    Unknown3001(200)
    sprite('null', 4)
    Unknown1067(-500)
    Unknown1059(0)
    Unknown3004(-22)
    sprite('null', 5)
    Unknown1067(0)
    Unknown1059(-5000)

@State
def ahe450_punch_04_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4008(3)
        Unknown4009(3)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f70756e63682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(200000)
        Unknown1007(370000)
        sendToLabelUpon(32, 0)
        Unknown23015(11)
    sprite('null', 10)
    Unknown1072(-30000)
    Unknown1056(3500)
    Unknown1064(2200)
    Unknown1059(60)
    Unknown1067(40)
    sprite('null', 2)
    Unknown1059(0)
    Unknown1067(-300)
    Unknown3022(-30)
    Unknown3016(-30)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1059(-766)
    Unknown1067(0)
    sprite('null', 0)
    Unknown13(25)
    label(0)
    sprite('null', 4)
    Unknown1059(0)
    Unknown1067(0)
    sprite('null', 2)
    Unknown1067(-300)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1067(0)
    Unknown1059(-666)
    Unknown3022(-66)
    Unknown3016(-66)
    sprite('null', 1)
    Unknown1056(3500)
    Unknown1064(2200)
    Unknown1099(0)
    Unknown3001(0)
    Unknown3004(0)
    Unknown3022(0)
    Unknown3016(0)
    Unknown3023(200)
    Unknown3017(200)
    teleportRelativeX(400000)
    sprite('null', 12)
    Unknown3001(255)
    Unknown1059(50)
    Unknown1067(33)
    sprite('null', 2)
    Unknown1067(-400)
    Unknown1059(0)
    Unknown3004(-51)
    sprite('null', 3)
    Unknown1067(0)
    Unknown1059(-666)
    Unknown3022(-66)
    Unknown3016(-66)

@State
def ahe450_cone_eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown2054(1)
        teleportRelativeX(-140000)
        Unknown1007(-50000)
        sendToLabelUpon(32, 0)
    sprite('null', 30)
    Unknown4007(0)
    GFX_2('aheef450_ring')
    Unknown1072(-35000)
    physicsXImpulse(-8000)
    physicsYImpulse(-8000)
    label(0)
    sprite('null', 30)
    physicsXImpulse(-8000)
    physicsYImpulse(-6000)

@State
def ahe450_cone2_eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown2054(1)
        teleportRelativeX(40000)
        Unknown1007(-120000)
    sprite('null', 30)
    Unknown4007(0)
    GFX_2('aheef450_ring')
    Unknown1072(-38000)
    physicsXImpulse(-8000)
    physicsYImpulse(-6000)

@State
def ahe450_dust_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown2054(1)
        teleportRelativeX(-80000)
        Unknown1007(-80000)
        sendToLabelUpon(32, 0)
    label(1)
    sprite('null', 1)
    GFX_0('ahe450_dust_01_eff', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 0)

@State
def ahe450_dust_01_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown1072(-40000)
    sprite('null', 100)
    GFX_2('aheef450_dust')

@State
def ahe450_heart_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4009(2)
    sprite('null', 2)
    sprite('null', 6)
    GFX_0('ahe450_heart_wing_eff', 100)
    sprite('null', 20)
    GFX_0('ahe450_heart_bg_eff', 100)
    GFX_0('ahe450_heart_a2_eff', 100)
    GFX_0('ahe450_heart_a_eff', 100)
    GFX_0('ahe450_heart_b2_eff', 100)
    GFX_0('ahe450_heart_b_eff', 100)
    GFX_0('ahe450_heart_flash_eff', 100)

@Subroutine
def ahe450_transform():
    teleportRelativeX(160000)
    Unknown1007(110000)
    Unknown1072(12000)

@Subroutine
def ahe450_speed():
    physicsXImpulse(10000)
    physicsYImpulse(7000)

@Subroutine
def ahe450_speed_01():
    physicsXImpulse(5000)
    physicsYImpulse(4000)

@Subroutine
def ahe450_speed_02():
    physicsXImpulse(1000)
    physicsYImpulse(1000)

@State
def ahe450_heart_a_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe450_transform')
    sprite('null', 6)
    Unknown1056(5720)
    Unknown1064(5200)
    Unknown3001(0)
    Unknown3004(42)
    callSubroutine('ahe450_speed')
    sprite('null', 12)
    callSubroutine('ahe450_speed_01')
    sprite('null', 8)
    callSubroutine('ahe450_speed_02')
    sprite('null', 10)
    Unknown1099(150)
    Unknown3004(-25)

@State
def ahe450_heart_a2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe450_transform')
    sprite('null', 6)
    Unknown1056(5434)
    Unknown1064(4939)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    callSubroutine('ahe450_speed')
    sprite('null', 12)
    callSubroutine('ahe450_speed_01')
    sprite('null', 8)
    Unknown3004(5)
    callSubroutine('ahe450_02')
    sprite('null', 8)
    Unknown1099(150)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe450_heart_b_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe450_transform')
    sprite('null', 6)
    Unknown1056(1787)
    Unknown1064(1625)
    Unknown1059(49)
    Unknown1067(44)
    Unknown3001(0)
    Unknown3004(42)
    callSubroutine('ahe450_speed')
    sprite('null', 12)
    callSubroutine('ahe450_speed_01')
    sprite('null', 8)
    callSubroutine('ahe450_speed_02')
    sprite('null', 10)
    Unknown1099(195)
    Unknown3004(-25)

@State
def ahe450_heart_b2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe450_transform')
    sprite('null', 6)
    Unknown1056(1644)
    Unknown1064(1494)
    Unknown1059(40)
    Unknown1067(36)
    Unknown3001(0)
    callSubroutine('ahe273_color')
    callSubroutine('ahe450_speed')
    sprite('null', 12)
    callSubroutine('ahe450_speed_01')
    sprite('null', 8)
    Unknown3004(5)
    callSubroutine('ahe450_speed_02')
    sprite('null', 8)
    Unknown1099(195)
    sprite('null', 6)
    Unknown3004(-3)
    Unknown3022(-25)
    Unknown3016(-25)

@State
def ahe450_heart_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe450_transform')
        Unknown3032()
    sprite('null', 6)
    Unknown1056(5720)
    Unknown1064(5200)
    Unknown3001(0)
    Unknown3004(30)
    callSubroutine('ahe273_color')
    callSubroutine('ahe450_speed')
    sprite('null', 12)
    Unknown3004(0)
    callSubroutine('ahe450_speed_01')
    sprite('null', 8)
    callSubroutine('ahe450_speed_02')
    sprite('null', 10)
    Unknown1099(150)
    Unknown3004(-18)

@State
def ahe450_heart_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        callSubroutine('ahe450_transform')
    sprite('null', 2)
    Unknown1056(5720)
    Unknown1064(5200)
    Unknown3014(-48)
    Unknown3020(-1)
    Unknown3001(255)
    callSubroutine('ahe450_speed')
    sprite('null', 4)
    Unknown3004(-15)
    sprite('null', 12)
    callSubroutine('ahe450_speed_01')
    sprite('null', 8)
    callSubroutine('ahe450_speed_02')
    sprite('null', 10)
    Unknown1059(-572)
    Unknown1067(-520)

@State
def ahe450_heart_wing_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4003('61686565665f686561727466756c6c70756e63685f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(0)
        callSubroutine('ahe450_transform')
    sprite('null', 2)
    Unknown1056(4680)
    Unknown1064(4680)
    teleportRelativeX(-140000)
    physicsXImpulse(23333)
    Unknown1007(-150000)
    physicsYImpulse(35000)
    sprite('null', 4)
    physicsYImpulse(20000)
    sprite('null', 6)
    Unknown1099(0)
    Unknown3004(-10)
    Unknown4007(0)
    callSubroutine('ahe450_speed')
    sprite('null', 7)
    callSubroutine('ahe450_speed_01')
    sprite('null', 13)
    callSubroutine('ahe450_speed_02')
    sprite('null', 2)
    Unknown1099(150)
    sprite('null', 12)
    Unknown3022(-8)
    Unknown3016(-8)

@State
def ahe450_circle_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown21010(1)
        teleportRelativeX(10000)
        Unknown1007(240000)
    sprite('null', 60)
    GFX_0('ahe450_circl_bg_eff', 100)
    GFX_0('ahe450_circle1_eff', 100)
    GFX_0('ahe450_circle2_eff', 100)
    GFX_0('ahe450_circle3_eff', 100)
    GFX_1('aheef450_magicsquare', 100)

@State
def ahe450_circle1_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('61686565665f61737472616c686561745f6d616769637371756172652e4449000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown21010(1)
        Unknown23015(11)
    sprite('null', 10)
    Unknown1074(-8000)
    Unknown1096(0)
    Unknown1099(480)
    sprite('null', 10)
    sprite('null', 30)
    Unknown1099(0)
    sprite('null', 10)
    Unknown3004(-12)
    Unknown1075(2000)
    sprite('null', 10)
    Unknown1075(1000)

@State
def ahe450_circle2_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('61686565665f61737472616c686561745f6d616769637371756172655f3030000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown21010(1)
        Unknown23015(11)
    sprite('null', 10)
    Unknown1074(4000)
    Unknown1096(0)
    Unknown1099(480)
    sprite('null', 10)
    sprite('null', 30)
    Unknown1099(0)
    sprite('null', 10)
    Unknown3004(-12)
    Unknown1075(-1000)
    sprite('null', 10)
    Unknown1075(-500)

@State
def ahe450_circle3_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('61686565665f61737472616c686561745f6d616769637371756172655f3031000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown21010(1)
        Unknown23015(11)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(25)
    Unknown1096(19200)
    Unknown1099(-960)
    sprite('null', 10)
    Unknown1099(0)
    sprite('null', 25)
    Unknown1099(0)
    sprite('null', 20)
    Unknown1099(-480)
    Unknown3004(-12)

@State
def ahe450_circl_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('61686565665f61737472616c686561745f6d616769637371756172655f3032000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown21010(1)
        Unknown3032()
        Unknown23015(12)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(5)
    Unknown1096(19200)
    Unknown1099(-960)
    sprite('null', 10)
    Unknown3004(0)
    Unknown1099(0)
    sprite('null', 28)
    Unknown1099(0)
    sprite('null', 20)
    Unknown1099(-480)
    Unknown3004(-2)

@State
def ahe450_tinkle_eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown2054(1)
        teleportRelativeX(33000)
        Unknown1007(8000)
    label(0)
    sprite('null', 3)
    GFX_1('aheef450_tinkle', 100)
    gotoLabel(0)

@State
def ahe450_attack_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown2054(1)
        teleportRelativeX(0)
        Unknown1007(1400000)
    sprite('null', 105)
    Unknown4049(5000)
    Unknown4045('61686565663435305f636961636c65000000000000000000000000000000000064000000')
    GFX_0('ahe450_sphere_eff', 100)
    GFX_0('ahe450_particle_eff', 100)
    GFX_0('ahe450_ring_eff', 100)
    GFX_0('ahe450_ring_add_eff', 100)
    GFX_0('ahe450_ring_bg_eff', 100)
    GFX_0('ahe450_ring_bg_add_eff', 100)
    GFX_0('ahe450_ring_add2_eff', 100)
    GFX_0('ahe450_ring2_bg_eff', 100)
    GFX_0('ahe450_ring2_bg_add_eff', 100)
    GFX_0('ahe450_ring2_eff', 100)
    GFX_0('ahe450_ring2_add_eff', 100)
    GFX_0('ahe450_ring2_add2_eff', 100)
    sprite('null', 60)
    physicsYImpulse(-14000)
    physicsXImpulse(4250)
    SFX_3('ahese_52')
    sprite('null', 32767)
    Unknown1099(100)

@Subroutine
def ahe450_ring():
    Unknown2008()
    Unknown1096(13000)
    Unknown1056(-13000)
    Unknown1072(22500)
    Unknown1074(750)

@Subroutine
def ahe450_ring2():
    Unknown2008()
    Unknown1096(15500)
    Unknown1056(-15500)
    Unknown1072(135000)
    Unknown1074(-1500)

@Subroutine
def ahe450_ring_color():
    Unknown3001(159)
    Unknown3007(223)
    Unknown3019(175)
    Unknown3013(63)

@Subroutine
def ahe450_ring_bg_color():
    Unknown3001(191)
    Unknown3007(255)
    Unknown3019(127)
    Unknown3013(0)

@State
def ahe450_sphere_eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 30)
    Unknown23015(13)
    Unknown4003('61686565665f61737472616c686561745f62616c6c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown1096(0)
    Unknown1099(500)
    sprite('null', 40)
    Unknown1099(75)
    sprite('null', 35)
    Unknown1096(18000)
    Unknown1099(0)
    sprite('null', 200)
    GFX_0('ahe450_flash_eff', 100)
    sprite('null', 100)
    Unknown3001(0)

@State
def ahe450_ring_add2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(12)
        callSubroutine('ahe450_ring')
        Unknown3001(63)
        Unknown3033()
    sprite('null', 32767)

@State
def ahe450_ring_add_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(12)
        callSubroutine('ahe450_ring')
        Unknown3001(191)
        Unknown3033()
    sprite('null', 32767)

@State
def ahe450_ring_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(12)
        callSubroutine('ahe450_ring')
        callSubroutine('ahe450_ring_color')
        Unknown3032()
    sprite('null', 32767)

@State
def ahe450_ring_bg_add_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(14)
        callSubroutine('ahe450_ring')
        Unknown3033()
        Unknown3001(63)
    sprite('null', 32767)

@State
def ahe450_ring_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(14)
        callSubroutine('ahe450_ring')
        callSubroutine('ahe450_ring_bg_color')
        Unknown3032()
    sprite('null', 32767)

@State
def ahe450_ring2_add2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30352e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
        callSubroutine('ahe450_ring2')
        Unknown3001(63)
        Unknown3033()
    sprite('null', 32767)

@State
def ahe450_ring2_add_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
        callSubroutine('ahe450_ring2')
        Unknown3001(191)
        Unknown3033()
    sprite('null', 32767)

@State
def ahe450_ring2_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30352e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(11)
        callSubroutine('ahe450_ring2')
        callSubroutine('ahe450_ring_color')
        Unknown3032()
    sprite('null', 32767)

@State
def ahe450_ring2_bg_add_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        callSubroutine('ahe450_ring2')
        Unknown3033()
        Unknown3001(63)
    sprite('null', 32767)

@State
def ahe450_ring2_bg_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4003('61686565665f61737472616c686561745f30362e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        callSubroutine('ahe450_ring2')
        callSubroutine('ahe450_ring_bg_color')
        Unknown3032()
    sprite('null', 32767)

@State
def ahe450_particle_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    label(0)
    sprite('null', 1)
    Unknown4049(2000)
    Unknown4054(13)
    Unknown4045('61686565663435305f7370686572655f7074000000000000000000000000000064000000')
    gotoLabel(0)

@State
def ahe450_flash_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4054(10)
        Unknown23067('aheef450_sphereflash')
    sprite('null', 90)
    Unknown1096(0)
    sprite('null', 90)
    Unknown1096(750)
    Unknown1099(750)
    sprite('null', 85)
    Unknown1099(0)
    sprite('null', 10)
    Unknown3004(-25)

@State
def AstralHeatCutInObject():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(400000)
        teleportRelativeY(-670000)
        if SLOT_38:
            Unknown1000(-880000)
        Unknown3038(1)
        Unknown2035(1)
    sprite('null', 1)
    GFX_0('AstralHeatCutInImage', -1)
    Unknown38(5, 1)
    sprite('null', 10)
    physicsXImpulse(10000)
    Unknown23029(5, 4511, 0)
    sprite('null', 40)
    physicsXImpulse(0)
    physicsXImpulse(500)
    sprite('null', 10)
    Unknown23029(5, 4512, 0)
    physicsXImpulse(5000)
    physicsYImpulse(-1500)
    Unknown1099(20)

@State
def AstralHeatCutInImage():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown2054(1)
        Unknown23015(5)
        Unknown6001(1)
        Unknown3001(0)
        Unknown2035(1)

        def upon_43():
            if (SLOT_48 == 4511):
                Unknown3004(25)
            if (SLOT_48 == 4512):
                Unknown3004(-25)
    label(0)
    sprite('vr_ahe450_cutin00', 6)
    sprite('vr_ahe450_cutin01', 6)
    sprite('vr_ahe450_cutin02', 6)
    sprite('vr_ahe450_cutin03', 6)
    loopRest()
    gotoLabel(0)

@State
def AstralHeatCutInLoveArcana():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown2054(1)
        Unknown23015(5)

        def upon_3():
            Unknown23057(50)
            Unknown23058(100)
        Unknown2035(1)

        def upon_43():
            if (SLOT_48 == 4513):
                sendToLabel(1)
    sprite('vr_ahe450_cutin04', 10)
    Unknown3001(0)
    Unknown3004(25)
    sprite('vr_ahe450_cutin04', 120)
    label(1)
    sprite('vr_ahe450_cutin04', 10)
    Unknown3001(255)
    Unknown3004(-25)

@State
def AstralFinishAttackObject():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(37000)
        Unknown11091(100)
        Unknown11064(3)
        AirPushbackX(60000)
        Unknown11084(1)
        Unknown9021(1)
        Unknown11067(1)
        Unknown11023(1)
        Unknown1096(5000)
        Unknown23027()
        Unknown2035(1)

        def upon_12():
            Unknown23029(3, 4506, 0)
        Unknown2006()
    sprite('null', 260)
    GFX_0('ahe450_attack_eff', 100)
    sprite('vr_ahe_magicol', 30)
    Unknown1086(22)
    Unknown1007(30000)
    RefreshMultihit()

@State
def AstralHeatPal():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown2018(0, 30)
        Unknown1096(2100)
        teleportRelativeX(200000)
        Unknown1007(-250000)
        Unknown23015(5)
    sprite('ahe450_36', 20)
    Unknown3001(0)
    SFX_3('ahese_53')
    sprite('keep', 100)
    Unknown3001(255)
    Unknown3026(-6299713)
    GFX_0('ahe450_pal_flash', 100)
    sprite('keep', 30)
    Unknown3004(-17)
    GFX_0('ahe450_pal_flash', 100)

@State
def ahe450_pal_flash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4013(2)
        Unknown4061(1)
        Unknown3000(0)
        Unknown3033()
        Unknown23015(15)
    sprite('vr_ahe450_pal', 30)
    Unknown3004(-8)

@State
def AstralCameraObject():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown2017(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown20003(1)
        Unknown20002(1)
        Unknown20008(1)

        def upon_STATE_END():
            Unknown20003(0)
            Unknown20002(0)
            Unknown20008(0)
        Unknown1096(1000)
        Unknown2003(1)
        Unknown2035(1)

        def upon_43():
            if (SLOT_48 == 4501):
                sendToLabel(200)
            if (SLOT_48 == 4502):
                sendToLabel(300)
            if (SLOT_48 == 4503):
                sendToLabel(400)
            if (SLOT_48 == 4505):
                sendToLabel(500)
            if (SLOT_48 == 4504):
                sendToLabel(600)
    sprite('null', 32767)

    def upon_16():
        Unknown2071('1600000000000000a08601006400000000000000')
    Unknown20000(1)
    label(200)
    sprite('null', 32767)

    def upon_16():
        Unknown1086(3)
        SLOT_51 = SLOT_163
        op(3, 2, 51, 0, 2)
        if SLOT_38:
            op(2, 2, 0, 0, -1)
        SLOT_83 = (SLOT_83 + SLOT_0)
        Unknown1007(60000)
    Unknown20000(1)
    label(300)
    sprite('null', 32767)

    def upon_16():
        Unknown2071('0300000000000000400d03001900000000000000')
    Unknown20000(1)
    label(400)
    sprite('null', 32767)

    def upon_16():
        Unknown2071('03000000206cfbffa08601001900000000000000')
    Unknown20005(240, 50)
    label(500)
    sprite('null', 6)

    def upon_16():
        Unknown2071('0300000000000000000000006400000000000000')
    Unknown20000(1)
    Unknown20001(1)
    sprite('null', 32767)
    Unknown20001(0)
    Unknown20008(0)
    label(600)
    sprite('null', 1)

@State
def aheef601_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 0)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 1)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 2)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 3)
    GFX_1('aheef601_dust', 16)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 4)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 5)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 6)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 7)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 8)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 9)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 10)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 11)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 12)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 13)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 14)
    sprite('ahe601_eff', 1)
    GFX_1('aheef601_heart', 15)

@State
def aheef611_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 0)
    GFX_1('aheef601_dust', 15)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 1)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 2)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 3)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 4)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 5)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 6)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 7)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 8)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 9)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 10)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 11)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 12)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 13)
    sprite('ahe611_eff', 2)
    GFX_1('aheef601_heart', 14)

@State
def ahe_test_blend_eff():

    def upon_IMMEDIATE():
        Unknown4003('61686565665f746573745f626c656e64000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2007()
        Unknown3032()
        Unknown23032(50)
        Unknown23033(50)
        Unknown1096(1000)
    sprite('null', 100)

@State
def ahe_test_eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown2055(100)
    sprite('vr_ahe_magicol', 20)
    Unknown4003('61686565665f69726f6e666973742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_2('aheef_test')
    GFX_1('aheef_test', 100)
    Unknown4007(0)
    teleportRelativeX(-180000)
    Unknown1007(185000)
    Unknown1096(1000)
    Unknown1097(500)
    Unknown1072(45000)
    Unknown1073(-30000)
    Unknown1074(0)
    Unknown3032()
    Unknown3001(255)
    Unknown3002(-128)
    Unknown3004(-1)
    Unknown3007(128)
    Unknown3013(128)
    Unknown3019(128)
    Unknown3008(64)
    Unknown3014(64)
    Unknown3020(64)
    Unknown23015(0)
    Unknown23015(10)
    Unknown23015(15)
    label(1)
    sprite('keep', 20)
    sprite('keep', 20)
    sprite('keep', 1)
    gotoLabel(1)
    label(0)
    sprite('null', 1)

@State
def XhitEff_Arcana():

    def upon_IMMEDIATE():
        Unknown2006()
        Unknown1086(22)
        teleportRelativeY(200000)
    sprite('null', 22)
    GFX_1('ef_hitx_ah', 0)