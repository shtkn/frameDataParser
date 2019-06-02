@State
def esef_001():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(4)
    sprite('null', 56)	# 1-56
    Unknown4047(240, 240, 240)
    Unknown23067('eseff_001tame_bloom')
    sprite('null', 20)	# 57-76
    Unknown3004(-32)
    Unknown26('esef_001_tame_add')

@State
def esef_001_tame_add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(4)
    sprite('null', 5)	# 1-5
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f30303174616d655f616464000000000000000000000000000000ffffffff')
    label(1)
    sprite('null', 5)	# 6-10
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f30303174616d655f616464320000000000000000000000000000ffffffff')
    gotoLabel(1)

@State
def EMB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3033()
        Unknown1096(1500)
        Unknown1007(273000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f65732e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
    sprite('null', 8)	# 1-8
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)	# 9-16
    Unknown3025(-8342273, 10)
    sprite('null', 8)	# 17-24
    Unknown3025(-16744193, 10)
    sprite('null', 8)	# 25-32
    Unknown3025(-16744193, 10)
    sprite('null', 80)	# 33-112

@State
def esef_333Eff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(4)
        Unknown21004(240)
        Unknown4007(3)
        Unknown4010(3)
        Unknown3038(1)
        Unknown4003('657365665f3333335f62727573743030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown23067('eseff_333_tobitiri')
        Unknown1096(600)
        Unknown1073(-29000)
        Unknown1007(200000)
        teleportRelativeX(-200000)
        Unknown2054(1)
    sprite('null', 3)	# 1-3
    Unknown3001(0)
    sprite('null', 25)	# 4-28
    Unknown3001(255)
    GFX_0('esef_333EffAdd', -1)
    sprite('null', 10)	# 29-38
    Unknown3004(-26)

@State
def esef_333EffAdd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4007(3)
        Unknown4010(3)
        Unknown3038(1)
        Unknown4003('657365665f3333335f62727573743030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(300)
        Unknown1073(-29000)
        Unknown2054(1)
    sprite('null', 20)	# 1-20
    sprite('null', 5)	# 21-25
    Unknown3004(-51)

@State
def esef_252():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(170)
        callSubroutine('Zanzou')
    sprite('vresef252_00', 16)	# 1-16

@Subroutine
def Zanzou():
    Unknown3033()
    Unknown4061(4)
    Unknown3053(1)
    Unknown3040(2)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3041(240)
    Unknown3044(1)

@State
def esef_201():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(194)
        callSubroutine('Zanzou')
    sprite('vresef201_00', 16)	# 1-16

@State
def esef_202():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(170)
        callSubroutine('Zanzou')
    sprite('vresef202_00', 4)	# 1-4
    sprite('vresef202_01', 30)	# 5-34
    Unknown4007(0)

@State
def eseff_DTame():

    def upon_IMMEDIATE():
        Unknown4061(4)
        Unknown4047(240, 240, 240)
        Unknown23067('eseff_203tame')
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 100):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 5)	# 32768-32772
    Unknown3004(-51)

@Subroutine
def Monsho_AtkData():
    AttackLevel_(1)
    AttackP1(70)
    AttackP2(90)
    Hitstop(6)
    Unknown9154(17)
    AirUntechableTime(21)
    Unknown11028(11)
    Unknown9016(1)

@State
def esef_203Add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4003('657365665f323033736c6173685f30324164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767

@State
def esef_203():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4019(2)
        Unknown3038(1)
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown1056(1250)
        Unknown1064(1200)
    sprite('vresef203_ParitclePos', 1)	# 1-1
    Unknown21010(1)
    Unknown4003('657365665f323033736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    sprite('vresef203_ParitclePos', 1)	# 2-2
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    sprite('vresef203_ParitclePos', 1)	# 3-3
    Unknown4003('657365665f323033736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    sprite('vresef203_ParitclePos', 1)	# 4-4
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    sprite('vresef203_ParitclePos', 1)	# 5-5
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    sprite('vresef203_ParitclePos', 1)	# 6-6
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    sprite('null', 10)	# 7-16
    Unknown4003('657365665f323033736c6173685f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('esef_203Add', -1)
    Unknown4009(2)
    Unknown21010(0)
    sprite('null', 12)	# 17-28
    Unknown4003('657365665f323033736c6173685f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_203Add')
    Unknown4009(0)
    Unknown4010(0)
    Unknown21010(1)
    Unknown2054(1)

@State
def es203_effAtk_Yotyou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f323033736c6173685f796f74796f7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown23015(15)
        Unknown1056(1250)
        Unknown1064(1200)
    sprite('null', 5)	# 1-5
    Unknown3001(0)
    Unknown3004(10)
    label(0)
    sprite('null', 5)	# 6-10
    sprite('null', 10)	# 11-20
    Unknown3004(-13)
    sprite('null', 10)	# 21-30
    Unknown3004(13)
    gotoLabel(0)

@State
def esef_203Monsho():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f323033736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1007(40000)
        teleportRelativeX(45000)
        Unknown1072(7500)
    sprite('null', 5)	# 1-5
    GFX_0('esef_203MonshoAdd', 100)
    ScreenShake(5000, 5000)
    Unknown21010(1)
    sprite('null', 10)	# 6-15
    Unknown21010(0)
    Unknown4009(2)
    sprite('vresef203_ParitclePos', 10)	# 16-25
    Unknown26('esef_203MonshoAdd')
    Unknown4003('657365665f323033736c61736841646441746b5f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3004(-25)
    Unknown4009(0)
    Unknown4010(0)
    Unknown2054(1)

@State
def esef_203MonshoAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4003('657365665f323033736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767

@State
def es203_effAtk():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        PushbackX(20000)
        Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 110):
                Unknown13(25)
            if (SLOT_48 == 129):
                Unknown13(25)
            if (SLOT_48 == 103):
                sendToLabel(0)
    sprite('null', 15)	# 1-15
    sprite('null', 5)	# 16-20
    GFX_0('es203_effAtk_Yotyou', -1)
    clearUponHandler(43)
    Unknown38(11, 1)
    label(0)
    clearUponHandler(43)
    sprite('null', 4)	# 21-24
    Unknown13(11)
    GFX_0('esef_203Monsho', 100)
    SFX_3('esse_01')
    sprite('es203_effatk', 3)	# 25-27	 **attackbox here**
    sprite('null', 50)	# 28-77

@State
def esef_405Eff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(2)
        Unknown4007(2)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f343035736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(4600)
        Unknown1088(500)
        Unknown1007(200000)
    sprite('null', 5)	# 1-5
    GFX_0('esef_405EffAdd', -1)
    sprite('null', 10)	# 6-15
    Unknown4007(0)
    sprite('null', 20)	# 16-35
    GFX_0('esef_405EffSlaskParticle', -1)
    Unknown21015('657365665f3430354566664164640000000000000000000000000000000000006500000000000000')
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_405EffAdd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3038(1)
        Unknown4003('657365665f343035736c6173685f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 101):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 15)	# 32768-32782
    Unknown4003('657365665f343035736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 32783-32787
    Unknown3004(-51)
    loopRest()

@State
def esef_405EffSlaskParticle():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(4)
        Unknown1096(800)
    sprite('vresef405_ParitclePos', 1)	# 1-1
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')

@State
def esef_405EffEX():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f343035736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(4600)
        Unknown1088(500)
        Unknown1007(200000)
    sprite('null', 5)	# 1-5
    GFX_0('esef_405EffAdd', -1)
    sprite('null', 5)	# 6-10
    Unknown4007(0)
    GFX_0('esef_405EffAddAtk', -1)
    GFX_0('es405_effAtk', -1)
    ScreenShake(5000, 5000)
    SFX_3('esse_01')
    sprite('null', 10)	# 11-20
    Unknown26('esef_405EffAdd')
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_405EffAdd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3038(1)
        Unknown4003('657365665f343035736c6173685f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 15)	# 32768-32782
    Unknown4003('657365665f343035736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 32783-32787
    Unknown3004(-51)
    loopRest()

@State
def esef_405EffAddAtk():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('657365665f343035736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown1096(3400)
        Unknown1088(500)
        Unknown3038(1)
        Unknown23015(12)
        teleportRelativeX(50000)
    sprite('null', 25)	# 1-25
    GFX_0('esef_405EffAddAtkadd', -1)
    ScreenShake(10000, 10000)
    Unknown4010(0)
    Unknown21010(1)
    sprite('null', 10)	# 26-35
    Unknown21015('657365665f34303545666641646441746b6164640000000000000000000000006500000000000000')
    Unknown21010(0)
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_405EffAddAtkadd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown4003('657365665f343035736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4013(2)
        Unknown3033()
        Unknown3038(1)
        Unknown23015(12)

        def upon_43():
            if (SLOT_48 == 101):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown4010(0)
    Unknown21010(1)
    label(0)
    sprite('null', 10)	# 32768-32777
    GFX_0('esef_405EffAddAtkParticle', -1)
    Unknown21010(0)
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_405EffAddAtkParticle():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(4)
    sprite('vresef405_ParitclePos', 1)	# 1-1
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000009000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000b000000')

@State
def es405_effAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Monsho_AtkData')
        Unknown9310(1)
        AirPushbackX(30000)
        AirPushbackY(-10000)
        teleportRelativeX(70000)
        Unknown4011(3)
        Unknown4007(2)
    sprite('null', 12)	# 1-12
    sprite('es405_effatk', 6)	# 13-18	 **attackbox here**
    sprite('null', 10)	# 19-28

@State
def esef_ThrowEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f3331315f6d6330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown23015(15)
        Unknown1086(22)

        def upon_43():
            if (SLOT_48 == 117):
                sendToLabel(0)
    sprite('null', 5)	# 1-5
    Unknown1096(50)
    Unknown1099(95)
    sprite('null', 32767)	# 6-32772
    Unknown1099(1)
    label(0)
    sprite('null', 25)	# 32773-32797
    Unknown4010(0)
    GFX_0('esef_ThrowEffAtk', -1)
    sprite('null', 5)	# 32798-32802
    Unknown3004(-51)
    Unknown1099(30)

@State
def esef_ThrowEffAtk():

    def upon_IMMEDIATE():
        Unknown4003('657365665f3331315f6d6330312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1086(22)
        Unknown1096(500)
        Unknown1065(200)
        Unknown2054(1)
    sprite('null', 20)	# 1-20
    GFX_0('esef_ThrowEffImpact', -1)
    GFX_0('esef_ThrowEffAtkAdd', -1)
    sprite('vresef311_ParticlePos', 10)	# 21-30
    Unknown3004(-26)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')

@State
def esef_ThrowEffAtkAdd():

    def upon_IMMEDIATE():
        Unknown4003('657365665f3331315f6d6330316164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown3038(1)
        Unknown1086(22)
        Unknown1096(500)
        Unknown1065(200)
        Unknown2054(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown3004(-26)

@State
def esef_ThrowEffImpact():

    def upon_IMMEDIATE():
        Unknown21010(2)
        Unknown2054(1)
        Unknown4003('657365665f636d6e626967696d7061637430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown1096(250)
        Unknown1007(10000)
    sprite('null', 5)	# 1-5
    Unknown1096(300)
    Unknown1099(95)
    sprite('null', 5)	# 6-10
    Unknown1099(10)
    Unknown21010(0)
    sprite('null', 5)	# 11-15
    Unknown3004(-51)

@State
def esef_BackThrowEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f3331315f6d6330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown23015(15)
        Unknown1086(22)
        Unknown1007(200000)
        Unknown1072(-65000)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 118):
                sendToLabel(0)
    sprite('null', 5)	# 1-5
    Unknown1056(200)
    Unknown1064(800)
    Unknown1099(95)
    sprite('null', 32767)	# 6-32772
    Unknown1099(1)
    label(0)
    sprite('null', 25)	# 32773-32797
    Unknown3001(150)
    Unknown4010(0)
    GFX_0('esef_BackThrowEffAtk', -1)
    GFX_0('esef_BackThrowEffAtkAdd', -1)
    GFX_0('esef_BackThrowEffAtkSub', -1)
    GFX_0('esef_BackThrowEffAtk2', -1)
    sprite('null', 5)	# 32798-32802
    Unknown3004(-51)
    Unknown1099(30)

@State
def esef_BackThrowEffAtk():

    def upon_IMMEDIATE():
        Unknown4003('657365665f3331335f6d6330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1096(1000)
        teleportRelativeX(-100000)
        Unknown1057(400)
        Unknown2054(1)
    sprite('null', 20)	# 1-20
    ScreenShake(10000, 10000)
    sprite('vresef313_ParticlePos', 10)	# 21-30
    Unknown3004(-26)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000009000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000b000000')

@State
def esef_BackThrowEffAtkAdd():

    def upon_IMMEDIATE():
        Unknown4003('657365665f3331335f6d6330306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown3038(1)
        Unknown1096(1000)
        Unknown1057(400)
        teleportRelativeX(-100000)
        Unknown2054(1)
    sprite('null', 19)	# 1-19
    sprite('null', 10)	# 20-29
    Unknown3004(-26)

@State
def esef_BackThrowEffAtkSub():

    def upon_IMMEDIATE():
        Unknown4003('657365665f3331335f6d6330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3035()
        Unknown3038(1)
        Unknown1096(1000)
        Unknown1057(400)
        teleportRelativeX(-100000)
        Unknown2054(1)
        Unknown23015(15)
        Unknown3001(100)
    sprite('null', 19)	# 1-19
    sprite('null', 10)	# 20-29
    Unknown3004(-26)

@State
def esef_BackThrowEffAtk2():

    def upon_IMMEDIATE():
        Unknown4003('657365665f3331335f6d6330306261636b2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1096(1000)
        Unknown1057(400)
        Unknown23015(15)
        Unknown2054(1)
    sprite('null', 20)	# 1-20
    Unknown3001(100)
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def esef_402_zanzou():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(2)
        callSubroutine('Zanzou')
    sprite('vresef402_00', 3)	# 1-3
    sprite('vresef402_01', 2)	# 4-5
    Unknown3004(-16)

@State
def esef_402Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4011(2)
        Unknown4003('657365665f343032736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        teleportRelativeX(100000)
        Unknown1064(700)
        Unknown1056(1000)
        Unknown3038(1)
    sprite('es402_effatk1', 24)	# 1-24	 **attackbox here**
    GFX_0('esef_402EffAdd', -1)
    GFX_0('esef_402EffKidou', -1)
    GFX_0('esef_402EffParticle', -1)
    sprite('null', 2)	# 25-26
    Unknown4003('657365665f343032736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21015('657365665f3430324566664164640000000000000000000000000000000000006400000000000000')
    Unknown21015('657365665f3430324566664b69646f75000000000000000000000000000000006400000000000000')
    Unknown4010(0)
    Unknown3004(-8)
    sprite('null', 2)	# 27-28
    Unknown4003('657365665f343032736c6173685f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 29-30
    Unknown4003('657365665f343032736c6173685f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 31-32
    Unknown4003('657365665f343032736c6173685f30342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 33-33
    Unknown4003('657365665f343032736c6173685f30352e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 34-34
    Unknown4003('657365665f343032736c6173685f30362e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 35-35
    Unknown4003('657365665f343032736c6173685f30372e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 36-36
    Unknown4003('657365665f343032736c6173685f30382e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 37-37
    Unknown4003('657365665f343032736c6173685f30392e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 38-38
    Unknown4003('657365665f343032736c6173685f31302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 39-39
    Unknown4003('657365665f343032736c6173685f31312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 40-40
    Unknown4003('657365665f343032736c6173685f31322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 41-41
    Unknown4003('657365665f343032736c6173685f31332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def es402_effAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Monsho_AtkData')
        AirUntechableTime(40)
        AirHitstunAnimation(10)
        AirPushbackY(18000)
        PushbackX(19800)
        Unknown4011(3)
        teleportRelativeX(150000)
        Unknown1007(400000)
    sprite('null', 21)	# 1-21
    sprite('null', 5)	# 22-26
    GFX_0('esef_402EffAddAtk', -1)
    GFX_0('esef_402EffAddAtkadd', -1)
    ScreenShake(5000, 5000)
    SFX_3('esse_01')
    sprite('es402_effatk', 6)	# 27-32	 **attackbox here**
    sprite('null', 10)	# 33-42

@State
def es403_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP1(48)
        AttackP2(100)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(1000)
        AirPushbackY(-50000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(50)
        AirHitstunAfterWallbounce(60)
        Unknown9016(1)
        Unknown2053(1)
        teleportRelativeX(200000)
        Unknown1007(150000)
        Unknown4011(3)
        Unknown30065(100)
        Unknown11044(1)
    sprite('null', 5)	# 1-5
    GFX_0('esef_402Eff2C', -1)
    Unknown36(1)
    teleportRelativeX(10000)
    Unknown35()
    sprite('es403_effatk', 8)	# 6-13	 **attackbox here**
    sprite('null', 60)	# 14-73
    Unknown23029(3, 139, 0)

@State
def esef_402Eff2C():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f3430325f32436566662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(300000)
        Unknown1057(300)
    sprite('null', 15)	# 1-15
    Unknown21010(1)
    GFX_0('esef_402Eff2CAdd', 100)
    sprite('vresef402_2CParitclePos', 2)	# 16-17
    Unknown21010(0)
    Unknown4010(0)
    Unknown4007(0)
    Unknown3004(-13)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    sprite('vresef402_2CParitclePos', 2)	# 18-19
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    sprite('vresef402_2CParitclePos', 2)	# 20-21
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    sprite('vresef402_2CParitclePos', 2)	# 22-23
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    sprite('vresef402_2CParitclePos', 2)	# 24-25
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    sprite('vresef402_2CParitclePos', 10)	# 26-35

@State
def esef_402Eff2CAdd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
        Unknown4003('657365665f3430325f32436566666164642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1057(300)
    sprite('null', 15)	# 1-15
    Unknown21010(1)
    sprite('null', 19)	# 16-34
    Unknown21010(0)
    Unknown4010(0)
    Unknown4007(0)
    Unknown3004(-13)

@State
def esef_402EffAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4013(2)
        Unknown4003('657365665f343032736c6173685f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown3038(1)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 100):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    label(1)
    sprite('null', 10)	# 32768-32777
    Unknown4010(0)
    Unknown3004(-25)
    loopRest()

@State
def esef_402EffAddAtk():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f343032736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        teleportRelativeX(100000)
        Unknown1064(700)
        Unknown1056(1000)
        Unknown3038(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_402EffAddAtkadd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f343032736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        teleportRelativeX(100000)
        Unknown1064(700)
        Unknown1056(1000)
        Unknown3038(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_402EffKidou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4013(2)
        Unknown4003('657365665f3430326b69646f7530312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 100):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    label(1)
    sprite('null', 15)	# 32768-32782
    Unknown4010(0)
    Unknown3004(-17)
    loopRest()

@State
def esef_402EffParticle():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(4)
        teleportRelativeX(100000)
    sprite('vresef402_ParitclePos', 1)	# 1-1
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    sprite('vresef402_ParitclePos', 1)	# 2-2
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    sprite('vresef402_ParitclePos', 1)	# 3-3
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    sprite('vresef402_ParitclePos', 1)	# 4-4
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    sprite('vresef402_ParitclePos', 1)	# 5-5
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    sprite('vresef402_ParitclePos', 1)	# 6-6
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    sprite('vresef402_ParitclePos', 1)	# 7-7
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    sprite('vresef402_ParitclePos', 1)	# 8-8
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    sprite('vresef402_ParitclePos', 1)	# 9-9
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
    sprite('vresef402_ParitclePos', 1)	# 10-10
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000009000000')
    sprite('vresef402_ParitclePos', 1)	# 11-11
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')
    sprite('vresef402_ParitclePos', 1)	# 12-12
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000b000000')

@State
def esef_231():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(194)
        callSubroutine('Zanzou')
    sprite('vresef231_00', 16)	# 1-16

@State
def esef_212():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 1)	# 1-1
    GFX_2('esef_212')
    GFX_1('esef_212add', -1)
    sprite('null', 30)	# 2-31
    Unknown4009(0)
    GFX_1('esef_212add', -1)

@State
def esef_211():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(194)
        callSubroutine('Zanzou')
    sprite('vresef211_00', 16)	# 1-16

@State
def esef_213():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f323133736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown1096(950)
        teleportRelativeY(12000)
    sprite('vresef213_ParitclePos', 15)	# 1-15
    GFX_0('esef_213Add', -1)
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    sprite('null', 15)	# 16-30
    Unknown4003('657365665f323133736c617368456e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_213Add')
    Unknown4010(0)
    Unknown21010(1)
    Unknown2054(1)

@State
def es213_effAtk():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(35000)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown11042(1)
        Unknown11031(5)
        Unknown11091(5)
        Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 103):
                sendToLabel(0)
            if (SLOT_48 == 110):
                Unknown13(25)
    sprite('null', 5)	# 1-5
    sprite('null', 7)	# 6-12
    GFX_0('es213_effAtk_Yotyou', -1)
    Unknown38(11, 1)
    label(0)
    sprite('null', 3)	# 13-15
    clearUponHandler(43)
    Unknown13(11)
    GFX_0('esef_213Monsho', -1)
    SFX_3('esse_01')
    sprite('es213_effatk', 3)	# 16-18	 **attackbox here**
    sprite('null', 50)	# 19-68

@State
def esef_213Add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4003('657365665f323133736c6173685f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767

@State
def esef_213():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f323133736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown1096(950)
        teleportRelativeY(12000)
    sprite('vresef213_ParitclePos', 15)	# 1-15
    GFX_0('esef_213Add', -1)
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    sprite('null', 15)	# 16-30
    Unknown4003('657365665f323133736c617368456e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_213Add')
    Unknown4010(0)
    Unknown21010(1)
    Unknown2054(1)

@State
def es213_effAtk_Yotyou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f323133736c6173685f796f74796f7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown23015(15)
        Unknown1096(850)
    sprite('null', 5)	# 1-5
    Unknown3001(0)
    Unknown3004(10)
    label(0)
    sprite('null', 5)	# 6-10
    sprite('null', 10)	# 11-20
    Unknown3004(-13)
    sprite('null', 10)	# 21-30
    Unknown3004(13)
    gotoLabel(0)

@State
def esef_213Monsho():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f323133736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1096(950)
        teleportRelativeY(12000)
    sprite('null', 5)	# 1-5
    ScreenShake(5000, 5000)
    GFX_0('esef_213MonshoAdd', 100)
    Unknown21010(1)
    sprite('null', 10)	# 6-15
    Unknown4009(2)
    Unknown21010(0)
    sprite('vresef213_ParitclePos', 10)	# 16-25
    Unknown4003('657365665f323133736c61736841646441746b5f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_213MonshoAdd')
    Unknown3004(-25)
    Unknown4009(0)
    Unknown4010(0)
    Unknown2054(1)

@State
def esef_213MonshoAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4003('657365665f323133736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767

@State
def esef_232():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4009(3)
        Unknown3001(170)
        callSubroutine('Zanzou')
    sprite('vresef232_00', 3)	# 1-3
    sprite('vresef232_01', 3)	# 4-6
    Unknown4007(0)

@State
def esef_235():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown23015(11)
        callSubroutine('Zanzou')
    sprite('vresef235_00', 3)	# 1-3
    sprite('vresef235_01', 3)	# 4-6
    sprite('vresef235_02', 3)	# 7-9
    sprite('vresef235_03', 3)	# 10-12
    sprite('vresef235_04', 16)	# 13-28
    Unknown4007(0)
    Unknown3004(-25)
    Unknown1007(5000)

@State
def esef_251():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(194)
        callSubroutine('Zanzou')
    sprite('vresef251_00', 3)	# 1-3
    sprite('vresef251_00', 14)	# 4-17
    Unknown4007(0)

@State
def esef_251_2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3001(194)
        callSubroutine('Zanzou')
    sprite('vresef251_10', 3)	# 1-3
    sprite('vresef251_10', 14)	# 4-17
    Unknown4007(0)

@State
def esef_253_wari():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f323533736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown23015(1)
        Unknown1007(250000)
        Unknown1096(750)
    sprite('null', 32767)	# 1-32767

@State
def esef_253_wari2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f323533736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown23015(1)
        Unknown1007(250000)
        Unknown1096(750)
    sprite('null', 32767)	# 1-32767

@State
def esef_253Add():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4003('657365665f323533736c6173685f30326164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767

@State
def esef_253():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f323533736c6173685f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown23015(15)
        Unknown1007(250000)
        Unknown1096(750)
    sprite('vresef253_ParitclePos', 10)	# 1-10
    Unknown2054(1)
    GFX_0('esef_253Add', -1)
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000009000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')
    Unknown4047(240, 240, 240)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000b000000')
    sprite('null', 15)	# 11-25
    Unknown4003('657365665f323533736c6173685f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_253Add')
    Unknown4010(0)
    Unknown21010(1)

@State
def es253_effAtk_Yotyou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f323533736c6173685f796f74796f7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown23015(15)
        Unknown1096(1200)
        Unknown1007(250000)
    sprite('null', 5)	# 1-5
    Unknown3001(0)
    Unknown3004(10)
    label(0)
    sprite('null', 5)	# 6-10
    sprite('null', 10)	# 11-20
    Unknown3004(-13)
    sprite('null', 10)	# 21-30
    Unknown3004(13)
    gotoLabel(0)

@State
def esef_253Monsho():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f323533736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1007(250000)
        Unknown1096(1100)
    sprite('null', 5)	# 1-5
    Unknown21010(1)
    ScreenShake(5000, 5000)
    GFX_0('esef_253MonshoAdd', 100)
    sprite('null', 10)	# 6-15
    Unknown21010(0)
    Unknown4009(2)
    sprite('vresef213_ParitclePos', 10)	# 16-25
    Unknown26('esef_253MonshoAdd')
    Unknown3004(-25)
    Unknown4009(0)
    Unknown4010(0)
    Unknown2054(1)

@State
def esef_253MonshoAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4003('657365665f323533736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767

@State
def es253_effAtk():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        Unknown11056(1)
        Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 103):
                sendToLabel(0)
            if (SLOT_48 == 110):
                Unknown13(25)
    sprite('null', 15)	# 1-15
    sprite('null', 5)	# 16-20
    GFX_0('es253_effAtk_Yotyou', -1)
    Unknown38(11, 1)
    label(0)
    sprite('null', 3)	# 21-23
    clearUponHandler(43)
    Unknown13(11)
    GFX_0('esef_253Monsho', -1)
    SFX_3('esse_01')
    sprite('es253_effatk', 3)	# 24-26	 **attackbox here**
    sprite('null', 50)	# 27-76

@Subroutine
def es400_Init():
    Unknown2010()
    AttackLevel_(2)
    Damage(1500)
    AttackP1(80)
    AttackP2(80)
    AirPushbackX(12000)
    AirPushbackY(12000)
    AirUntechableTime(22)
    Unknown9154(17)
    Hitstop(8)
    PushbackX(8000)
    Unknown9016(1)
    Unknown4011(3)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

    def upon_54():
        clearUponHandler(43)
        Unknown13(25)
        Unknown23029(4, 124, 0)
    callSubroutine('es400_Delete')

@Subroutine
def es400_Delete():

    def upon_3():
        if SLOT_38:
            Unknown23045('7d000000')
            if (SLOT_22 < SLOT_0):
                clearUponHandler(2)
                clearUponHandler(54)
                clearUponHandler(3)
                Unknown13(25)
                Unknown13(4)
        else:
            Unknown23045('7d000000')
            if (SLOT_22 > SLOT_0):
                clearUponHandler(2)
                clearUponHandler(54)
                clearUponHandler(3)
                Unknown13(25)
                Unknown13(4)

@State
def es400_A():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown1007(128000)
        teleportRelativeX(100000)
    sprite('es400eff_atk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff_MatomeA', -1)
    Unknown38(4, 1)
    physicsXImpulse(45000)
    Unknown1028(-1300)
    SFX_3('esse_03')
    sprite('es400eff_atk2', 27)	# 4-30	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')
    sprite('null', 1)	# 31-31
    Unknown23029(4, 125, 0)

@State
def es400_B():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown1007(128000)
        teleportRelativeX(100000)

        def upon_43():
            if (SLOT_48 == 126):
                Unknown2003(1)
    sprite('null', 3)	# 1-3
    GFX_0('esef_400eff_MatomeB', -1)
    Unknown38(4, 1)
    physicsXImpulse(2500)
    SFX_3('esse_03')
    sprite('es400eff_atk1', 22)	# 4-25	 **attackbox here**
    clearUponHandler(43)
    sprite('es400eff_atk2', 100)	# 26-125	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')
    physicsXImpulse(70000)

@State
def es400_ASS():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown1007(128000)
        teleportRelativeX(100000)
        AttackP1(70)
        Unknown11042(1)
    sprite('es400eff_atk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff_MatomeA', -1)
    Unknown38(4, 1)
    physicsXImpulse(45000)
    Unknown1028(-1300)
    SFX_3('esse_03')
    sprite('es400eff_atk2', 27)	# 4-30	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')
    sprite('null', 1)	# 31-31
    Unknown23029(4, 125, 0)

@State
def es400_A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)
    sprite('es400eff_atk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeA', -1)
    Unknown38(4, 1)
    physicsXImpulse(45000)
    Unknown1028(-1300)
    sprite('es400eff_atk2', 27)	# 4-30	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')
    sprite('null', 1)	# 31-31
    Unknown23029(4, 125, 0)

@State
def es400_A_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)
    sprite('es400eff_atk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeA', -1)
    Unknown38(4, 1)
    physicsXImpulse(45000)
    Unknown1028(-1300)
    sprite('es400eff_atk2', 27)	# 4-30	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')
    sprite('null', 1)	# 31-31
    Unknown23029(4, 125, 0)

@State
def es400_B_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)

        def upon_43():
            if (SLOT_48 == 119):
                GFX_0('es400_B_2ndEX', -1)
                Unknown26('es400_A')
                Unknown26('esef_400eff_MatomeA')
                Unknown13(25)
                Unknown26('esef_400eff2nd_MatomeB')
                Unknown26('esef_400eff2nd_MatomeB2')
    Unknown48('190000000200000033000000030000000200000033000000')
    if SLOT_51:
        _gotolabel(10)
    sprite('es400eff_atk1', 25)	# 1-25	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB', -1)
    Unknown38(4, 1)
    physicsXImpulse(2500)
    sprite('es400eff_atk2', 100)	# 26-125	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')
    physicsXImpulse(65000)
    ExitState()
    label(10)
    sprite('es400eff_atk1', 3)	# 126-128	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB2', -1)
    Unknown38(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)	# 129-228	 **attackbox here**

@State
def es400_B_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)

        def upon_43():
            if (SLOT_48 == 119):
                GFX_0('es400_B_2ndEX', -1)
                Unknown26('es400_A')
                Unknown26('esef_400eff_MatomeA')
                Unknown13(25)
                Unknown26('esef_400eff2nd_MatomeB')
                Unknown26('esef_400eff2nd_MatomeB2')
    Unknown48('190000000200000033000000030000000200000033000000')
    if SLOT_51:
        _gotolabel(10)
    sprite('es400eff_atk1', 25)	# 1-25	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB', -1)
    Unknown38(4, 1)
    physicsXImpulse(2500)
    sprite('es400eff_atk2', 100)	# 26-125	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')
    physicsXImpulse(65000)
    ExitState()
    label(10)
    sprite('es400eff_atk1', 3)	# 126-128	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB2', -1)
    Unknown38(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)	# 129-228	 **attackbox here**

@State
def es400_ASS_2ndASS():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)
        AttackP1(70)
        Unknown11042(1)
    sprite('es400eff_atk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB2', -1)
    Unknown38(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)	# 4-103	 **attackbox here**

@State
def es400_A_2ndEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Unknown11033(2)
        Damage(2500)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(36000)
        AirPushbackY(12000)
        AirUntechableTime(38)
        Unknown9202(1)
        Hitstop(11)
        Unknown9215()
        Unknown9016(1)
        Unknown1007(128000)
        teleportRelativeX(50000)
        Unknown4011(3)
        Unknown23089('0100000000000000000000000100000001000000000000000000000000000000')

        def upon_54():
            Unknown23027()
            Unknown13(25)
            Unknown23029(4, 124, 0)
        callSubroutine('es400_Delete')

        def upon_ON_HIT_OR_BLOCK():
            Unknown23027()
        Unknown26('es400_B')
        Unknown26('esef_400eff_MatomeB')
    sprite('es400eff_largeatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff_EX', -1)
    Unknown38(4, 1)
    physicsXImpulse(70000)
    SFX_3('esse_03')
    sprite('es400eff_largeatk2', 100)	# 4-103	 **attackbox here**

@State
def es400_B_2ndEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Unknown11033(2)
        Damage(2500)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(36000)
        AirPushbackY(12000)
        AirUntechableTime(38)
        Unknown9202(1)
        Hitstop(11)
        Unknown9215()
        Unknown9016(1)
        teleportRelativeX(-50000)
        Unknown4011(3)
        Unknown23089('0100000000000000000000000100000001000000000000000000000000000000')

        def upon_54():
            Unknown23027()
            Unknown13(25)
            Unknown23029(4, 124, 0)
        callSubroutine('es400_Delete')

        def upon_ON_HIT_OR_BLOCK():
            Unknown23027()
    sprite('es400eff_largeatk2', 103)	# 1-103	 **attackbox here**
    GFX_0('esef_400eff_EX', -1)
    Unknown38(4, 1)
    physicsXImpulse(70000)

@State
def es400_EX_2ndEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Unknown11033(2)
        Damage(2500)
        AttackP1(80)
        AttackP2(70)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown9178(1)
        AirPushbackX(72000)
        AirPushbackY(7000)
        AirUntechableTime(60)
        WallbounceReboundTime(10)
        Unknown9202(1)
        Hitstop(11)
        Unknown11091(10)
        Unknown9215()
        Unknown9016(1)
        Unknown1007(128000)
        teleportRelativeX(50000)
        Unknown4011(3)
        Unknown23089('0100000000000000000000000100000001000000000000000000000000000000')

        def upon_54():
            Unknown23027()
            Unknown13(25)
            Unknown23029(4, 124, 0)
        callSubroutine('es400_Delete')

        def upon_ON_HIT_OR_BLOCK():
            Unknown23027()
        Unknown30065(0)
        Unknown26('es400_B')
        Unknown26('esef_400eff_MatomeB')
    sprite('es400eff_largeatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff_EX', -1)
    Unknown38(4, 1)
    physicsXImpulse(70000)
    SFX_3('esse_03')
    sprite('es400eff_largeatk2', 100)	# 4-103	 **attackbox here**

@State
def es400_EX_2ndEX_ASS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Unknown11033(2)
        Damage(2000)
        AttackP1(70)
        AttackP2(80)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown9178(1)
        AirPushbackX(72000)
        AirPushbackY(9500)
        AirUntechableTime(60)
        WallbounceReboundTime(10)
        Unknown9202(1)
        Hitstop(11)
        Unknown9215()
        Unknown9016(1)
        Unknown11042(1)
        Unknown1007(128000)
        teleportRelativeX(50000)
        Unknown4011(3)
        Unknown23089('0100000000000000000000000100000001000000000000000000000000000000')

        def upon_54():
            Unknown23027()
            Unknown13(25)
            Unknown23029(4, 124, 0)
        callSubroutine('es400_Delete')

        def upon_ON_HIT_OR_BLOCK():
            Unknown23027()
        Unknown26('es400_B')
        Unknown26('esef_400eff_MatomeB')
    sprite('es400eff_largeatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff_EX', -1)
    Unknown38(4, 1)
    physicsXImpulse(70000)
    SFX_3('esse_03')
    sprite('es400eff_largeatk2', 100)	# 4-103	 **attackbox here**

@State
def es401_A():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        teleportRelativeX(100000)
        Unknown1007(80000)
        Unknown1072(42000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown13(25)
            Unknown23029(4, 125, 0)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff_MatomeA', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')

@State
def es401_B():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        teleportRelativeX(100000)
        Unknown1007(140000)
        Unknown1072(5000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            Unknown23090(25)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff_MatomeB', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')

@State
def es401_EX():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown30065(0)
        Unknown11091(10)
        teleportRelativeX(100000)
        Unknown1007(80000)
        Unknown1072(42000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown13(25)
            Unknown23029(4, 125, 0)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff_MatomeA', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**

@State
def es401_A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        teleportRelativeX(60000)
        Unknown1007(70000)
        Unknown1072(42000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            Unknown23090(25)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff2nd_MatomeA', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')

@State
def es401_B_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        teleportRelativeX(100000)
        Unknown1007(140000)
        Unknown1072(5000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            Unknown23090(25)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff2nd_MatomeB', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')

@State
def es401_A_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        teleportRelativeX(60000)
        Unknown1007(70000)
        Unknown1072(42000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            Unknown23090(25)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff2nd_MatomeA', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')

@State
def es401_B_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        teleportRelativeX(100000)
        Unknown1007(140000)
        Unknown1072(5000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            Unknown23090(25)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff2nd_MatomeB', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')

@State
def es401_EX_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown30065(0)
        Unknown9215()
        Unknown11091(10)
        teleportRelativeX(100000)
        Unknown1007(140000)
        Unknown1072(5000)
        Unknown1110(35000, 0)
        Unknown23026(20000)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown13(25)
            Unknown23029(4, 125, 0)
    sprite('es400eff_airatk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400Aireff2nd_MatomeB', -1)
    Unknown38(4, 1)
    sprite('es400eff_airatk2', 100)	# 4-103	 **attackbox here**

@State
def esef_400Aura():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(4)
        Unknown21004(240)
        Unknown4003('657365665f636d6e65666630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown19001(25000)
        Unknown1077(-10000, 10000)
        Unknown1010(-50000, 50000)
        Unknown1011(-50000, 50000)
        Unknown1096(2500)
        Unknown1057(1000)
        Unknown2054(1)
    sprite('null', 45)	# 1-45
    Unknown3001(128)
    Unknown1099(20)
    Unknown3004(-2)

@State
def esef_400eff_MatomeA():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot', -1)
    GFX_0('shot_add', -1)
    GFX_0('esef_400_zanzo', -1)
    label(0)
    sprite('esef400_EXpoint2', 5)	# 4-8
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 9-13
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 19-23
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 12)	# 24-35
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    Unknown1099(-50)
    ExitState()
    label(2)
    sprite('keep', 6)	# 36-41
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    physicsXImpulse(4500)
    Unknown3004(-42)
    Unknown1099(-50)

@State
def esef_400eff_MatomeB():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 105)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 25)	# 1-25
    GFX_0('shot', -1)
    GFX_0('shot_add', -1)
    GFX_0('esef_400_zanzo', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 26-30
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 31-35
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 36-40
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 41-45
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('keep', 12)	# 46-57
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    Unknown1099(-50)

@State
def esef_400eff2nd_MatomeA():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot2', -1)
    GFX_0('shot2_add', -1)
    GFX_0('esef_400_zan2', -1)
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 4-8
    Unknown4061(4)
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 9-13
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 19-23
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 12)	# 24-35
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    Unknown1099(-50)
    ExitState()
    label(2)
    sprite('keep', 6)	# 36-41
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    physicsXImpulse(4500)
    Unknown3004(-42)
    Unknown1099(-50)

@State
def esef_400eff2nd_MatomeB():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
        Unknown2003(1)
        loopRelated(17, 105)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 25)	# 1-25
    GFX_0('shot2', -1)
    GFX_0('shot2_add', -1)
    GFX_0('esef_400_zan2', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 26-30
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 31-35
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 36-40
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 41-45
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('keep', 12)	# 46-57
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    Unknown1099(-50)

@State
def esef_400eff2nd_MatomeB2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot2', -1)
    GFX_0('shot2_add', -1)
    GFX_0('esef_400_zan2', -1)
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 4-8
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 9-13
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 19-23
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('keep', 12)	# 24-35
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    Unknown1099(-50)

@State
def esef_400eff_EX():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
        Unknown2003(1)
        loopRelated(17, 103)

        def upon_17():
            Unknown13(25)
    sprite('esef400_Expoint3', 3)	# 1-3
    GFX_0('largeshot', -1)
    GFX_0('largeshot_add', -1)
    GFX_0('esef_400large_zan', -1)
    label(0)
    sprite('esef400_Expoint4', 5)	# 4-8
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_Expoint4', 5)	# 9-13
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_Expoint4', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_Expoint4', 5)	# 19-23
    Unknown4047(241, 241, 241)
    Unknown4048(-90000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('keep', 12)	# 24-35
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    Unknown1099(-50)

@State
def esef_400Aireff_MatomeA():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot', -1)
    GFX_0('shot_add', -1)
    GFX_0('esef_400_zanzo', -1)
    Unknown23029(1, 121, 0)
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 4-8
    GFX_0('esef_400Aura', -1)
    Unknown36(1)
    Unknown1073(35000)
    Unknown35()
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-405000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 9-13
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-405000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-405000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 19-23
    Unknown4047(241, 241, 241)
    Unknown4048(-405000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 12)	# 24-35
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end2', -1)
    Unknown3004(-21)
    ExitState()
    label(2)
    sprite('null', 6)	# 36-41
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end2', -1)
    Unknown3004(-42)

@State
def esef_400Aireff_MatomeB():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot', -1)
    GFX_0('shot_add', -1)
    GFX_0('esef_400_zanzo', -1)
    Unknown23029(1, 122, 0)
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 4-8
    GFX_0('esef_400Aura', -1)
    Unknown36(1)
    Unknown1073(5000)
    Unknown35()
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-80000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 9-13
    Unknown4047(241, 241, 241)
    Unknown4048(-80000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-80000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 19-23
    Unknown4047(241, 241, 241)
    Unknown4048(-80000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('null', 12)	# 24-35
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    ExitState()
    label(2)
    sprite('null', 6)	# 36-41
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end2', -1)
    Unknown3004(-42)

@State
def esef_400Aireff2nd_MatomeA():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot2', -1)
    GFX_0('shot2_add', -1)
    GFX_0('esef_400_zan2', -1)
    Unknown23029(1, 121, 0)
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 5)	# 4-8
    GFX_0('esef_400Aura', -1)
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-45000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 9-13
    Unknown4047(241, 241, 241)
    Unknown4048(-45000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    sprite('esef400_EXpoint2', 5)	# 14-18
    Unknown4047(241, 241, 241)
    Unknown4048(-45000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('null', 12)	# 19-30
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end2', -1)
    Unknown3004(-21)
    ExitState()
    label(2)
    sprite('null', 6)	# 31-36
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end2', -1)
    Unknown3004(-42)

@State
def esef_400Aireff2nd_MatomeB():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 124):
                sendToLabel(1)
            if (SLOT_48 == 125):
                sendToLabel(2)
        Unknown2003(1)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
    sprite('esef400_EXpoint1', 3)	# 1-3
    GFX_0('shot2', -1)
    GFX_0('shot2_add', -1)
    GFX_0('esef_400_zan2', -1)
    Unknown23029(1, 122, 0)
    SFX_3('esse_03')
    label(0)
    sprite('esef400_EXpoint2', 4)	# 4-7
    Unknown4061(4)
    Unknown4047(241, 241, 241)
    Unknown4048(-80000)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
    gotoLabel(0)
    label(1)
    sprite('null', 12)	# 8-19
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end', -1)
    Unknown3004(-21)
    ExitState()
    label(2)
    sprite('null', 6)	# 20-25
    clearUponHandler(43)
    clearUponHandler(17)
    GFX_0('shot_end2', -1)
    Unknown3004(-42)

@State
def shot():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 120):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown4061(4)
    Unknown21004(241)
    Unknown4003('657365665f34303073686f745f4e6f4a65742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)
    label(0)
    sprite('null', 32767)	# 32768-65534
    Unknown4061(4)
    Unknown21004(241)
    Unknown4003('657365665f34303073686f742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)

@State
def shot_add():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4003('657365665f34303073686f745f6164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)

@State
def shot_sub():

    def upon_IMMEDIATE():
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4003('657365665f34303073686f745f7375622e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)

@State
def shot_end():

    def upon_IMMEDIATE():
        Unknown4061(4)
        Unknown3038(1)
        Unknown1096(700)
        Unknown4006(2)
    sprite('vresef400_ParitclePos00', 1)	# 1-1
    Unknown4048(-90000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4048(-90000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4048(-90000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4048(-90000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4048(-90000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
    Unknown4048(-90000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')
    Unknown4048(-90000)

@State
def shot_end2():

    def upon_IMMEDIATE():
        Unknown4061(4)
        Unknown3038(1)
        Unknown1096(700)
        Unknown4006(2)
    sprite('vresef400_ParitclePos00', 1)	# 1-1
    Unknown4048(-45000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4048(-45000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4048(-45000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4048(-45000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4048(-45000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
    Unknown4048(-45000)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')

@State
def shot_test():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 60)	# 1-60
    Unknown4003('657365665f34303073686f745f746573742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def shot2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)

        def upon_43():
            if (SLOT_48 == 120):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown4061(4)
    Unknown21004(241)
    Unknown4003('657365665f34303073686f74325f4e6f4a65742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)
    label(0)
    sprite('null', 32767)	# 32768-65534
    Unknown4061(4)
    Unknown21004(241)
    Unknown4003('657365665f34303073686f74322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)

@State
def shot2_add():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4003('657365665f34303073686f74325f6164642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def shot2_sub():

    def upon_IMMEDIATE():
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4003('657365665f34303073686f74325f7375622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(0)
    Unknown3004(32)

@State
def largeshot():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4061(4)
    Unknown21004(241)
    Unknown4003('657365665f3430306c6172676573686f742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def largeshot_add():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4003('657365665f3430306c6172676573686f745f6164642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def largeshot_sub():

    def upon_IMMEDIATE():
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
    sprite('null', 32767)	# 1-32767
    Unknown4003('657365665f3430306c6172676573686f745f7375622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def esef_400_zanzo():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 121):
                Unknown1072(42000)
                SLOT_51 = 1
            if (SLOT_48 == 122):
                Unknown1072(5000)
                SLOT_52 = 1
    label(1)
    sprite('null', 2)	# 1-2
    GFX_0('esef_400_zan_a', -1)
    if SLOT_51:
        Unknown23029(1, 121, 0)
    elif SLOT_52:
        Unknown23029(1, 122, 0)
    gotoLabel(1)

@State
def esef_400_zan_a():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 121):
                Unknown1072(42000)
            if (SLOT_48 == 122):
                Unknown1072(5000)
    sprite('null', 7)	# 1-7
    Unknown4061(4)
    Unknown21004(240)
    Unknown4003('657365665f34303073686f745f4e6f4a65742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(90)
    Unknown3004(-12)

@State
def esef_400_zan2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 121):
                Unknown1072(42000)
                SLOT_51 = 1
            if (SLOT_48 == 122):
                Unknown1072(5000)
                SLOT_52 = 1
    label(1)
    sprite('null', 2)	# 1-2
    GFX_0('esef_400_zan_a', -1)
    if SLOT_51:
        Unknown23029(1, 121, 0)
    elif SLOT_52:
        Unknown23029(1, 122, 0)
    gotoLabel(1)

@State
def esef_400_zan2_a():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 121):
                Unknown1072(42000)
            if (SLOT_48 == 122):
                Unknown1072(5000)
    sprite('null', 5)	# 1-5
    Unknown4061(4)
    Unknown21004(240)
    Unknown4003('657365665f34303073686f74325f4e6f4a65742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(90)
    Unknown3004(-15)
    Unknown1099(20)

@State
def esef_400large_zan():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
    label(1)
    sprite('null', 2)	# 1-2
    GFX_0('esef_400large_zan_a', -1)
    gotoLabel(1)

@State
def esef_400large_zan_a():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4006(2)
    sprite('null', 5)	# 1-5
    Unknown4061(4)
    Unknown21004(240)
    Unknown4003('657365665f3430306c6172676573686f742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3001(90)
    Unknown3004(-15)
    Unknown1099(20)

@State
def esef_400_zanzou():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('Zanzou')
    sprite('vresef400_00', 20)	# 1-20

@State
def esef_400_zanzou2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('Zanzou')
    sprite('vresef400_10', 20)	# 1-20

@State
def esef_401_zanzou():

    def upon_IMMEDIATE():
        callSubroutine('Zanzou')
    sprite('vresef401_00', 20)	# 1-20

@State
def esef_401_zanzou2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        callSubroutine('Zanzou')
    sprite('vresef401_10', 30)	# 1-30

@State
def esef_404_kick():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(3)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou')
        Unknown1007(45000)
    sprite('vresef404_00', 5)	# 1-5
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    sprite('vresef404_01', 5)	# 6-10
    sprite('vresef404_01', 12)	# 11-22
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')

@State
def esef_404_kick_BDD():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        callSubroutine('Zanzou')
        Unknown1007(-40000)
    sprite('vresef404_00', 5)	# 1-5
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
    sprite('vresef404_01', 4)	# 6-9
    Unknown4007(0)
    sprite('vresef404_02', 8)	# 10-17
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')

@State
def esef_406Eff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4009(3)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f343036736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(200000)
        Unknown1096(800)

        def upon_43():
            if (SLOT_48 == 111):
                Unknown2037(1)
            if (SLOT_48 == 101):
                sendToLabel(0)

        def upon_56():
            Unknown4009(0)
    sprite('null', 20)	# 1-20
    GFX_0('esef_406Effadd', -1)
    loopRest()
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000280000000200000002000000')
    label(0)
    sprite('null', 20)	# 21-40
    clearUponHandler(43)
    GFX_0('esef_406EffAddAtkParticle', -1)
    Unknown4003('657365665f343036736c6173685f3030656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_406Effadd')
    Unknown3004(-12)

@State
def esef_406Effadd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(3)
        Unknown3038(1)
        Unknown4003('657365665f343036736c6173685f3030656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(800)

        def upon_43():
            if (SLOT_48 == 111):
                Unknown2037(1)

        def upon_56():
            Unknown4009(0)
    sprite('null', 20)	# 1-20
    loopRest()
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000280000000200000002000000')
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def esef_406Eff2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f343036736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(200000)
        teleportRelativeX(-50000)
        Unknown1096(800)
    sprite('null', 25)	# 1-25
    GFX_0('esef_406Effadd2', -1)
    sprite('null', 20)	# 26-45
    Unknown21015('657365665f3430364566660000000000000000000000000000000000000000006500000000000000')
    Unknown4003('657365665f343036736c6173685f3031656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('esef_406EffAddAtkParticle2', -1)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown1007(-200000)
    Unknown35()
    Unknown26('esef_406Effadd2')
    Unknown3004(-12)

@State
def esef_406Effadd2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3038(1)
        Unknown4003('657365665f343036736c6173685f3031656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(800)
    sprite('null', 20)	# 1-20
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def esef_406EffEX():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown4009(3)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f343036736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(200000)
        Unknown1096(800)

        def upon_43():
            if (SLOT_48 == 111):
                Unknown2037(1)
            if (SLOT_48 == 102):
                sendToLabel(0)

        def upon_56():
            Unknown4009(0)
    sprite('null', 20)	# 1-20
    GFX_0('esef_406Effadd', -1)
    loopRest()
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000280000000200000002000000')
    label(0)
    sprite('null', 10)	# 21-30
    clearUponHandler(43)
    GFX_0('esef_406EffAddAtk', 100)
    if (not SLOT_2):
        GFX_0('es406_effAtk', -1)
    SFX_3('esse_01')
    sprite('null', 20)	# 31-50
    Unknown4003('657365665f343036736c6173685f3030656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('esef_406EffAddAtkParticle', -1)
    Unknown3004(-12)

@State
def esef_406Eff2EX():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4011(3)
        Unknown3038(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f343036736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(200000)
        teleportRelativeX(-50000)
        Unknown1096(800)
    sprite('null', 15)	# 1-15
    GFX_0('esef_406Effadd2', -1)
    sprite('null', 10)	# 16-25
    Unknown21015('657365665f3430364566664558000000000000000000000000000000000000006600000000000000')
    GFX_0('esef_406EffAddAtk2', 100)
    GFX_0('es407_effAtk', -1)
    sprite('null', 20)	# 26-45
    Unknown4003('657365665f343036736c6173685f3031656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('esef_406EffAddAtkParticle2', -1)
    Unknown3004(-12)

@State
def esef_406EffAddAtk():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f343036736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1096(800)
    sprite('null', 25)	# 1-25
    GFX_0('esef_406EffAddAtkadd', -1)
    Unknown4010(0)
    Unknown21010(1)
    sprite('null', 10)	# 26-35
    Unknown21015('657365665f34303645666641646441746b6164640000000000000000000000006500000000000000')
    Unknown21010(0)
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_406EffAddAtkadd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f343036736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown3038(1)
        Unknown1096(800)

        def upon_43():
            if (SLOT_48 == 101):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown4010(0)
    Unknown21010(1)
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown21010(0)
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_406EffAddAtk2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f343036736c61736841646441746b5f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1096(800)
    sprite('null', 25)	# 1-25
    GFX_0('esef_406EffAddAtkadd2', -1)
    ScreenShake(10000, 10000)
    Unknown4010(0)
    Unknown21010(1)
    Unknown26('esef_406Effadd')
    sprite('null', 10)	# 26-35
    Unknown21015('657365665f34303645666641646441746b6164643200000000000000000000006500000000000000')
    Unknown21010(0)
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_406EffAddAtkadd2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f343036736c61736841646441746b5f30316164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown3038(1)
        Unknown1096(800)

        def upon_43():
            if (SLOT_48 == 101):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown4010(0)
    Unknown21010(1)
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown21010(0)
    Unknown4010(0)
    Unknown3004(-25)

@State
def esef_406EffAddAtkParticle():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(4)
    sprite('vresef406_ParitclePos', 2)	# 1-2
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    sprite('vresef406_ParitclePos', 2)	# 3-4
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    sprite('vresef406_ParitclePos', 2)	# 5-6
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    sprite('vresef406_ParitclePos', 2)	# 7-8
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    sprite('vresef406_ParitclePos', 2)	# 9-10
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    sprite('vresef406_ParitclePos', 2)	# 11-12
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')

@State
def esef_406EffAddAtkParticle2():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(4)
        teleportRelativeX(150000)
    sprite('vresef406_ParitclePos2', 2)	# 1-2
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    sprite('vresef406_ParitclePos2', 2)	# 3-4
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    sprite('vresef406_ParitclePos2', 2)	# 5-6
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    sprite('vresef406_ParitclePos2', 2)	# 7-8
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    sprite('vresef406_ParitclePos2', 2)	# 9-10
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    sprite('vresef406_ParitclePos2', 2)	# 11-12

@State
def es406_effAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Monsho_AtkData')
        Damage(500)
        AirPushbackX(8000)
        AirPushbackY(22000)
        AirUntechableTime(40)
        PushbackX(19800)
        Unknown30065(0)
        Unknown4011(3)
        ScreenShake(5000, 5000)
    sprite('es406_effatk', 6)	# 1-6	 **attackbox here**
    sprite('null', 15)	# 7-21

@State
def es407_effAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Monsho_AtkData')
        Damage(500)
        GroundedHitstunAnimation(2)
        Unknown9142(36)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(24000)
        AirUntechableTime(55)
        PushbackX(19800)
        Unknown4011(3)
        ScreenShake(5000, 5000)
        Unknown30065(0)
    sprite('null', 7)	# 1-7
    sprite('es407_effatk', 6)	# 8-13	 **attackbox here**
    sprite('null', 15)	# 14-28

@State
def esef_408Eff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4047(241, 241, 241)
        Unknown23067('eseff_4083tame_jizoku')
        Unknown4003('657365665f3430385f4d436972636c6530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3038(1)
        Unknown1007(25000)
        Unknown19001(25000)
    sprite('null', 18)	# 1-18
    sprite('null', 10)	# 19-28
    Unknown3004(-26)
    Unknown1059(20)
    Unknown1091(20)

@State
def esef_430EffStartOD():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(4)
        Unknown21004(241)
        Unknown1007(310000)
        teleportRelativeX(288000)
        Unknown2054(1)
        Unknown4010(2)
        Unknown3001(255)
        Unknown1056(1500)
        Unknown1064(2200)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 114):
                sendToLabel(0)
            if (SLOT_48 == 115):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    GFX_0('esef_430EffStartODhikari', -1)
    Unknown4003('657365665f3433306566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('vresef430_ParitclePos', 32767)	# 32768-65534
    Unknown21015('657365665f34333045666653746172744f4468696b61726900000000000000007200000000000000')
    Unknown4003('657365665f3433306566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
    Unknown4049(1500)
    Unknown4047(241, 241, 241)
    Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
    label(1)
    sprite('null', 4)	# 65535-65538
    Unknown26('esef_430EffStartODhikari')
    ScreenShake(10000, 10000)
    GFX_0('esef_430EffStartAdd', -1)
    Unknown4003('657365665f3433306566663032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)	# 65539-65544
    Unknown4003('657365665f3433306566663033000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_430EffStartAdd')
    sprite('null', 20)	# 65545-65564
    Unknown3004(-12)

@State
def esef_430EffStartODhikari():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(4)
        Unknown2054(1)
        Unknown4006(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        Unknown3001(255)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 114):
                sendToLabel(0)
    sprite('null', 10)	# 1-10
    Unknown4003('657365665f3433306566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)	# 11-32777
    Unknown3004(-26)
    label(0)
    sprite('null', 5)	# 32778-32782
    Unknown4003('657365665f3433306566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)	# 32783-65549
    Unknown3004(-26)

    @State
    def esef_430EffStart():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(310000)
            teleportRelativeX(288000)
            Unknown2054(1)
            Unknown4010(2)
            Unknown3001(255)
            Unknown1056(1500)
            Unknown1064(2200)
            Unknown3038(1)

            def upon_43():
                if (SLOT_48 == 112):
                    sendToLabel(0)
                if (SLOT_48 == 113):
                    sendToLabel(1)
        sprite('null', 32767)	# 1-32767
        Unknown4003('657365665f3433306566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        label(0)
        sprite('vresef430_ParitclePos', 32767)	# 32768-65534
        Unknown4003('657365665f3433306566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
        Unknown4049(1500)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
        label(1)
        sprite('null', 4)	# 65535-65538
        ScreenShake(10000, 10000)
        GFX_0('esef_430EffStartAdd', -1)
        Unknown4003('657365665f3433306566663032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 6)	# 65539-65544
        Unknown4003('657365665f3433306566663033000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown26('esef_430EffStartAdd')
        sprite('null', 20)	# 65545-65564
        Unknown3004(-12)

    @State
    def esef_430EffStartAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown2054(1)
            Unknown4013(2)
            Unknown4010(2)
            Unknown4006(2)
            Unknown3001(255)
        sprite('null', 4)	# 1-4
        ScreenShake(10000, 10000)
        Unknown4003('657365665f3433306566663032616464000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 25)	# 5-29
        Unknown1099(10)

    @State
    def esef_430Eff():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(230000)
            teleportRelativeX(350000)
            Unknown1096(1300)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
        sprite('null', 4)	# 1-4
        Unknown3001(0)
        Unknown4003('657365665f343330656666303073686f740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        label(0)
        sprite('null', 5)	# 5-9
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3433305f67726173730000000000000000000000000000000000ffffffff')
        Unknown3001(255)
        gotoLabel(0)

    @State
    def esef_430EffAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown1007(230000)
            teleportRelativeX(350000)
            Unknown1096(1300)
        sprite('null', 4)	# 1-4
        Unknown3001(0)
        Unknown4003('657365665f343330656666303073686f740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 32767)	# 5-32771
        Unknown3001(255)
        Unknown4003('657365665f343330656666303073686f744164640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

    @Subroutine
    def es430_Init():
        Unknown4011(3)
        Unknown2011()
        AttackLevel_(4)
        Damage(4200)
        Unknown11091(27)
        AttackP2(60)
        Hitstop(6)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(45000)
        AirPushbackY(20000)
        PushbackX(50000)
        AirUntechableTime(40)
        Unknown9016(1)
        Unknown2055(60)

        def upon_3():
            if SLOT_38:
                Unknown23045('7d000000')
                if (SLOT_22 < SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)
            else:
                Unknown23045('7d000000')
                if (SLOT_22 > SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)

    @Subroutine
    def es430OD_Init():
        Unknown4011(3)
        Unknown2011()
        AttackLevel_(4)
        Damage(5200)
        Unknown11091(26)
        AttackP2(60)
        Hitstop(6)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(45000)
        AirPushbackY(20000)
        PushbackX(50000)
        AirUntechableTime(40)
        Unknown9016(1)
        Unknown9001(5)
        Unknown2055(60)

        def upon_3():
            if SLOT_38:
                Unknown23045('7d000000')
                if (SLOT_22 < SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)
            else:
                Unknown23045('7d000000')
                if (SLOT_22 > SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)

    @State
    def es430LandA():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            Unknown23056('')
        sprite('null', 4)	# 1-4
        GFX_0('esef_430Eff', -1)
        GFX_0('esef_430EffAdd', -1)
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_LandAtk1', 3)	# 5-7
        physicsXImpulse(70000)
        sprite('es430_LandAtk2', 60)	# 8-67
        label(580)
        sprite('null', 60)	# 68-127
        clearUponHandler(54)

    @State
    def es430LandB():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            AirPushbackX(40000)
            AirPushbackY(40000)
            teleportRelativeX(-50000)
            Unknown1007(50000)
            Unknown1072(345000)
            Unknown23089('0100000001000000010000000000000000000000000000000100000001000000')
            sendToLabelUpon(54, 580)
        sprite('null', 4)	# 1-4
        GFX_0('esef_430Eff', -1)
        Unknown36(1)
        Unknown1072(346000)
        Unknown35()
        GFX_0('esef_430EffAdd', -1)
        Unknown36(1)
        Unknown1072(346000)
        Unknown35()
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_LandAtk3', 3)	# 5-7
        Unknown1110(70000, 0)
        sprite('es430_LandAtk4', 60)	# 8-67
        label(580)
        sprite('null', 60)	# 68-127
        clearUponHandler(54)

    @State
    def esef_430EffOD():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(230000)
            teleportRelativeX(350000)
            Unknown1096(1300)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
        sprite('null', 4)	# 1-4
        Unknown3001(0)
        Unknown4003('657365665f343330656666303073686f740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        label(0)
        sprite('null', 6)	# 5-10
        GFX_0('esef_430EffODnokosi', -1)
        GFX_0('esef_430EffAddNokosi', -1)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3433305f67726173730000000000000000000000000000000000ffffffff')
        Unknown3001(255)
        gotoLabel(0)

    @State
    def esef_430EffODnokosi():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(240)
            Unknown1096(1300)
            Unknown3001(160)
            Unknown4010(2)
            Unknown23015(15)
        sprite('null', 1)	# 1-1
        Unknown4006(2)
        sprite('null', 20)	# 2-21
        Unknown3004(-8)
        Unknown4003('657365665f343330656666303073686f744164646e6f6b6f73690000000000000000000000000000000000000000000000000000000000000000000000000000')

    @State
    def esef_430EffAddNokosi():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown1096(800)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(-300000)
        sprite('null', 3)	# 1-3
        GFX_1('eseff_430_odparticle', -1)
        Unknown4003('657365665f3433306566665f6f643030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 20)	# 4-23
        Unknown3004(-12)
        Unknown1067(-20)

    @State
    def es430LandAOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            Unknown23056('')
        sprite('null', 4)	# 1-4
        GFX_0('esef_430EffOD', -1)
        GFX_0('esef_430EffAdd', -1)
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_LandAtk1', 2)	# 5-6
        physicsXImpulse(70000)
        label(0)
        sprite('es430_LandAtk1', 2)	# 7-8
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)	# 9-68
        clearUponHandler(54)

    @State
    def es430LandBOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            AirPushbackX(60000)
            AirPushbackY(30000)
            teleportRelativeX(-50000)
            Unknown1007(50000)
            Unknown1072(345000)
        sprite('null', 4)	# 1-4
        GFX_0('esef_430EffAddNokosiAir', -1)
        Unknown36(1)
        Unknown1072(346000)
        Unknown35()
        GFX_0('esef_430EffAirOD', -1)
        Unknown36(1)
        Unknown1072(346000)
        Unknown35()
        GFX_0('esef_430EffAdd', -1)
        Unknown36(1)
        Unknown1072(346000)
        Unknown35()
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_LandAtk3', 2)	# 5-6
        Unknown1110(70000, 0)
        label(0)
        sprite('es430_LandAtk3', 2)	# 7-8
        RefreshMultihit()
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)	# 9-68
        clearUponHandler(54)

    @State
    def esef_430EffAsiba():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4003('657365665f3331315f6d6330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1096(200)
            Unknown23015(11)

            def upon_43():
                if (SLOT_48 == 116):
                    sendToLabel(0)
        sprite('null', 5)	# 1-5
        Unknown1099(100)
        Unknown3001(128)
        sprite('null', 32767)	# 6-32772
        Unknown1099(1)
        label(0)
        sprite('null', 10)	# 32773-32782
        Unknown3004(-13)

    @State
    def es430AirA():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            Unknown23056('')
        sprite('null', 4)	# 1-4
        GFX_0('esef_430Eff', -1)
        GFX_0('esef_430EffAdd', -1)
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_LandAtk1', 3)	# 5-7
        physicsXImpulse(70000)
        sprite('es430_LandAtk2', 60)	# 8-67
        label(580)
        sprite('null', 60)	# 68-127
        clearUponHandler(54)

    @State
    def es430AirB():

        def upon_IMMEDIATE():
            callSubroutine('es430_Init')
            Unknown1072(10000)
            Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
            sendToLabelUpon(54, 580)
        sprite('null', 4)	# 1-4
        GFX_0('esef_430Eff', -1)
        Unknown36(1)
        Unknown1073(11000)
        Unknown35()
        GFX_0('esef_430EffAdd', -1)
        Unknown36(1)
        Unknown1073(11000)
        Unknown35()
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_AirAtk1', 3)	# 5-7
        Unknown1110(70000, 0)
        sprite('es430_AirAtk2', 60)	# 8-67
        label(580)
        sprite('null', 60)	# 68-127
        clearUponHandler(54)

    @State
    def esef_430EffAirOD():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(230000)
            teleportRelativeX(350000)
            Unknown1096(1300)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
        sprite('null', 4)	# 1-4
        Unknown3001(0)
        Unknown4003('657365665f343330656666303073686f740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        label(0)
        sprite('null', 6)	# 5-10
        GFX_0('esef_430EffODnokosi', -1)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3433305f67726173730000000000000000000000000000000000ffffffff')
        Unknown3001(255)
        gotoLabel(0)

    @State
    def esef_430EffAddNokosiAir():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown1096(800)
            Unknown1057(200)
            Unknown4061(4)
            Unknown21004(241)
            Unknown4003('657365665f34333165666630316f6432000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1007(250000)
            teleportRelativeX(290000)
            Unknown4007(2)
            Unknown4010(2)
        label(0)
        sprite('null', 4)	# 1-4
        Unknown4048(11000)
        Unknown4049(1400)
        Unknown4045('65736566665f3433305f6f647061727469636c65416972000000000000000000ffffffff')
        gotoLabel(0)

    @State
    def es430AirAOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            AirPushbackY(20000)
            Unknown23056('')
        sprite('null', 4)	# 1-4
        GFX_0('esef_430EffAddNokosiAir', -1)
        GFX_0('esef_430EffAirOD', -1)
        GFX_0('esef_430EffAdd', -1)
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_LandAtk1', 2)	# 5-6
        physicsXImpulse(70000)
        label(0)
        sprite('es430_LandAtk1', 2)	# 7-8
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)	# 9-68
        clearUponHandler(54)

    @State
    def es430AirBOD():

        def upon_IMMEDIATE():
            callSubroutine('es430OD_Init')
            Unknown1072(10000)
        sprite('null', 4)	# 1-4
        GFX_0('esef_430EffAddNokosiAir', -1)
        Unknown36(1)
        Unknown1073(11000)
        Unknown35()
        GFX_0('esef_430EffAirOD', -1)
        Unknown36(1)
        Unknown1073(11000)
        Unknown35()
        GFX_0('esef_430EffAdd', -1)
        Unknown36(1)
        Unknown1073(11000)
        Unknown35()
        SFX_3('esse_04')
        SFX_3('esse_04')
        sprite('es430_AirAtk1', 2)	# 5-6
        Unknown1110(70000, 0)
        label(0)
        sprite('es430_LandAtk3', 2)	# 7-8
        RefreshMultihit()
        loopRest()
        gotoLabel(0)
        label(580)
        sprite('null', 60)	# 9-68
        clearUponHandler(54)

    @State
    def esef_431Eff():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown4009(2)
            Unknown4010(3)
            Unknown4022(2)

            def upon_43():
                if (SLOT_48 == 104):
                    sendToLabel(0)
                if (SLOT_48 == 105):
                    sendToLabel(2)
            Unknown1007(200000)
            teleportRelativeX(200000)
        sprite('null', 32767)	# 1-32767
        GFX_0('esef_431Emb', -1)
        GFX_0('esef_431EffSub', -1)
        label(0)
        sprite('esef431_03', 1)	# 32768-32768
        GFX_0('esef_431Tossin', -1)
        Unknown3038(1)
        Unknown1096(1200)
        Unknown21015('657365665f343331456d620000000000000000000000000000000000000000006a00000000000000')
        Unknown21015('657365665f3433314566665375620000000000000000000000000000000000006b00000000000000')
        Unknown2054(1)
        Unknown1059(15)
        Unknown3029(1)
        label(1)
        sprite('esef431_03', 2)	# 32769-32770
        GFX_0('esef_431EmbNokosi', -1)
        gotoLabel(1)
        label(2)
        sprite('esef431_04', 10)	# 32771-32780
        Unknown21015('657365665f343331546f7373696e0000000000000000000000000000000000006d00000000000000')
        Unknown3004(-31)

    @State
    def esef_431Emb():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown4010(3)

            def upon_43():
                if (SLOT_48 == 106):
                    sendToLabel(0)
            teleportRelativeX(70000)
        sprite('null', 10)	# 1-10
        Unknown1096(50)
        Unknown1099(75)
        Unknown4003('657365665f3433316566665f656d6230300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_0('esef_431EmbAdd', -1)
        sprite('null', 32767)	# 11-32777
        Unknown1099(1)
        label(0)
        sprite('null', 5)	# 32778-32782
        Unknown1099(50)
        sprite('null', 20)	# 32783-32802
        Unknown23015(15)
        Unknown21015('657365665f343331456d624164640000000000000000000000000000000000006c00000000000000')
        Unknown3004(-12)
        Unknown1099(5)
        Unknown4022(0)
        Unknown4010(0)

    @State
    def esef_431EmbAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(3)
            Unknown4013(2)

            def upon_43():
                if (SLOT_48 == 108):
                    sendToLabel(0)
        sprite('null', 32767)	# 1-32767
        Unknown4003('657365665f3433316566665f656d6230300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        label(0)
        sprite('null', 20)	# 32768-32787
        Unknown23015(15)
        Unknown3004(-12)
        Unknown1099(5)
        Unknown4010(0)

    @State
    def esef_431EffSub():

        def upon_IMMEDIATE():
            Unknown2054(1)
            Unknown4010(3)
            Unknown4007(2)

            def upon_43():
                if (SLOT_48 == 107):
                    sendToLabel(0)
            Unknown1096(2000)
        sprite('null', 32767)	# 1-32767
        GFX_2('eseff_431gen')
        label(0)
        sprite('null', 10)	# 32768-32777
        Unknown3004(-25)

    @State
    def esef_431EmbNokosi():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown23015(15)
        sprite('null', 10)	# 1-10
        Unknown4003('657365665f3433316566665f656d6230310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3004(-25)
        Unknown1099(20)

    @State
    def esef_431Tossin():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown4010(3)
            Unknown4007(2)
            Unknown4003('657365665f3433315f746f7373696e30300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

            def upon_43():
                if (SLOT_48 == 109):
                    sendToLabel(0)
            Unknown1096(800)
            Unknown1065(200)
        sprite('null', 5)	# 1-5
        GFX_0('esef_431TossinAdd', -1)
        Unknown1067(-5)
        sprite('null', 32767)	# 6-32772
        Unknown3004(13)
        label(0)
        sprite('null', 10)	# 32773-32782
        Unknown3004(-25)

    @State
    def esef_431TossinAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4013(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('657365665f3433315f746f7373696e30306164640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 5)	# 1-5
        sprite('null', 10)	# 6-15
        Unknown3004(26)

    @State
    def esef_431Camera():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown2054(1)
            Unknown20000(1)
            Unknown20009(900)
        sprite('null', 300)	# 1-300

    @State
    def esef_431Eff2():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4061(4)
            Unknown4010(2)
            Unknown4007(2)
            Unknown2054(1)
        sprite('esef431_20', 5)	# 1-5
        sprite('esef431_11', 3)	# 6-8
        teleportRelativeX(-300000)
        ScreenShake(10000, 10000)
        Unknown4007(0)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        sprite('esef431_11', 3)	# 9-11
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        sprite('esef431_12', 6)	# 12-17
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        sprite('esef431_13', 6)	# 18-23
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        sprite('esef431_14', 5)	# 24-28
        sprite('esef431_15', 5)	# 29-33

    @State
    def esef_431EffSlash():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown2054(1)
            Unknown1007(180000)
        sprite('null', 60)	# 1-60
        Unknown4047(241, 241, 241)
        Unknown23067('eseff_431_slash')

    @State
    def esef_431EffSlashOD():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown2054(1)
            Unknown1007(180000)
        sprite('null', 80)	# 1-80
        GFX_0('esef_431EffSlashODCorol', -1)
        Unknown23067('eseff_431_slashOD')

    @State
    def esef_431EffSlashODCorol():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown2054(1)
            Unknown1064(2000)
        sprite('null', 60)	# 1-60
        Unknown4047(241, 241, 241)
        Unknown23067('eseff_431_slash01')

    @State
    def esef_431EffEsRay():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4003('657365665f3433316573526179303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(3)
            Unknown1096(2435)
            Unknown3001(200)
            Unknown1007(15000)
        sprite('null', 19)	# 1-19
        GFX_0('esef_431EffEsRayColor', -1)
        sprite('null', 10)	# 20-29
        sprite('null', 10)	# 30-39
        Unknown3004(-20)

    @State
    def esef_431EffEsRayColor():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4003('657365665f3433316573526179303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4013(2)
            Unknown4061(4)
            Unknown21004(240)
        sprite('null', 24)	# 1-24
        sprite('null', 15)	# 25-39
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3433315f726179656e6400000000000000000000000000000000ffffffff')

    @State
    def esef_431EffScrew():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4003('657365665f3433316566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(200000)
            teleportRelativeX(200000)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(3)
            Unknown1065(1100)
            Unknown1089(1100)
        sprite('null', 14)	# 1-14
        sprite('null', 5)	# 15-19
        Unknown3004(-51)

    @State
    def esef_431EffScrewOD():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4003('657365665f34333165666630316f6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown1007(200000)
            teleportRelativeX(300000)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(3)
            Unknown1065(1080)
            Unknown1089(1320)
            Unknown3001(128)
        sprite('null', 6)	# 1-6
        GFX_0('esef_431EffMcOD', -1)
        Unknown1067(-20)
        Unknown1091(-20)
        sprite('null', 6)	# 7-12
        GFX_0('esef_431EffMcOD', -1)
        sprite('null', 6)	# 13-18
        GFX_0('esef_431EffMcOD', -1)
        sprite('null', 6)	# 19-24
        GFX_0('esef_431EffMcOD', -1)
        sprite('null', 9)	# 25-33
        GFX_0('esef_431EffMcOD', -1)
        sprite('null', 19)	# 34-52
        Unknown3004(-6)

    @State
    def esef_431EffMcOD():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4003('657365665f34333165666630316f645f636972636c65000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown3001(0)
            Unknown1072(-20000)
        sprite('null', 5)	# 1-5
        Unknown3004(40)
        physicsXImpulse(-12500)
        sprite('null', 5)	# 6-10
        Unknown3004(0)
        physicsXImpulse(-35000)
        Unknown1099(50)
        sprite('null', 10)	# 11-20
        Unknown3004(-25)

    @State
    def esef_340():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4010(3)
            Unknown4007(3)
            Unknown1072(-30000)
            teleportRelativeX(-6000)
            Unknown4061(4)
        sprite('esef340_circle', 3)	# 1-3
        GFX_0('esef_340_circle1', -1)
        GFX_0('esef_340_circle2', -1)
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
        label(0)
        sprite('esef340_circle', 3)	# 4-6
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
        gotoLabel(0)

    @State
    def esef_340_circle1():

        def upon_IMMEDIATE():
            Unknown4061(4)
            Unknown21004(240)
            Unknown4011(3)
            Unknown4010(3)
            Unknown4007(3)
            Unknown4006(2)
            Unknown4003('657365665f333430636972636c652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

            def upon_43():
                if (SLOT_48 == 100):
                    sendToLabel(0)
        sprite('null', 12)	# 1-12
        Unknown3001(0)
        Unknown3004(21)
        Unknown1096(437)
        Unknown1100(36)
        sprite('null', 32767)	# 13-32779
        Unknown3001(255)
        Unknown3004(0)
        Unknown1096(875)
        Unknown1099(0)
        label(0)
        sprite('null', 10)	# 32780-32789
        Unknown3001(255)
        Unknown3004(0)
        Unknown1096(875)
        Unknown1099(0)
        Unknown3004(-25)
        Unknown1099(50)

    @State
    def esef_340_circle2():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4010(3)
            Unknown4007(3)
            Unknown4006(2)
            Unknown4061(4)
            Unknown21004(240)
            Unknown4003('657365665f333430636972636c65322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

            def upon_43():
                if (SLOT_48 == 100):
                    sendToLabel(0)
        sprite('null', 12)	# 1-12
        GFX_0('esef_340_circle2Add', -1)
        Unknown3001(0)
        Unknown3004(21)
        Unknown1096(375)
        Unknown1100(31)
        teleportRelativeX(27000)
        Unknown1007(9000)
        sprite('null', 32767)	# 13-32779
        Unknown3001(255)
        Unknown3004(0)
        Unknown1096(750)
        Unknown1099(0)
        label(0)
        sprite('null', 10)	# 32780-32789
        Unknown21015('657365665f3334305f636972636c6532416464000000000000000000000000006400000000000000')
        Unknown3001(255)
        Unknown3004(0)
        Unknown1096(750)
        Unknown1099(0)
        Unknown3004(-25)
        Unknown1099(50)

    @State
    def esef_340_circle2Add():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4010(3)
            Unknown4007(3)
            Unknown4006(2)
            Unknown4003('657365665f333430636972636c65326164642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

            def upon_43():
                if (SLOT_48 == 100):
                    sendToLabel(0)
        sprite('null', 12)	# 1-12
        Unknown3001(0)
        Unknown3004(21)
        Unknown1096(375)
        Unknown1100(31)
        teleportRelativeX(27000)
        Unknown1007(9000)
        sprite('null', 32767)	# 13-32779
        Unknown3001(255)
        Unknown3004(0)
        Unknown1096(750)
        Unknown1099(0)
        label(0)
        sprite('null', 5)	# 32780-32784
        Unknown3001(255)
        Unknown3004(0)
        Unknown1096(750)
        Unknown1099(0)
        Unknown3004(-51)
        Unknown1099(50)

    @State
    def esef_340_blade():

        def upon_IMMEDIATE():
            Unknown1007(200000)
            teleportRelativeX(50000)
            Unknown4009(3)
        sprite('null', 10)	# 1-10
        GFX_0('esef_340_blade_color', -1)
        GFX_0('esef_340_blade_add', -1)
        Unknown4061(4)
        Unknown4047(241, 241, 240)
        Unknown4045('657365665f333430637261736800000000000000000000000000000000000000ffffffff')
        sprite('null', 15)	# 11-25

    @State
    def esef_340_blade_color():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4011(3)
            Unknown4009(2)
            Unknown4015()
            Unknown4061(4)
            Unknown21004(240)
            Unknown1072(75000)
            Unknown1096(1400)
            Unknown1057(650)
            Unknown3038(1)
        sprite('null', 2)	# 1-2
        Unknown4003('657365665f333430626c6164655f73746172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 4)	# 3-6
        Unknown4003('657365665f333430626c6164652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('vresef340_ParitclePos', 10)	# 7-16
        Unknown3004(-25)
        Unknown1059(7)
        Unknown1067(14)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')

    @State
    def esef_340_blade_add():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown1096(1400)
            Unknown4011(3)
            Unknown4015()
            Unknown1072(75000)
            Unknown1057(650)
        sprite('null', 2)	# 1-2
        Unknown4003('657365665f333430626c6164655f73746172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 4)	# 3-6
        Unknown4003('657365665f333430626c6164652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        sprite('null', 9)	# 7-15
        Unknown4003('657365665f333430626c6164655f656e642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3004(-51)
        Unknown1059(-7)
        Unknown1067(14)

    @State
    def esef_340_zanzou():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4010(3)
            Unknown4007(3)
            callSubroutine('Zanzou')
        sprite('vresef340_00', 1)	# 1-1
        sprite('vresef340_00', 16)	# 2-17
        Unknown3004(-25)

    @State
    def esef_233Add():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown4013(2)
            Unknown4003('657365665f323333736c6173685f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3033()
        sprite('null', 32767)	# 1-32767

    @State
    def esef_233():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown4003('657365665f323333736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3038(1)
            Unknown1096(950)
            teleportRelativeY(12000)
        sprite('vresef233_ParitclePos', 15)	# 1-15
        GFX_0('esef_233Add', -1)
        Unknown4047(240, 240, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(240, 240, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(240, 240, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(240, 240, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        Unknown4047(240, 240, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        Unknown4047(240, 240, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
        sprite('null', 15)	# 16-30
        Unknown4003('657365665f323333736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown26('esef_233Add')
        Unknown4010(0)
        Unknown21010(1)
        Unknown2054(1)

    @State
    def es233_effAtk_Yotyou():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(3)
            Unknown4003('657365665f323333736c6173685f796f74796f7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown23015(15)
            Unknown1096(850)
            Unknown1057(200)
            teleportRelativeX(-200000)
            Unknown1007(25000)
        sprite('null', 5)	# 1-5
        Unknown3001(0)
        Unknown3004(10)
        label(0)
        sprite('null', 5)	# 6-10
        sprite('null', 10)	# 11-20
        Unknown3004(-13)
        sprite('null', 10)	# 21-30
        Unknown3004(13)
        gotoLabel(0)

    @State
    def esef_233Monsho():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4003('657365665f323333736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown3038(1)
            Unknown1096(950)
            teleportRelativeY(12000)
            teleportRelativeX(-50000)
        sprite('null', 5)	# 1-5
        ScreenShake(5000, 5000)
        GFX_0('esef_233MonshoAdd', 100)
        Unknown21010(1)
        sprite('null', 10)	# 6-15
        Unknown21010(0)
        Unknown4009(2)
        sprite('vresef213_ParitclePos', 10)	# 16-25
        Unknown4003('657365665f323333736c61736841646441746b5f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown26('esef_233MonshoAdd')
        Unknown3004(-25)
        Unknown4009(0)
        Unknown4010(0)
        Unknown2054(1)

    @State
    def esef_233MonshoAdd():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown4013(2)
            Unknown4003('657365665f323333736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3033()
        sprite('null', 32767)	# 1-32767

    @State
    def es233_effAtk():

        def upon_IMMEDIATE():
            Unknown2009()
            callSubroutine('Monsho_AtkData')
            AirPushbackX(20000)
            AirPushbackY(20000)
            Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

            def upon_54():
                Unknown13(25)

            def upon_43():
                if (SLOT_48 == 103):
                    sendToLabel(0)
                if (SLOT_48 == 110):
                    Unknown13(25)
                if (SLOT_48 == 129):
                    Unknown13(25)
                    Unknown13(11)
        sprite('null', 10)	# 1-10
        sprite('null', 5)	# 11-15
        GFX_0('es233_effAtk_Yotyou', -1)
        clearUponHandler(43)
        Unknown38(11, 1)
        label(0)
        clearUponHandler(43)
        sprite('null', 3)	# 16-18
        Unknown13(11)
        GFX_0('esef_233Monsho', -1)
        SFX_3('esse_01')
        sprite('es233_effatk', 3)	# 19-21	 **attackbox here**
        clearUponHandler(43)
        sprite('null', 50)	# 22-71

    @State
    def es233_effAtkASS():

        def upon_IMMEDIATE():
            Unknown2009()
            callSubroutine('Monsho_AtkData')
            AirPushbackX(5500)
            AirPushbackY(20000)
            Hitstop(7)
            AirUntechableTime(40)
            Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

            def upon_54():
                Unknown13(25)

            def upon_43():
                if (SLOT_48 == 103):
                    sendToLabel(0)
                if (SLOT_48 == 110):
                    Unknown13(25)
        sprite('null', 20)	# 1-20
        sprite('null', 5)	# 21-25
        GFX_0('es233_effAtk_Yotyou', -1)
        Unknown38(11, 1)
        label(0)
        sprite('null', 3)	# 26-28
        Unknown13(11)
        GFX_0('esef_233Monsho', -1)
        SFX_3('esse_01')
        sprite('es233_effatk', 3)	# 29-31	 **attackbox here**
        sprite('null', 50)	# 32-81

    @State
    def es233_effAtkOD():

        def upon_IMMEDIATE():
            Unknown2009()
            callSubroutine('Monsho_AtkData')
            AirPushbackX(5500)
            AirPushbackY(20000)
            Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

            def upon_54():
                Unknown13(25)

            def upon_43():
                if (SLOT_48 == 103):
                    sendToLabel(0)
                if (SLOT_48 == 110):
                    Unknown13(25)
            Unknown1098(120)
        sprite('null', 20)	# 1-20
        sprite('null', 5)	# 21-25
        label(0)
        sprite('null', 10)	# 26-35
        sprite('null', 3)	# 36-38
        GFX_0('esef_233Monsho', -1)
        Unknown36(1)
        Unknown1098(120)
        Unknown35()
        sprite('es233_effatk', 3)	# 39-41	 **attackbox here**
        sprite('null', 50)	# 42-91

    @State
    def esef_409_3rd():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
        sprite('esef409_3rd', 10)	# 1-10
        Unknown3038(1)
        GFX_0('esef_409_3rd_kick', -1)
        GFX_0('esef_409_3rd_kick_add', -1)
        Unknown4061(4)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        sprite('esef409_3rd', 20)	# 11-30
        Unknown4007(0)

    @State
    def esef_409_3rd_kick():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown1096(1500)
            Unknown1007(225000)
        sprite('null', 10)	# 1-10
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f3430396b69636b322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        sprite('null', 10)	# 11-20
        Unknown4007(0)
        Unknown3004(-25)

    @State
    def esef_409_3rd_kick_add():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown1096(1500)
            Unknown1007(225000)
        sprite('null', 10)	# 1-10
        Unknown4003('657365665f3430396b69636b325f6164642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        sprite('null', 10)	# 11-20
        Unknown4007(0)
        Unknown3004(-25)

    @State
    def suef_600_screen():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4061(3)
            Unknown3035()
            Unknown23015(15)

            def upon_3():
                Unknown23057(50)
                Unknown23058(50)

            def upon_STATE_END():
                Unknown36(24)
                Unknown3025(-1, 32)
                Unknown35()
        sprite('esef600_screen', 32)	# 1-32
        Unknown3001(0)
        Unknown3004(2)
        Unknown36(24)
        Unknown3025(-6908266, 32)
        Unknown35()
        sprite('esef600_screen', 60)	# 33-92
        Unknown3004(0)
        Unknown3001(64)
        sprite('esef600_screen', 32)	# 93-124
        Unknown3004(-2)
        Unknown36(24)
        Unknown3025(-1, 32)
        Unknown35()

    @State
    def suef_600_es():

        def upon_IMMEDIATE():
            Unknown4061(4)
            Unknown3033()
        sprite('esef600_00', 16)	# 1-16
        Unknown3001(0)
        Unknown3004(16)
        sprite('esef600_00', 16)	# 17-32
        Unknown3004(-16)

    @State
    def suef_600_light_core():
        sprite('null', 32)	# 1-32
        Unknown4061(4)
        Unknown4054(11)
        Unknown4047(241, 241, 241)
        Unknown23067('esef_600core')
        Unknown1096(0)
        Unknown1099(100)
        Unknown3004(-8)

    @State
    def suef_600_light():
        sprite('null', 1)	# 1-1
        Unknown4061(4)
        Unknown4054(11)
        Unknown4047(240, 240, 240)
        Unknown4045('657365665f3630306c6967687400000000000000000000000000000000000000ffffffff')
        Unknown4054(11)
        Unknown4047(241, 241, 241)
        Unknown4045('657365665f363030616d69646100000000000000000000000000000000000000ffffffff')
        GFX_1('esef_600dust', -1)

    @State
    def esef_600light_end():
        sprite('null', 9)	# 1-9
        sprite('null', 1)	# 10-10
        Unknown4061(4)
        Unknown4047(241, 241, 241)
        Unknown4045('657365665f363030656e64000000000000000000000000000000000000000000ffffffff')
        GFX_1('esef_600end2', -1)

    @State
    def esef_600_particle():

        def upon_IMMEDIATE():
            Unknown4007(2)
            Unknown4061(4)
            Unknown3038(1)
        label(0)
        sprite('es600_09', 5)	# 1-5
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
        gotoLabel(0)

    @State
    def esef_601():

        def upon_IMMEDIATE():
            teleportRelativeX(180000)
            Unknown1007(256000)
        sprite('null', 1)	# 1-1
        GFX_0('esef_601_sword', -1)
        GFX_0('esef_601_sword_add', -1)
        GFX_0('esef_601_bloom', -1)
        GFX_0('esef_601_sub', -1)
        GFX_0('esef_601_sword_particle', -1)

    @State
    def esef_601_bloom():

        def upon_IMMEDIATE():
            Unknown4061(4)
            Unknown4047(240, 240, 240)
            Unknown23067('esef_601bloom')
            sendToLabelUpon(32, 0)
        sprite('null', 32767)	# 1-32767
        Unknown3001(0)
        Unknown3004(4)
        label(0)
        sprite('null', 60)	# 32768-32827
        Unknown3004(-4)

    @State
    def esef_601_sub():

        def upon_IMMEDIATE():
            GFX_2('esef_601sub')
            sendToLabelUpon(32, 0)
        sprite('null', 32767)	# 1-32767
        Unknown3001(0)
        Unknown3004(4)
        label(0)
        sprite('null', 60)	# 32768-32827
        Unknown3004(-4)

    @State
    def esef_601_sword_particle():

        def upon_IMMEDIATE():
            Unknown4061(4)
        label(0)
        sprite('esef601_sword', 16)	# 1-16
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000006a000000')
        gotoLabel(0)

    @State
    def esef_601_sword():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown1096(860)

            def upon_32():
                SLOT_51 = 1
        sprite('null', 10)	# 1-10
        sprite('null', 100)	# 11-110
        Unknown4061(4)
        Unknown21004(241)
        Unknown4003('657365665f36303173776f72642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
        Unknown3004(6)
        label(0)
        sprite('null', 3)	# 111-113
        Unknown4003('657365665f36303173776f7264332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        loopRest()
        Unknown19(0, 2, 51)
        sprite('null', 34)	# 114-147
        sprite('null', 15)	# 148-162
        Unknown21007(3, 32)
        sprite('null', 7)	# 163-169
        Unknown4003('657365665f36303173776f7264322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_0('esef_601_sword_zanzou1', -1)
        sprite('null', 7)	# 170-176
        GFX_0('esef_601_sword_zanzou2', -1)
        sprite('null', 7)	# 177-183
        GFX_0('esef_601_sword_zanzou3', -1)

    @State
    def esef_601_sword_add():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown1096(860)

            def upon_32():
                SLOT_51 = 1
        sprite('null', 10)	# 1-10
        sprite('null', 100)	# 11-110
        Unknown4061(4)
        Unknown21004(242)
        Unknown4003('657365665f36303173776f72645f6164642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
        Unknown3004(6)
        label(0)
        sprite('null', 3)	# 111-113
        Unknown4003('657365665f36303173776f7264335f6164642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        loopRest()
        Unknown19(0, 2, 51)
        sprite('null', 34)	# 114-147
        sprite('null', 15)	# 148-162
        sprite('null', 7)	# 163-169
        Unknown4003('657365665f36303173776f7264325f6164642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 7)	# 170-176
        sprite('null', 7)	# 177-183

    @State
    def esef_601_sword_zanzou1():
        sprite('null', 28)	# 1-28
        Unknown1096(860)
        Unknown23015(11)
        Unknown4061(4)
        Unknown21004(240)
        Unknown4003('657365665f36303173776f7264325f7a616e7a6f75312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3004(-5)

    @State
    def esef_601_sword_zanzou2():
        sprite('null', 21)	# 1-21
        Unknown1096(860)
        Unknown23015(11)
        Unknown4061(4)
        Unknown21004(240)
        Unknown4003('657365665f36303173776f7264325f7a616e7a6f75322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3004(-10)

    @State
    def esef_601_sword_zanzou3():
        sprite('null', 7)	# 1-7
        Unknown1096(860)
        Unknown23015(11)
        Unknown4061(4)
        Unknown21004(240)
        Unknown4003('657365665f36303173776f7264325f7a616e7a6f75332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3004(-15)
        sprite('null', 14)	# 8-21
        GFX_0('esef_601_sword_zanzou4', -1)

    @State
    def esef_601_sword_zanzou4():
        sprite('null', 21)	# 1-21
        Unknown1096(860)
        Unknown23015(11)
        Unknown4061(4)
        Unknown21004(240)
        Unknown4003('657365665f36303173776f7264325f7a616e7a6f75342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3004(-20)

    @State
    def esef_601_zanzou():

        def upon_IMMEDIATE():
            Unknown4061(4)
            Unknown3033()
        sprite('esef601_00', 7)	# 1-7
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        sprite('esef601_01', 7)	# 8-14
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        sprite('esef601_02', 7)	# 15-21
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')

    @State
    def esef_610_emblem():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4007(3)
            Unknown3033()
            Unknown4061(3)
            Unknown3001(0)
            Unknown3004(4)
            Unknown2007()
        sprite('null', 10)	# 1-10
        GFX_0('esef_610_particle', -1)
        loopRest()
        Unknown1096(625)
        if Unknown42('brg'):
            sendToLabel(1)
        if Unknown42('bjn'):
            sendToLabel(2)
        if Unknown42('bno'):
            sendToLabel(3)
        if Unknown42('brc'):
            sendToLabel(4)
        if Unknown42('btg'):
            sendToLabel(6)
        if Unknown42('bha'):
            sendToLabel(11)
        if Unknown42('bny'):
            sendToLabel(12)
        if Unknown42('bhz'):
            sendToLabel(14)
        if Unknown42('bmk'):
            sendToLabel(16)
        if Unknown42('bpt'):
            sendToLabel(18)
        if Unknown42('biz'):
            sendToLabel(20)
        if Unknown42('baz'):
            sendToLabel(23)
        if Unknown42('bph'):
            sendToLabel(31)
        if Unknown42('bes'):
            sendToLabel(34)
        if Unknown42('bjb'):
            sendToLabel(36)
        label(1)
        sprite('esef_emb_rg', 32767)	# 11-32777
        label(2)
        sprite('esef_emb_jn', 32767)	# 32778-65544
        label(3)
        sprite('esef_emb_no', 32767)	# 65545-98311
        label(4)
        sprite('esef_emb_rc', 32767)	# 98312-131078
        label(5)
        sprite('esef_emb_tk', 32767)	# 131079-163845
        label(6)
        sprite('esef_emb_tg', 32767)	# 163846-196612
        label(7)
        sprite('esef_emb_lc', 32767)	# 196613-229379
        label(8)
        sprite('esef_emb_ar', 32767)	# 229380-262146
        label(9)
        sprite('esef_emb_bn', 32767)	# 262147-294913
        label(10)
        sprite('esef_emb_ca', 32767)	# 294914-327680
        label(11)
        sprite('esef_emb_ha', 32767)	# 327681-360447
        label(12)
        sprite('esef_emb_ny', 32767)	# 360448-393214
        label(13)
        sprite('esef_emb_tb', 32767)	# 393215-425981
        label(14)
        sprite('esef_emb_hz', 32767)	# 425982-458748
        label(15)
        sprite('esef_emb_mu', 32767)	# 458749-491515
        label(16)
        sprite('esef_emb_mk', 32767)	# 491516-524282
        label(17)
        sprite('esef_emb_vh', 32767)	# 524283-557049
        label(18)
        sprite('esef_emb_pt', 32767)	# 557050-589816
        label(19)
        sprite('esef_emb_rl', 32767)	# 589817-622583
        label(20)
        sprite('esef_emb_iz', 32767)	# 622584-655350
        label(21)
        sprite('esef_emb_am', 32767)	# 655351-688117
        label(22)
        sprite('esef_emb_bl', 32767)	# 688118-720884
        label(23)
        sprite('esef_emb_az', 32767)	# 720885-753651
        label(24)
        sprite('esef_emb_kg', 32767)	# 753652-786418
        label(25)
        sprite('esef_emb_kk', 32767)	# 786419-819185
        label(26)
        sprite('esef_emb_tm', 32767)	# 819186-851952
        label(27)
        sprite('esef_emb_ce', 32767)	# 851953-884719
        label(28)
        sprite('esef_emb_rm', 32767)	# 884720-917486
        label(29)
        sprite('esef_emb_hb', 32767)	# 917487-950253
        label(30)
        sprite('esef_emb_nt', 32767)	# 950254-983020
        label(31)
        sprite('esef_emb_ph', 32767)	# 983021-1015787
        label(32)
        sprite('esef_emb_mi', 32767)	# 1015788-1048554
        label(33)
        sprite('esef_emb_su', 32767)	# 1048555-1081321
        label(34)
        sprite('esef_emb_es', 32767)	# 1081322-1114088
        label(35)
        sprite('esef_emb_ma', 32767)	# 1114089-1146855
        label(36)
        sprite('esef_emb_jb', 32767)	# 1146856-1179622

    @State
    def esef_610_particle():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4007(3)
        sprite('null', 1)	# 1-1
        GFX_0('esef_610_particle_color', -1)
        GFX_0('esef_610_particle_sub', -1)

    @State
    def esef_610_particle_color():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4007(3)
            Unknown4061(4)
            Unknown4047(240, 240, 240)
            Unknown23067('esef_610light')
            Unknown3001(0)
            Unknown3004(8)
        sprite('null', 30)	# 1-30
        Unknown4047(241, 241, 241)
        Unknown4045('657365665f363130736d6f6b6500000000000000000000000000000000000000ffffffff')
        GFX_1('esef_610dust', -1)
        GFX_1('esef_610circle', -1)
        label(0)
        sprite('null', 30)	# 31-60
        Unknown4047(241, 241, 241)
        Unknown4045('657365665f363130736d6f6b6500000000000000000000000000000000000000ffffffff')
        GFX_1('esef_610dust', -1)
        gotoLabel(0)

    @State
    def esef_610_particle_sub():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4007(3)
            GFX_2('esef_610sub')
            Unknown3001(0)
            Unknown3004(8)
        sprite('null', 32767)	# 1-32767

    @State
    def esef_611():
        GFX_0('esef_611_sword', -1)
        GFX_0('esef_611_sword_add', -1)
        GFX_0('esef_611_particle', -1)

    @State
    def esef_611_sword():

        def upon_IMMEDIATE():
            Unknown4061(0)
            Unknown3032()
        sprite('esef611_sword00', 7)	# 1-7

    @State
    def esef_611_sword_add():

        def upon_IMMEDIATE():
            Unknown4061(4)
            Unknown3033()
            Unknown2019(-1000)
        sprite('esef611_sword01', 7)	# 1-7
        Unknown3001(0)
        Unknown3004(36)
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        sprite('esef611_sword02', 7)	# 8-14
        sprite('esef611_sword03', 7)	# 15-21
        sprite('esef611_sword04', 7)	# 22-28
        sprite('null', 1)	# 29-29
        GFX_0('esef_611_henkei', -1)

    @State
    def esef_611_henkei():
        GFX_0('esef_611_sword2', -1)
        GFX_0('esef_611_sword2_add', -1)

    @State
    def esef_611_sword2():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
        sprite('null', 21)	# 1-21
        Unknown4003('657365665f36313173776f7264322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 30)	# 22-51
        Unknown3004(-16)

    @State
    def esef_611_sword2_add():

        def upon_IMMEDIATE():
            Unknown3033()
        sprite('null', 21)	# 1-21
        Unknown4003('657365665f36313173776f7264325f6164642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 30)	# 22-51
        Unknown3004(-16)

    @State
    def esef_611_particle():

        def upon_IMMEDIATE():
            Unknown4061(4)
            Unknown3038(1)
        sprite('esef611_particle', 14)	# 1-14
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        sprite('esef611_particle', 7)	# 15-21
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        sprite('esef611_particle', 7)	# 22-28
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        sprite('esef611_particle', 7)	# 29-35
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        sprite('esef611_particle', 7)	# 36-42
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')

    @State
    def esef_611_es_add():

        def upon_IMMEDIATE():
            Unknown4007(2)
            Unknown4061(4)
            Unknown3033()
            Unknown23015(11)
        sprite('esef611_07', 7)	# 1-7
        Unknown3001(0)
        Unknown3004(18)
        sprite('esef611_08', 7)	# 8-14
        sprite('esef611_09', 7)	# 15-21
        sprite('esef611_10', 7)	# 22-28
        sprite('esef611_11', 7)	# 29-35
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown3004(-12)
        sprite('esef611_11', 7)	# 36-42
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        sprite('esef611_11', 7)	# 43-49
        Unknown4054(12)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')

    @State
    def esef_404_kick_BDD():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4007(2)
            Unknown4009(2)
            callSubroutine('Zanzou')
            Unknown1007(-40000)
        sprite('vresef404_00', 5)	# 1-5
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
        sprite('vresef404_01', 4)	# 6-9
        Unknown4007(0)
        sprite('vresef404_02', 8)	# 10-17
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')

    @State
    def AstralHeat_Camera():

        def upon_IMMEDIATE():
            Unknown20000(1)
            Unknown20003(1)
            Unknown4011(3)
            Unknown4010(3)
            Unknown4008(3)

            def upon_43():
                if (SLOT_48 == 130):
                    sendToLabel(0)
                if (SLOT_48 == 131):
                    sendToLabel(1)
                if (SLOT_48 == 132):
                    sendToLabel(2)
                if (SLOT_48 == 133):
                    sendToLabel(3)
                if (SLOT_48 == 134):
                    sendToLabel(4)
        sprite('null', 32767)	# 1-32767
        label(0)
        sprite('null', 2)	# 32768-32769
        Unknown20009(950)
        sprite('null', 2)	# 32770-32771
        Unknown20009(900)
        sprite('null', 2)	# 32772-32773
        Unknown20009(850)
        sprite('null', 2)	# 32774-32775
        Unknown20009(800)
        sprite('null', 2)	# 32776-32777
        Unknown20009(750)
        sprite('null', 32767)	# 32778-65544
        Unknown20009(700)
        label(1)
        sprite('null', 2)	# 65545-65546
        Unknown20009(750)
        teleportRelativeX(30000)
        sprite('null', 2)	# 65547-65548
        Unknown20009(800)
        teleportRelativeX(30000)
        sprite('null', 2)	# 65549-65550
        Unknown20009(850)
        teleportRelativeX(30000)
        Unknown1007(300000)
        sprite('null', 2)	# 65551-65552
        Unknown20009(900)
        teleportRelativeX(30000)
        Unknown1007(50000)
        sprite('null', 2)	# 65553-65554
        Unknown20009(950)
        teleportRelativeX(30000)
        Unknown1007(50000)
        sprite('null', 2)	# 65555-65556
        Unknown20009(1000)
        teleportRelativeX(30000)
        Unknown1007(50000)
        sprite('null', 2)	# 65557-65558
        Unknown20009(1100)
        teleportRelativeX(30000)
        Unknown1007(50000)
        sprite('null', 2)	# 65559-65560
        Unknown20009(1200)
        teleportRelativeX(30000)
        Unknown1007(50000)
        sprite('null', 44)	# 65561-65604
        Unknown20009(1300)
        teleportRelativeX(30000)
        Unknown1007(50000)
        sprite('null', 2)	# 65605-65606
        Unknown1007(100000)
        sprite('null', 2)	# 65607-65608
        Unknown1007(100000)
        sprite('null', 2)	# 65609-65610
        Unknown1007(100000)
        sprite('null', 2)	# 65611-65612
        Unknown1007(100000)
        sprite('null', 10)	# 65613-65622
        Unknown1007(100000)
        sprite('null', 2)	# 65623-65624
        Unknown1007(100000)
        sprite('null', 2)	# 65625-65626
        Unknown1007(100000)
        sprite('null', 1000)	# 65627-66626
        Unknown1007(100000)
        loopRest()
        gotoLabel(4)
        label(2)
        sprite('null', 1000)	# 66627-67626
        Unknown20001(1)
        Unknown1000(-880000)
        teleportRelativeY(1500000)
        loopRest()
        gotoLabel(4)
        label(3)
        sprite('null', 2)	# 67627-67628
        sprite('null', 6)	# 67629-67634
        Unknown4009(2)
        Unknown20001(0)
        physicsXImpulse(170000)
        physicsYImpulse(-220000)
        sprite('null', 1000)	# 67635-68634
        Unknown4009(0)
        Unknown1084(1)
        label(4)
        sprite('null', 1)	# 68635-68635
        Unknown20000(0)
        Unknown20003(0)
        Unknown20009(1000)

    @State
    def EMB_ES_AH():

        def upon_IMMEDIATE():
            Unknown2007()
            Unknown3033()
            Unknown1096(1500)
            Unknown1007(273000)
            Unknown2054(1)
            Unknown4003('65665f656d625f65732e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown23015(5)
        sprite('null', 10)	# 1-10
        Unknown3026(-16777216)
        Unknown3025(-65536, 10)
        sprite('null', 10)	# 11-20
        Unknown3025(-55256, 10)
        sprite('null', 10)	# 21-30
        Unknown3025(-19276, 10)
        sprite('null', 10)	# 31-40
        Unknown3025(-65536, 10)
        sprite('null', 80)	# 41-120

    @State
    def esef_430EffSlash():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown1096(2500)
        sprite('null', 4)	# 1-4
        Unknown3001(0)
        Unknown3004(63)
        GFX_0('esef_430EffSlashAdd', -1)
        Unknown4003('657365665f3435305f736c6d30300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 5-7
        Unknown4003('657365665f3435305f736c6d30310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 8-10
        Unknown4003('657365665f3435305f736c6d30320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 4)	# 11-14
        Unknown4003('657365665f3435305f736c6d30330000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 15-17
        Unknown4003('657365665f3435305f736c6d30340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 18-20
        Unknown4003('657365665f3435305f736c6d30350000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 21-23
        Unknown4003('657365665f3435305f736c6d30360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 10)	# 24-33
        Unknown4003('657365665f3435305f736c6d30370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 30)	# 34-63
        Unknown3004(-8)
        GFX_0('esef_430EffNokosi', -1)

    @State
    def esef_430EffNokosi():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown2054(1)
            Unknown4007(2)
            Unknown3038(1)
        sprite('vresef450_ParitclePos', 1)	# 1-1
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000000000000')
        sprite('vresef450_ParitclePos', 1)	# 2-2
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000001000000')
        GFX_0('esef_CmnMg', 1)
        sprite('vresef450_ParitclePos', 1)	# 3-3
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000002000000')
        sprite('vresef450_ParitclePos', 1)	# 4-4
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000003000000')
        GFX_0('esef_CmnMg', 3)
        sprite('vresef450_ParitclePos', 1)	# 5-5
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000004000000')
        sprite('vresef450_ParitclePos', 1)	# 6-6
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000005000000')
        GFX_0('esef_CmnMg', 5)
        sprite('vresef450_ParitclePos', 1)	# 7-7
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000006000000')
        sprite('vresef450_ParitclePos', 1)	# 8-8
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000007000000')
        GFX_0('esef_CmnMg', 7)
        sprite('vresef450_ParitclePos', 1)	# 9-9
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000008000000')
        sprite('vresef450_ParitclePos', 1)	# 10-10
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e676172617373000000000000000000000000000000000009000000')
        sprite('vresef450_ParitclePos', 1)	# 11-11
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000a000000')
        sprite('vresef450_ParitclePos', 1)	# 12-12
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000b000000')
        sprite('vresef450_ParitclePos', 1)	# 13-13
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000c000000')
        sprite('vresef450_ParitclePos', 1)	# 14-14
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e67617261737300000000000000000000000000000000000d000000')

    @State
    def esef_CmnMg():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown21010(1)
            Unknown3001(255)
            Unknown1070(-200, 200)
            Unknown4003('657365665f636d6e6566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 60)	# 1-60
        Unknown1067(20)
        Unknown3004(-4)

    @State
    def esef_BuffMg():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown21010(1)
            Unknown3001(255)
            Unknown1010(-50000, 50000)
            Unknown1011(0, 200000)
            Unknown1070(-100, 100)
            Unknown4003('657365665f636d6e6566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1096(400)
            Unknown23015(11)
        sprite('null', 10)	# 1-10
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f636d6e6761726173730000000000000000000000000000000000ffffffff')
        Unknown3001(0)
        Unknown3004(51)
        physicsYImpulse(4000)
        sprite('null', 20)	# 11-30
        Unknown3004(-12)

    @State
    def esef_430EffSlashAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4013(2)
        sprite('null', 4)	# 1-4
        Unknown3001(0)
        Unknown3004(8)
        Unknown4003('657365665f3435305f736c6d30300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 5-7
        Unknown4003('657365665f3435305f736c6d30310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 8-10
        Unknown4003('657365665f3435305f736c6d30320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 4)	# 11-14
        Unknown4003('657365665f3435305f736c6d30330000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 15-17
        Unknown4003('657365665f3435305f736c6d30340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 18-20
        Unknown4003('657365665f3435305f736c6d30350000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 3)	# 21-23
        Unknown4003('657365665f3435305f736c6d30360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 10)	# 24-33
        Unknown4003('657365665f3435305f736c6d30370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 10)	# 34-43
        Unknown3004(-25)

    @State
    def esef_430EffBG():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4023(3)
            Unknown4003('657365665f3435305f42473030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1056(3000)
            Unknown1064(3200)
            Unknown1088(3000)
            Unknown1007(-10000)

            def upon_43():
                if (SLOT_48 == 135):
                    sendToLabel(0)
                if (SLOT_48 == 136):
                    sendToLabel(1)
        sprite('null', 30)	# 1-30
        Unknown3001(0)
        Unknown3004(8)
        sprite('null', 32767)	# 31-32797
        Unknown3004(0)
        label(0)
        sprite('null', 10)	# 32798-32807
        Unknown3004(-14)
        sprite('null', 32767)	# 32808-65574
        Unknown3004(0)
        label(1)
        sprite('null', 1)	# 65575-65575

    @State
    def esef_430EffBGAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4023(3)
            Unknown4003('657365665f3435305f42473030616464000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1056(3000)
            Unknown1064(3200)
            Unknown1088(3000)
            Unknown1007(-10000)

            def upon_43():
                if (SLOT_48 == 137):
                    sendToLabel(0)
        sprite('null', 30)	# 1-30
        Unknown3001(0)
        Unknown3004(8)
        sprite('null', 32767)	# 31-32797
        Unknown3004(0)
        label(0)
        sprite('null', 10)	# 32798-32807
        Unknown3004(-25)

    @State
    def esef_450ChangeSordEff():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown4010(2)
            Unknown4007(3)
            Unknown1064(1000)
            Unknown1056(1500)
            Unknown1073(30000)
            Unknown4003('657365665f3435305f70617267653030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1007(60000)
            teleportRelativeX(30000)
        sprite('null', 10)	# 1-10
        GFX_0('esef_450ChangeSordEffC', -1)
        sprite('null', 29)	# 11-39
        Unknown3004(-9)

    @State
    def esef_450ChangeSordEffC():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4010(2)
            Unknown4007(3)
            Unknown4006(2)
            Unknown1064(1000)
            Unknown4003('657365665f3435305f70617267653030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 5)	# 1-5
        sprite('null', 5)	# 6-10
        Unknown3004(-51)

    @State
    def esef_430EffAtkSlash():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            GFX_2('eseff_431_slash')
            Unknown1007(200000)
        sprite('null', 60)	# 1-60
        GFX_0('esef_430EffAtkSlashC', -1)
        ScreenShake(10000, 10000)

    @State
    def esef_430EffAtkSlashC():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4003('657365665f3435305f736c6173683030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1064(1200)
        sprite('null', 10)	# 1-10
        sprite('null', 20)	# 11-30
        Unknown3004(-12)

    @State
    def esef_430EffAasiba():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown23015(15)
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4003('657365665f3435305f61736962613030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1096(2000)
        sprite('null', 15)	# 1-15
        GFX_0('esef_430EffAasibaAdd', -1)
        sprite('null', 4)	# 16-19
        Unknown1099(300)
        Unknown3004(-13)
        Unknown4047(241, 241, 240)
        Unknown4045('65736566665f636d6e6761726173730000000000000000000000000000000000ffffffff')
        sprite('null', 15)	# 20-34
        Unknown1099(100)

    @State
    def esef_430EffAasibaAdd():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown23015(15)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4003('657365665f3435305f61736962613030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4007(2)
            Unknown4013(2)
            Unknown4006(2)
        sprite('null', 15)	# 1-15
        Unknown3004(-12)
        sprite('null', 5)	# 16-20
        Unknown1099(300)

    @State
    def esef_430EffCutIn():

        def upon_IMMEDIATE():
            Unknown4061(0)
            Unknown2054(1)
            Unknown4010(2)
            teleportRelativeX(200000)
            Unknown1007(140000)
            Unknown23015(1)
            Unknown3029(1)
        sprite('es450cutin_00', 4)	# 1-4	 **attackbox here**
        GFX_0('esef_430EffBG2', -1)
        ScreenShake(10000, 10000)
        physicsXImpulse(60000)
        physicsYImpulse(-30000)
        GFX_0('esef_430EffCutInSpeed', 0)
        Unknown36(1)
        Unknown1007(500000)
        Unknown1097(300)
        Unknown35()
        GFX_0('esef_430EffCutInSpeed', 1)
        Unknown36(1)
        Unknown1007(-400000)
        Unknown35()
        SFX_0('000_airdash_0')
        sprite('es450cutin_00', 32767)	# 5-32771	 **attackbox here**
        physicsXImpulse(1000)
        physicsYImpulse(-500)

    @State
    def esef_430EffCutInSpeed():

        def upon_IMMEDIATE():
            Unknown4061(0)
            Unknown2054(1)
            Unknown4010(2)
            Unknown4054(4)
            Unknown23067('eseff_450_cutin_speed')
            Unknown1072(33000)
            Unknown1096(1500)
        sprite('null', 32767)	# 1-32767

    @State
    def esef_430EffBG2():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4003('657365665f3435305f42473031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1096(2000)
            Unknown1065(300)
            Unknown1007(10000)
            teleportRelativeX(100000)
            Unknown1073(35000)
        sprite('null', 6)	# 1-6
        Unknown3001(0)
        sprite('null', 8)	# 7-14
        Unknown3004(31)
        sprite('null', 32767)	# 15-32781
        Unknown3004(0)

    @State
    def esef_450SlashLast():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4003('657365665f3435305f6c617374736c61736830300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1073(35000)
            Unknown1096(900)
            Unknown1000(-1269000)
            teleportRelativeY(1490000)
            Unknown4009(2)
        sprite('null', 7)	# 1-7
        Unknown4061(4)
        Unknown4047(241, 241, 241)
        Unknown4048(35000)
        Unknown4045('65736566665f3435305f666c6173680000000000000000000000000000000000ffffffff')
        GFX_0('esef_450EffLastSlashNigiyakasi', -1)
        sprite('null', 8)	# 8-15
        physicsXImpulse(130000)
        physicsYImpulse(-90000)
        sprite('null', 20)	# 16-35
        Unknown1084(1)
        sprite('null', 60)	# 36-95
        ScreenShake(20000, 20000)
        Unknown3001(0)

    @State
    def esef_450EffLastSlashNigiyakasi():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(4)
            Unknown21004(241)
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('657365665f3435305f736c6173683030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1064(1200)
        sprite('null', 5)	# 1-5
        Unknown3001(0)
        sprite('null', 10)	# 6-15
        Unknown3004(26)
        sprite('null', 10)	# 16-25
        sprite('null', 20)	# 26-45
        Unknown3004(-12)

    @State
    def esef_450EffEmb():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4003('657365665f3435305f656d6230300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            teleportRelativeX(-200000)
            Unknown1007(200000)
            Unknown2005()
        sprite('null', 1)	# 1-1
        Unknown4045('65736566665f3435305f666c6173683200000000000000000000000000000000ffffffff')
        label(0)
        sprite('null', 5)	# 2-6
        ScreenShake(800, 800)
        gotoLabel(0)

    @State
    def esef_450EffWing():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4003('657365665f3435305f77696e67303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown23015(2)
            Unknown1096(1000)
            GFX_0('esef_450EffWingSub', -1)
            Unknown3038(1)
            SFX_3('esse_12')
        label(0)
        sprite('vresef450_ParitclePos2', 5)	# 1-5
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000000000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000001000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000002000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000003000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000004000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000005000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000006000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000007000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000008000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f747961303000000000000000000000000000000009000000')
        Unknown4054(13)
        Unknown4045('65736566665f3435305f676f74796130300000000000000000000000000000000a000000')
        Unknown1097(2)
        sprite('vresef450_ParitclePos2', 5)	# 6-10
        Unknown1097(2)
        sprite('vresef450_ParitclePos2', 5)	# 11-15
        Unknown1097(2)
        sprite('vresef450_ParitclePos2', 5)	# 16-20
        Unknown1097(2)
        gotoLabel(0)

    @State
    def esef_450EffWingAdd():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4003('657365665f3435305f77696e67303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown23015(2)
            Unknown1096(1000)
            Unknown3038(1)

            def upon_43():
                if (SLOT_48 == 138):
                    sendToLabel(1)
        label(0)
        sprite('null', 5)	# 1-5
        Unknown3001(0)
        Unknown1097(2)
        gotoLabel(0)
        label(1)
        sprite('null', 5)	# 6-10
        Unknown3004(4)
        gotoLabel(1)

    @State
    def esef_450EffWingSub():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4010(2)
            Unknown4003('657365665f3435305f77696e67303073756200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown23015(6)
            Unknown1096(1000)
        label(0)
        sprite('null', 10)	# 1-10
        Unknown3001(75)
        Unknown1096(1000)
        sprite('null', 10)	# 11-20
        Unknown3001(0)
        sprite('null', 5)	# 21-25
        Unknown3001(75)
        sprite('null', 5)	# 26-30
        Unknown3001(0)
        gotoLabel(0)

    @State
    def esef_450EffBGClash():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4003('657365665f3435305f42473032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown23015(2)
            Unknown1064(1300)
            Unknown1056(3000)
            Unknown3001(200)
            Unknown1007(-115000)
            SFX_3('esse_13')
        sprite('null', 32767)	# 1-32767

    @State
    def esef_450EffBGLast():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown2054(1)
            Unknown4003('657365665f3435305f42473033000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1064(850)
            Unknown3001(255)
            Unknown1007(-15000)
        sprite('null', 32767)	# 1-32767

    @State
    def esef_450EffClashA():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            GFX_2('eseff_450_clash00')
            Unknown23015(2)
            Unknown1096(800)
            Unknown1072(-65000)
        sprite('null', 150)	# 1-150
        Unknown1099(1)
        ScreenShake(20000, 20000)

    @State
    def esef_450EffClashB():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4010(2)
            GFX_2('eseff_450_clash00')
            Unknown23015(2)
            Unknown1096(500)
            Unknown1072(-100000)
        sprite('null', 150)	# 1-150
        Unknown1099(1)
        ScreenShake(20000, 20000)

    @State
    def esef_450EffClashC():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4010(2)
            GFX_2('eseff_450_clash00')
            Unknown23015(2)
            Unknown1096(600)
            Unknown1072(-25000)
        sprite('null', 150)	# 1-150
        Unknown1099(1)
        ScreenShake(20000, 20000)

    @State
    def esef_450EffClashAmove():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4010(2)
            GFX_2('eseff_450_clash00m')
            Unknown23015(2)
            Unknown1096(800)
            Unknown1072(-65000)
        sprite('null', 130)	# 1-130
        Unknown26('esef_450EffClashA')

    @State
    def esef_450EffClashBmove():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            Unknown4010(2)
            GFX_2('eseff_450_clash00m')
            Unknown23015(2)
            Unknown1096(500)
            Unknown1072(-100000)
        sprite('null', 130)	# 1-130
        Unknown26('esef_450EffClashB')

    @State
    def esef_450EffClashCmove():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4010(2)
            GFX_2('eseff_450_clash00m')
            Unknown23015(2)
            Unknown1096(800)
            Unknown1072(-25000)
        sprite('null', 130)	# 1-130
        Unknown26('esef_450EffClashC')

    @State
    def esef_450EffClash01():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4010(2)
            GFX_2('eseff_450_clash00')
            Unknown23015(2)
            Unknown1096(800)
            Unknown1007(180000)
            teleportRelativeX(-400000)
        sprite('null', 149)	# 1-149

    @State
    def esef_450EffClash01m():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown2054(1)
            Unknown4006(2)
            Unknown4010(2)
            Unknown4010(2)
            GFX_2('eseff_450_clash00m')
            Unknown23015(2)
            Unknown1096(800)
            Unknown1007(180000)
            teleportRelativeX(-400000)
        sprite('null', 100)	# 1-100

    @State
    def esef_450WhiteOut():

        def upon_IMMEDIATE():
            Unknown1000(260000)
            Unknown4010(2)
        sprite('null', 10)	# 1-10
        sprite('null', 200)	# 11-210
        Unknown4054(4)
        Unknown23067('eseff_450_flash3')

    @State
    def esef_450PaticleInf():

        def upon_IMMEDIATE():
            Unknown4010(2)
        sprite('null', 32767)	# 1-32767
        GFX_2('eseff_450_infwin')

    @State
    def esef_450SordLostMaso():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4007(3)
            Unknown4061(4)
        sprite('vresef615_whitesord', 100)	# 1-100
        Unknown3001(0)
        sprite('vresef615_whitesord', 40)	# 101-140
        Unknown3004(6)
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3435305f6d61736f6c6f7374000000000000000000000000000000000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3435305f6d61736f6c6f7374000000000000000000000000000001000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3435305f6d61736f6c6f7374000000000000000000000000000002000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3435305f6d61736f6c6f7374000000000000000000000000000003000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3435305f6d61736f6c6f7374000000000000000000000000000004000000')
        Unknown4047(241, 241, 241)
        Unknown4045('65736566665f3435305f6d61736f6c6f7374000000000000000000000000000005000000')
        sprite('vresef615_whitesord', 32767)	# 141-32907
