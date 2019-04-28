@State
def PLA_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('504c415f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PLA_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PLA_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PLA_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 200):
            Unknown23185('504c415f506572736f6e6135413474680000000000000000000000000000000032000000')
        if (SLOT_48 == 201):
            Unknown23185('504c415f506572736f6e6135420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 202):
            Unknown23185('504c415f506572736f6e613542326e640000000000000000000000000000000032000000')
        if (SLOT_48 == 205):
            Unknown23185('504c415f506572736f6e6135423372640000000000000000000000000000000032000000')
        if (SLOT_48 == 207):
            Unknown23185('504c415f506572736f6e6141697235430000000000000000000000000000000032000000')
        if (SLOT_48 == 400):
            Unknown23185('504c415f506572736f6e615461636b6c6500000000000000000000000000000032000000')
        if (SLOT_48 == 950):
            Unknown23185('504c415f506572736f6e614963686967656b690000000000000000000000000032000000')
        if (SLOT_48 == 300):
            Unknown23185('504c415f506572736f6e6153686f745f5441470000000000000000000000000032000000')
        if (SLOT_48 == 301):
            Unknown23185('504c415f506572736f6e614f72616f72615f544147000000000000000000000032000000')
        if (SLOT_48 == 1001):
            Unknown23185('504c415f506572736f6e614d6174636857696e0000000000000000000000000032000000')
        if (SLOT_48 == 121):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e670000000000000000000032000000')

@Subroutine
def PersonaReset():
    Unknown4061(1)
    Unknown23022(0)
    Unknown2053(0)
    Unknown23015(11)
    Unknown2019(-1)
    Unknown1084(1)
    Unknown4009(0)
    Unknown4008(0)
    Unknown4007(0)
    Unknown2017(0)
    Unknown30041('')
    Unknown3031()

@Subroutine
def PLA_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PLA_AttackInit():
    Unknown23028(1, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 100
    callSubroutine('PLA_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PLA_SPAttackInit():
    Unknown23028(2, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 110
    callSubroutine('PLA_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PLA_DDAttackInit():
    Unknown23028(3, 1)
    Unknown30037('')
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    Unknown11034(1)
    Unknown11033(0)
    SLOT_11 = 120
    callSubroutine('PLA_ReceptionSignal')
    Unknown23023()

@Subroutine
def PLA_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PLA_ForceWarp():
    SLOT_58 = 1
    Unknown3001(0)
    Unknown3004(85)
    loopRelated(17, 4)

    def upon_17():
        Unknown3001(255)
        Unknown3004(0)

@State
def PersonaDeleteAndIdling():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
    sprite('keep', 32767)	# 1-32767
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_3('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PLA_PersonaWait')

@State
def PersonaSummonEffect():
    sprite('null', 30)	# 1-30
    Unknown23015(13)
    Unknown4054(11)
    Unknown4045('706572736f6e615f73756d6d6f6e00000000000000000000000000000000000064000000')

@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)	# 1-30
    Unknown1007(288000)
    teleportRelativeX(112000)
    GFX_1('persona_summon_ply', 100)

@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PLA_ReceptionSignal')
    sprite('null', 30)	# 1-30
    Unknown2019(1)
    Unknown23053('190000000b000000')
    Unknown4061(1)
    Unknown3032()
    Unknown1059(-100)
    Unknown1067(150)
    Unknown3004(-20)
    Unknown23022(1)
    Unknown4054(11)
    Unknown4045('706572736f6e615f64656c65746500000000000000000000000000000000000064000000')
    Unknown2054(1)
    Unknown2017(0)
    Unknown1084(1)

@State
def laef_burner_loop():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_2('laef_burner')
    gotoLabel(0)

@State
def laef_burner_loop_reaction():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('null', 4)	# 1-4
    GFX_2('laef_burner')
    sprite('null', 4)	# 5-8
    GFX_2('laef_burner')
    sprite('null', 4)	# 9-12
    GFX_2('laef_burner')
    sprite('null', 4)	# 13-16
    GFX_2('laef_burner')
    sprite('null', 4)	# 17-20
    GFX_2('laef_burner')
    sprite('null', 4)	# 21-24
    GFX_2('laef_burner')
    sprite('null', 4)	# 25-28
    GFX_2('laef_burner')
    sprite('null', 4)	# 29-32
    GFX_2('laef_burner')
    sprite('null', 4)	# 33-36
    GFX_2('laef_burner')
    sprite('null', 4)	# 37-40
    GFX_2('laef_burner')
    sprite('null', 4)	# 41-44
    GFX_2('laef_burner')
    sprite('null', 4)	# 45-48
    GFX_2('laef_burner')
    sprite('null', 6)	# 49-54
    GFX_2('laef_burner')

@State
def laef001burner():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 16)	# 1-16
    GFX_0('laef_burner_loop_reaction', 100)
    Unknown1072(65000)
    Unknown1096(450)
    Unknown1099(50)
    sprite('null', 30)	# 17-46
    Unknown1099(0)
    sprite('null', 8)	# 47-54
    Unknown1099(-100)

@State
def laef001burner_add():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 64)	# 1-64
    Unknown1072(65000)
    Unknown23067('laef_burner_add001')

@State
def laef001burner2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 16)	# 1-16
    GFX_0('laef_burner_loop_reaction', 100)
    Unknown1072(35000)
    Unknown1096(450)
    Unknown1099(50)
    sprite('null', 30)	# 17-46
    Unknown1099(0)
    sprite('null', 8)	# 47-54
    Unknown1099(-100)

@State
def laef001burner2_add():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 64)	# 1-64
    Unknown1072(35000)
    Unknown23067('laef_burner_add001')

@State
def laef001burner3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 16)	# 1-16
    GFX_0('laef_burner_loop_reaction', 100)
    Unknown1072(15000)
    Unknown1096(450)
    Unknown1099(50)
    sprite('null', 30)	# 17-46
    Unknown1099(0)
    sprite('null', 8)	# 47-54
    Unknown1099(-100)

@State
def laef001burner3_add():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 64)	# 1-64
    Unknown1072(15000)
    Unknown23067('laef_burner_add001')

@State
def laef001burner4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 16)	# 1-16
    GFX_0('laef_burner_loop_reaction', 100)
    Unknown1072(-175000)
    Unknown1096(450)
    Unknown1099(50)
    sprite('null', 30)	# 17-46
    Unknown1099(0)
    sprite('null', 8)	# 47-54
    Unknown1099(-100)

@State
def laef001burner4_add():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 64)	# 1-64
    Unknown1072(-175000)
    Unknown23067('laef_burner_add001')

@State
def laef001burner5():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 16)	# 1-16
    GFX_0('laef_burner_loop_reaction', 100)
    Unknown1072(-150000)
    Unknown1096(450)
    Unknown1099(50)
    sprite('null', 30)	# 17-46
    Unknown1099(0)
    sprite('null', 8)	# 47-54
    Unknown1099(-100)

@State
def laef001burner5_add():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 64)	# 1-64
    Unknown1072(-120000)
    Unknown23067('laef_burner_add001')

@State
def laef001burner6():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 16)	# 1-16
    GFX_0('laef_burner_loop_reaction', 100)
    Unknown1072(-120000)
    Unknown1096(450)
    Unknown1099(50)
    sprite('null', 30)	# 17-46
    Unknown1099(0)
    sprite('null', 8)	# 47-54
    Unknown1099(-100)

@State
def laef001burner6_add():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 64)	# 1-64
    Unknown1072(-120000)
    Unknown23067('laef_burner_add001')

@State
def laef404burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4250)
    Unknown1072(60000)

@State
def laef404burner_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(60000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef404burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2500)
    Unknown1064(5000)
    Unknown1072(45000)

@State
def laef404burner2_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(45000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef404burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1750)
    Unknown1064(4000)
    Unknown1072(30000)

@State
def laef404burner3_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(30000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef405burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2250)
    Unknown1064(4500)
    Unknown1072(15000)

@State
def laef405burner_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(15000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef405burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2250)
    Unknown1064(4500)
    Unknown1072(0)

@State
def laef405burner2_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(0)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef405burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2250)
    Unknown1064(4500)
    Unknown1072(-10000)

@State
def laef405burner3_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(-10000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef430burner_start():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1750)
    Unknown1064(3500)
    Unknown1072(185000)

@State
def laef430burner_start_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(185000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef430burner2_start():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4750)
    Unknown1072(190000)

@State
def laef430burner2_start_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(190000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef430burner3_start():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2500)
    Unknown1064(5250)
    Unknown1072(210000)

@State
def laef430burner3_start_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(210000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef430burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2250)
    Unknown1064(2750)
    Unknown1072(120000)

@State
def laef430burner_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(120000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef430burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4500)
    Unknown1072(150000)

@State
def laef430burner2_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(150000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef430burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1750)
    Unknown1064(5000)
    Unknown1072(180000)

@State
def laef430burner3_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4048(180000)
    Unknown4045('6c6165665f6275726e65725f616464343035000000000000000000000000000064000000')
    gotoLabel(0)

@State
def laef432_10_burner4():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1072(255000)
    Unknown1064(4750)
    Unknown1056(2375)

@State
def laef432_10_burner5():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1072(270000)
    Unknown1064(4750)
    Unknown1056(2375)

@State
def laef432_10_burner6():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1072(280000)
    Unknown1064(4750)
    Unknown1056(2375)

@State
def laef432_11_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 20)	# 1-20
    GFX_0('laef_burner_loop', 100)
    Unknown1072(280000)
    Unknown1064(3000)
    Unknown1056(2500)
    sprite('null', 16)	# 21-36
    Unknown1059(-187)
    Unknown1067(-156)
    sprite('null', 1)	# 37-37
    Unknown1096(0)
    Unknown1099(0)

@State
def laef432_11_burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 20)	# 1-20
    GFX_0('laef_burner_loop', 100)
    Unknown1072(260000)
    Unknown1064(3000)
    Unknown1056(2500)
    sprite('null', 16)	# 21-36
    Unknown1059(-187)
    Unknown1067(-156)
    sprite('null', 1)	# 37-37
    Unknown1096(0)
    Unknown1099(0)

@State
def laef432_11_burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 20)	# 1-20
    GFX_0('laef_burner_loop', 100)
    Unknown1072(250000)
    Unknown1064(3000)
    Unknown1056(2500)
    sprite('null', 16)	# 21-36
    Unknown1059(-187)
    Unknown1067(-156)
    sprite('null', 1)	# 37-37
    Unknown1096(0)
    Unknown1099(0)

@State
def laef432_11_burner4():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 20)	# 1-20
    GFX_0('laef_burner_loop', 100)
    Unknown1072(60000)
    Unknown1096(1500)
    sprite('null', 16)	# 21-36
    Unknown1099(-93)
    sprite('null', 1)	# 37-37
    Unknown1096(0)
    Unknown1099(0)

@State
def laef432_11_burner5():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 20)	# 1-20
    GFX_0('laef_burner_loop', 100)
    Unknown1072(80000)
    Unknown1096(1500)
    sprite('null', 16)	# 21-36
    Unknown1099(-93)
    sprite('null', 1)	# 37-37
    Unknown1096(0)
    Unknown1099(0)

@State
def laef432_11_burner6():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 20)	# 1-20
    GFX_0('laef_burner_loop', 100)
    Unknown1072(100000)
    Unknown1096(1500)
    sprite('null', 16)	# 21-36
    Unknown1099(-93)
    sprite('null', 1)	# 37-37
    Unknown1096(0)
    Unknown1099(0)

@State
def laef600burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4000)
    Unknown1072(-45000)

@State
def laef600burner_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
    label(0)
    sprite('null', 1)	# 1-1
    GFX_1('laef_burner_add600', 100)
    gotoLabel(0)

@State
def laef600burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4000)
    Unknown1072(-60000)

@State
def laef600burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4000)
    Unknown1072(-90000)

@State
def laef600burner4():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(4000)
    Unknown1072(-30000)

@State
def laef600burner_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(50000)

@State
def laef600burner2_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(70000)

@State
def laef600burner3_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(90000)

@State
def laef600burner4_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(20000)

@State
def laef600burner_c():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(65000)

@State
def laef600burner2_c():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(95000)

@State
def laef600burner3_c():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(120000)

@State
def laef600burner4_c():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(35000)

@State
def laef600_wing():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(0)
        Unknown3032()
    sprite('vr_la600_w00', 32767)	# 1-32767
    physicsXImpulse(-8000)
    physicsYImpulse(12000)
    GFX_0('laef600burner_wing', 0)
    GFX_0('laef600burner_wing2', 1)
    GFX_0('laef600burner_wing3', 2)
    GFX_0('laef600burner_wing4', 3)

@State
def laef600burner_wing():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(60000)

@State
def laef600burner_wing2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(80000)

@State
def laef600burner_wing3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(105000)

@State
def laef600burner_wing4():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1072(50000)

@State
def laef600_axe():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(0)
        Unknown3032()
    sprite('vr_la600_w10', 32)	# 1-32
    Unknown1007(512000)
    physicsYImpulse(-16000)
    sprite('vr_la600_w11', 4)	# 33-36
    physicsYImpulse(0)
    sprite('vr_la600_w12', 4)	# 37-40
    sprite('vr_la600_w13', 4)	# 41-44

@State
def laef_win2_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1072(-35000)

@State
def laef_win2_burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1072(-60000)

@State
def laef_win2_burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1072(-90000)

@State
def laef_win2_burner_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1250)
    Unknown1064(2500)
    Unknown1072(180000)

@State
def laef_win2_burner_b2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1375)
    Unknown1064(2750)
    Unknown1072(180000)

@State
def laef_win2_burner_b3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(1500)
    Unknown1064(3000)
    Unknown1072(180000)

@State
def axe_level2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown1007(-24000)

        def upon_STATE_END():
            SLOT_6 = 2
    sprite('null', 16)	# 1-16
    GFX_2('laef_axe_level2')

@State
def axe_level3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown1007(-24000)

        def upon_STATE_END():
            SLOT_6 = 3
    sprite('null', 16)	# 1-16
    GFX_2('laef_axe_level3')

@State
def axe_level4():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown1007(-24000)

        def upon_STATE_END():
            SLOT_6 = 4
    sprite('null', 16)	# 1-16
    GFX_2('laef_axe_level4')

@State
def axe_level5():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown1007(-24000)

        def upon_STATE_END():
            SLOT_6 = 5
    sprite('null', 16)	# 1-16
    GFX_2('laef_axe_level5')

@State
def hibana2AB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('6c6165665f3231316173686962616e615f30302e4449470000000000000000006c6165665f3231316173686962616e615f30305f3030302e6d6d6f7400000000')
        Unknown4015()
        Unknown3001(0)
        teleportRelativeX(20000)
    sprite('null', 18)	# 1-18
    Unknown3004(51)
    GFX_1('laef_asismoke_sm2', 100)
    GFX_1('agef_kickhibana_00', 100)
    GFX_0('hibana2ABa', 100)

@State
def hibana2ABa():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
    sprite('null', 2)	# 1-2
    sprite('null', 2)	# 3-4
    GFX_0('hibana2ABb', 100)
    sprite('null', 2)	# 5-6
    GFX_0('hibana2ABb', 100)
    sprite('null', 1)	# 7-7
    GFX_0('hibana2ABb', 100)
    sprite('null', 8)	# 8-15
    GFX_0('hibana2ABc', 100)

@State
def hibana2ABb():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4003('6c6165665f3231316173686962616e615f30312e4449470000000000000000006c6165665f3231316173686962616e615f30315f3030302e6d6d6f7400000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 18)	# 1-18
    Unknown3004(51)

@State
def hibana2ABc():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(3)
        Unknown4003('6c6165665f3231316173686962616e615f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(60000)
    sprite('null', 15)	# 1-15
    Unknown3004(-17)

@State
def PLA_Persona5A4th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000006079feff000000006079feff00000000')
        callSubroutine('PLA_AttackInit')
        callSubroutine('PLA_CheckWarp')
    sprite('lp406_05', 6)	# 1-6
    GFX_0('406setlope', 100)
    sprite('lp406_06', 6)	# 7-12
    sprite('lp406_07', 6)	# 13-18
    Unknown21015('3430366269726477696e67000000000000000000000000000000000000000000de00000000000000')
    SFX_3('cloth_l')
    sprite('lp406_08', 6)	# 19-24
    sprite('lp406_09', 6)	# 25-30
    sprite('lp406_07', 6)	# 31-36
    SFX_3('cloth_m')
    sprite('lp406_08', 6)	# 37-42
    sprite('lp406_09', 6)	# 43-48
    sprite('lp406_07', 6)	# 49-54
    sprite('lp406_08', 6)	# 55-60
    sprite('lp406_09', 6)	# 61-66
    sprite('keep', 32767)	# 67-32833
    enterState('PersonaDeleteAndIdling')
    loopRest()
    ExitState()
    label(2)
    sprite('lp406_07', 6)	# 32834-32839
    sprite('lp406_08', 6)	# 32840-32845
    sprite('lp406_09', 6)	# 32846-32851
    sprite('lp406_07', 6)	# 32852-32857
    sprite('lp406_08', 6)	# 32858-32863
    sprite('lp406_09', 6)	# 32864-32869
    sprite('lp406_07', 7)	# 32870-32876
    sprite('lp406_08', 7)	# 32877-32883
    sprite('lp406_09', 7)	# 32884-32890
    sprite('lp406_07', 8)	# 32891-32898
    sprite('lp406_08', 8)	# 32899-32906
    sprite('lp406_09', 8)	# 32907-32914
    sprite('keep', 32767)	# 32915-65681
    enterState('PersonaDeleteAndIdling')

@State
def PLA_Persona5B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000b03cffff00000000b03cffff00000000')
        callSubroutine('PLA_AttackInit')
        callSubroutine('PLA_ForceWarp')
        Unknown4007(3)
        Unknown2017(0)
        setInvincible(1)
        Unknown22019('0100000000000000000000000000000000000000')
    sprite('lp232_00', 3)	# 1-3
    sprite('lp232_01', 3)	# 4-6
    SFX_3('la000')
    GFX_0('232uzu', 100)
    GFX_0('232handeff', 100)
    GFX_0('232atk', 100)
    sprite('lp232_02', 3)	# 7-9
    GFX_0('232atk', 100)
    sprite('lp232_00', 3)	# 10-12
    sprite('lp232_03', 3)	# 13-15
    GFX_0('vr_lp232atk', 100)
    sprite('lp232_04', 3)	# 16-18
    sprite('lp232_05', 3)	# 19-21
    sprite('lp232_06', 4)	# 22-25
    SFX_3('cloth_l')
    setInvincible(0)
    sprite('lp232_07', 4)	# 26-29
    sprite('lp232_08', 4)	# 30-33
    sprite('lp232_06', 4)	# 34-37
    SFX_3('cloth_l')
    sprite('lp232_07', 4)	# 38-41
    sprite('lp232_08', 4)	# 42-45
    sprite('keep', 32767)	# 46-32812
    enterState('PersonaDeleteAndIdling')

@State
def PLA_Persona5B2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff000000006079feffa08601006079feffa0860100')
        callSubroutine('PLA_AttackInit')
        callSubroutine('PLA_CheckWarp')
        Unknown4007(3)
        Unknown2017(0)
    sprite('lp205_00', 3)	# 1-3
    GFX_0('Cmnrasen', 100)
    sprite('lp205_01', 3)	# 4-6
    sprite('lp205_02', 3)	# 7-9
    GFX_0('205birdwing', 100)
    GFX_0('205bird', 100)
    sprite('lp205_03', 3)	# 10-12
    sprite('lp205_04', 3)	# 13-15
    sprite('lp205_05', 3)	# 16-18
    sprite('lp205_06', 3)	# 19-21
    sprite('lp205_07', 4)	# 22-25
    SFX_3('cloth_m')
    sprite('lp205_08', 4)	# 26-29
    sprite('lp205_09', 4)	# 30-33
    sprite('lp205_07', 4)	# 34-37
    sprite('lp205_08', 4)	# 38-41
    sprite('lp205_09', 4)	# 42-45
    sprite('lp205_07', 4)	# 46-49
    SFX_3('cloth_m')
    sprite('lp205_08', 4)	# 50-53
    sprite('lp205_09', 4)	# 54-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PLA_Persona5B3rd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff000000006079feffa08601006079feffa0860100')
        callSubroutine('PLA_AttackInit')
        callSubroutine('PLA_CheckWarp')
    sprite('lp206_00', 4)	# 1-4
    SFX_3('la000')
    GFX_0('206birdwing_anim', 100)
    sprite('lp206_01', 4)	# 5-8
    sprite('lp206_02', 4)	# 9-12
    GFX_0('206birdwing', 100)
    GFX_0('206bird', 100)
    sprite('lp206_03', 4)	# 13-16
    sprite('lp206_04', 4)	# 17-20
    sprite('lp206_05', 4)	# 21-24
    sprite('lp206_06', 4)	# 25-28
    SFX_3('cloth_m')
    sprite('lp206_07', 4)	# 29-32
    sprite('lp206_08', 4)	# 33-36
    sprite('lp206_06', 4)	# 37-40
    sprite('lp206_07', 4)	# 41-44
    sprite('lp206_08', 4)	# 45-48
    sprite('lp206_06', 4)	# 49-52
    SFX_3('cloth_m')
    sprite('lp206_07', 4)	# 53-56
    sprite('lp206_08', 4)	# 57-60
    sprite('lp206_06', 4)	# 61-64
    sprite('lp206_07', 4)	# 65-68
    sprite('lp206_08', 4)	# 69-72
    sprite('lp206_06', 4)	# 73-76
    sprite('lp206_07', 4)	# 77-80
    sprite('lp206_08', 4)	# 81-84
    sprite('lp206_06', 4)	# 85-88
    sprite('lp206_07', 4)	# 89-92
    sprite('lp206_08', 4)	# 93-96
    sprite('keep', 32767)	# 97-32863
    enterState('PersonaDeleteAndIdling')

@State
def PLA_PersonaAir5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000b03cffff00000000b03cffff00000000b03cffff')
        callSubroutine('PLA_AttackInit')
        callSubroutine('PLA_ForceWarp')
        Unknown4007(3)
        Unknown2017(0)
    sprite('lp254_00', 3)	# 1-3
    GFX_0('254atk', 100)
    GFX_0('254circle', 1)
    SFX_3('la000')
    sprite('lp254_01', 3)	# 4-6
    sprite('lp254_02', 1)	# 7-7
    GFX_0('vr_lp254atk', 100)
    SFX_3('cloth_m')
    sprite('lp254_02', 7)	# 8-14
    sprite('lp254_03', 6)	# 15-20
    sprite('lp254_04', 6)	# 21-26
    sprite('lp254_02', 6)	# 27-32
    Unknown4007(0)
    sprite('lp254_03', 6)	# 33-38
    sprite('lp254_04', 6)	# 39-44
    sprite('lp254_02', 6)	# 45-50
    SFX_3('cloth_m')
    sprite('lp254_03', 6)	# 51-56
    sprite('lp254_04', 6)	# 57-62
    sprite('lp254_02', 6)	# 63-68
    sprite('lp254_03', 6)	# 69-74
    sprite('lp254_04', 6)	# 75-80
    sprite('keep', 32767)	# 81-32847
    enterState('PersonaDeleteAndIdling')

@State
def PLA_PersonaTackle():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000803801000000000080380100000000008038010000000000')
        callSubroutine('PLA_DDAttackInit')
        callSubroutine('PLA_ForceWarp')
        Unknown4007(3)
        Unknown2011()
        AttackLevel_(5)
        Damage(1000)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(3)
        AirUntechableTime(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(50000)
        AirPushbackX(25000)
        PushbackX(20000)
        Hitstop(20)
        Unknown11084(1)
        Unknown2017(0)
        Unknown11072(1, 200000, 0)
        Unknown11001(0, 0, 0)

        def upon_43():
            if (SLOT_48 == 401):
                sendToLabel(1)
            if (SLOT_48 == 404):
                sendToLabel(3)
            if (SLOT_48 == 402):
                Unknown23027()
                Unknown4007(0)
                Unknown4009(0)
                physicsXImpulse(60000)
            if (SLOT_48 == 406):
                Hitstop(45)
                AirPushbackX(50000)
                Unknown23182(3)
                AttackP2(60)
                Unknown11092(1)
        GFX_0('430Ptackle_start', 100)

        def upon_11():
            Unknown23029(3, 405, 0)

        def upon_78():
            Unknown23027()
            Unknown23029(3, 408, 0)
        setInvincible(1)
        Unknown23078(1)
    label(0)
    sprite('lp430_00', 4)	# 1-4
    SFX_3('la000')
    sprite('lp430_01', 4)	# 5-8
    sprite('lp430_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lp430_03', 4)	# 13-16
    SFX_3('la006')
    GuardPoint_(1)
    sprite('lp430_04', 4)	# 17-20
    sprite('lp430_05', 4)	# 21-24
    sprite('lp430_06', 3)	# 25-27	 **attackbox here**
    GFX_0('430tackleatk', 100)
    SFX_3('slash_blade_slow')
    label(9)
    sprite('lp430_07', 3)	# 28-30	 **attackbox here**
    sprite('lp430_08', 3)	# 31-33	 **attackbox here**
    sprite('lp430_06', 3)	# 34-36	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(3)
    sprite('keep', 32767)	# 37-32803
    enterState('PersonaDeleteAndIdling')

@State
def PLA_PersonaOraora_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PLA_SPAttackInit')
        callSubroutine('PLA_ForceWarp')
        Unknown4007(3)
    sprite('lp433_00', 6)	# 1-6
    GFX_0('Cmnrasen', 0)
    GFX_0('433lopecore', 100)
    SFX_3('la000')
    sprite('lp433_01', 6)	# 7-12
    sprite('lp433_02', 6)	# 13-18
    sprite('lp433_03', 6)	# 19-24
    sprite('lp433_04', 6)	# 25-30
    SFX_3('cut_m')
    sprite('lp433_05', 6)	# 31-36
    SFX_3('cut_m')
    sprite('lp433_06', 6)	# 37-42
    sprite('lp433_07', 6)	# 43-48
    sprite('lp433_08', 6)	# 49-54
    sprite('lp433_09', 6)	# 55-60
    sprite('lp433_10', 6)	# 61-66
    GFX_0('433ringatk', 100)
    sprite('lp433_11', 6)	# 67-72
    sprite('lp433_12', 6)	# 73-78
    Unknown7007('6c613332320000000000000000000000640000006c6133323400000000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('lp433_13', 6)	# 79-84
    SFX_3('cloth_l')
    sprite('lp433_14', 6)	# 85-90
    sprite('lp433_15', 6)	# 91-96
    sprite('lp433_13', 6)	# 97-102
    sprite('lp433_14', 6)	# 103-108
    sprite('lp433_15', 6)	# 109-114
    sprite('lp433_13', 6)	# 115-120
    SFX_3('cloth_l')
    sprite('lp433_14', 6)	# 121-126
    sprite('lp433_15', 6)	# 127-132
    sprite('lp433_13', 6)	# 133-138
    sprite('lp433_14', 6)	# 139-144
    sprite('lp433_15', 6)	# 145-150
    sprite('lp433_13', 6)	# 151-156
    SFX_3('cloth_m')
    sprite('lp433_14', 6)	# 157-162
    sprite('lp433_15', 6)	# 163-168
    sprite('lp433_13', 6)	# 169-174
    sprite('lp433_14', 6)	# 175-180
    sprite('lp433_15', 6)	# 181-186
    sprite('keep', 32767)	# 187-32953
    enterState('PersonaDeleteAndIdling')

@State
def PLA_PersonaShot_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000b03cffff00000000b03cffff00000000')
        callSubroutine('PLA_SPAttackInit')
        callSubroutine('PLA_ForceWarp')
        Unknown4007(3)
        Unknown2017(0)
        Unknown11063(1)
    sprite('lp407_00', 3)	# 1-3
    sprite('lp407_01', 3)	# 4-6
    sprite('lp407_02', 3)	# 7-9
    SFX_3('la000')
    GFX_0('407ready_C', 0)
    GFX_0('407add_C', 0)
    sprite('lp407_03', 3)	# 10-12
    sprite('lp407_04', 3)	# 13-15
    sprite('lp407_05', 3)	# 16-18
    label(1)
    sprite('lp407_03', 3)	# 19-21
    SLOT_51 = (SLOT_51 + 1)
    sprite('lp407_04', 3)	# 22-24
    sprite('lp407_05', 2)	# 25-26
    sprite('lp407_05', 1)	# 27-27
    if (not (SLOT_51 >= 2)):
        sendToLabel(1)
    sprite('lp407_06', 6)	# 28-33
    sprite('lp407_07', 6)	# 34-39
    Unknown26('407ready_C')
    GFX_0('407Shot_SB', 0)
    label(0)
    sprite('lp407_08', 3)	# 40-42
    SLOT_52 = (SLOT_52 + 1)
    sprite('lp407_09', 3)	# 43-45
    sprite('lp407_10', 2)	# 46-47
    sprite('lp407_10', 1)	# 48-48
    if (not (SLOT_52 >= 7)):
        sendToLabel(0)
    sprite('keep', 32767)	# 49-32815
    enterState('PersonaDeleteAndIdling')
    ExitState()

@State
def PLA_PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000402bfeff50c30000402bfeff50c30000402bfeff50c30000')
        callSubroutine('PersonaReset')
        callSubroutine('PLA_ForceWarp')
        Unknown2053(1)
    sprite('lp610_00', 6)	# 1-6
    sprite('lp610_01', 6)	# 7-12
    sprite('lp610_02', 6)	# 13-18
    GFX_0('610winline', 100)
    sprite('lp610_03', 6)	# 19-24
    sprite('lp610_04', 6)	# 25-30
    sprite('lp610_05', 6)	# 31-36
    sprite('lp610_03', 6)	# 37-42
    sprite('lp610_04', 6)	# 43-48
    sprite('lp610_05', 6)	# 49-54
    label(0)
    sprite('lp610_06', 8)	# 55-62
    SFX_3('cloth_l')
    sprite('lp610_07', 8)	# 63-70
    sprite('lp610_08', 8)	# 71-78
    sprite('lp610_06', 8)	# 79-86
    sprite('lp610_07', 8)	# 87-94
    sprite('lp610_08', 8)	# 95-102
    loopRest()
    gotoLabel(0)

@State
def PLA_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000010b6fdff00000000b03cffff00000000b03cffff00000000')
        callSubroutine('PLA_AttackInit')
        callSubroutine('PLA_ForceWarp')
        Unknown2017(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5002):
                sendToLabel(0)
        Unknown23022(1)

        def upon_3():
            Unknown4007(3)
    sprite('lp450_00', 6)	# 1-6
    GFX_0('450rasen', 100)
    sprite('lp450_01', 6)	# 7-12
    sprite('lp450_02', 6)	# 13-18
    sprite('lp450_03', 6)	# 19-24
    sprite('lp450_04', 6)	# 25-30
    sprite('lp450_05', 6)	# 31-36
    sprite('lp450_06', 6)	# 37-42
    sprite('lp450_07', 6)	# 43-48
    sprite('lp450_08', 6)	# 49-54
    sprite('lp450_09', 6)	# 55-60
    sprite('lp450_10', 6)	# 61-66
    sprite('lp450_11', 6)	# 67-72
    sprite('lp450_12', 6)	# 73-78
    sprite('lp450_13', 6)	# 79-84
    GFX_0('Ichigeki_atk', 100)
    sprite('lp450_14', 6)	# 85-90
    sprite('lp450_15', 6)	# 91-96
    sprite('lp450_13', 6)	# 97-102
    sprite('lp450_14', 6)	# 103-108
    sprite('lp450_15', 6)	# 109-114
    sprite('lp450_13', 7)	# 115-121
    sprite('lp450_14', 7)	# 122-128
    sprite('lp450_15', 7)	# 129-135
    sprite('lp450_13', 8)	# 136-143
    sprite('lp450_14', 8)	# 144-151
    sprite('lp450_15', 8)	# 152-159
    label(0)
    sprite('keep', 32767)	# 160-32926
    Unknown4007(0)
    enterState('PersonaDeleteAndIdling')

@State
def __406setlope():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(28)
    sprite('null', 3)	# 1-3
    GFX_0('406birdwing', 100)
    sprite('null', 3)	# 4-6
    SFX_3('cut_m')
    sprite('null', 8)	# 7-14
    GFX_0('406yariatk', 100)

@State
def __406birdwing():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f3430366269726477696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(28)
        Unknown4007(2)
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        Unknown4015()

        def upon_43():
            if (SLOT_48 == 222):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown3004(30)
    label(0)
    sprite('null', 37)	# 32768-32804
    teleportRelativeX(-25000)
    Unknown1007(10000)
    Unknown1056(1400)
    sprite('null', 11)	# 32805-32815
    Unknown3004(-25)

@State
def __406line():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('6c6165665f3430366c696e652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1800)
        Unknown3001(0)
        Unknown4015()
    sprite('null', 20)	# 1-20
    Unknown3004(50)
    sprite('null', 20)	# 21-40
    GFX_0('406linedel', 100)
    sprite('null', 7)	# 41-47
    Unknown3004(-40)

@State
def __406linedel():

    def upon_IMMEDIATE():
        teleportRelativeX(170000)
        Unknown1007(400000)
        physicsXImpulse(12000)
        physicsYImpulse(-27000)
        GFX_0('406linedeleff', 100)
    sprite('null', 10)	# 1-10
    sprite('null', 7)	# 11-17
    Unknown3004(-40)

@State
def __406linedeleff():

    def upon_IMMEDIATE():
        Unknown53(2)
        Unknown4007(2)
        Unknown4010(2)
    label(1)
    sprite('null', 1)	# 1-1
    GFX_1('lpef_406linedel', 100)
    loopRest()
    gotoLabel(1)

@State
def __406floor():

    def upon_IMMEDIATE():
        Unknown53(2)
        teleportRelativeY(0)
        if (SLOT_19 < 400000):
            SLOT_52 = SLOT_23
            Unknown1086(22)
            teleportRelativeY(0)
    sprite('null', 1)	# 1-1
    GFX_1('lpef_406floor', 100)

@State
def __406yariatk():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f343036796172692e444947000000000000000000000000000000006c6165665f343036796172695f3030302e6d6d6f740000000000000000000000')
        Unknown3032()
        Unknown1096(2200)
        Unknown3001(0)
        teleportRelativeX(400000)
        Unknown1007(50000)
        if (SLOT_19 < 400000):
            SLOT_52 = SLOT_23
            Unknown1086(22)
            teleportRelativeY(50000)

        def upon_12():
            sendToLabel(10)
    sprite('null', 10)	# 1-10
    GFX_0('406floor', 100)
    Unknown3004(50)
    sprite('null', 30)	# 11-40
    GFX_0('vr_lp406_1statk', 100)
    sprite('null', 30)	# 41-70
    GFX_0('406yarihitmiss', 100)
    Unknown3004(-20)

@State
def vr_lp406_1statk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AirPushbackY(25000)
        Unknown9016(1)
        AirUntechableTime(40)
        GroundedHitstunAnimation(9)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23027()

        def upon_12():
            sendToLabel(10)
    sprite('lp406_atk00', 1)	# 1-1
    Unknown1064(1000)
    RefreshMultihit()
    sprite('lp406_atk00ex', 13)	# 2-14
    sprite('lp406_atk00', 2)	# 15-16
    Unknown23027()
    loopRest()
    ExitState()
    label(10)
    sprite('null', 15)	# 17-31
    sprite('null', 20)	# 32-51
    Unknown3004(-20)

@State
def __406yarihitmiss():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    GFX_1('lpef_406syometuA', 100)
    sprite('null', 1)	# 2-2
    GFX_1('lpef_406syometuD', 100)
    sprite('null', 1)	# 3-3
    GFX_1('lpef_406syometuE', 100)
    sprite('null', 1)	# 4-4
    GFX_1('lpef_406syometuB', 100)
    sprite('null', 1)	# 5-5
    GFX_1('lpef_406syometuC', 100)

@State
def __205bird():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 8)	# 1-8
    Unknown3004(20)
    sprite('null', 10)	# 9-18
    GFX_0('205birdline', 100)
    GFX_0('vr_lp205atk', 100)
    sprite('null', 37)	# 19-55
    Unknown3004(-13)

@State
def __205birdwing():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f3230356269726477696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(3)
        Unknown4010(3)
        Unknown23015(2)
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        Unknown3004(30)
    sprite('null', 42)	# 1-42
    sprite('null', 15)	# 43-57
    Unknown3004(-17)

@State
def __205birdline():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f323035626972646c696e652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1300)
        teleportRelativeY(75000)
        Unknown3001(0)
        Unknown4015()
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 15)	# 1-15
    Unknown3004(40)
    SFX_3('slash_rapier_fast')
    sprite('null', 15)	# 16-30
    Unknown3004(-17)

@State
def __206bird():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(28)
        Unknown4010(2)
    sprite('null', 2)	# 1-2
    sprite('null', 1)	# 3-3
    GFX_0('206birdline1', 100)
    GFX_0('206pattern', 100)
    sprite('null', 6)	# 4-9
    sprite('null', 13)	# 10-22
    GFX_0('vr_lp206atk_00', 100)
    sprite('null', 12)	# 23-34
    GFX_0('vr_lp206atk_01', 100)
    sprite('null', 5)	# 35-39
    GFX_0('vr_lp206atk_02', 100)
    sprite('null', 7)	# 40-46
    GFX_0('vr_lp206atk_03', 100)
    sprite('null', 20)	# 47-66
    GFX_0('vr_lp206atk_04', 100)

@State
def __206birdwing_anim():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f3230366269726477696e675f616e696d2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(2)
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(255)
        Unknown3004(80)
        Unknown1007(30000)
    sprite('null', 15)	# 1-15
    physicsXImpulse(-6000)
    Unknown1059(-80)
    sprite('null', 5)	# 16-20
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1059(0)
    Unknown3004(-51)

@State
def __206birdwing():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f3230366269726477696e672e4449470000000000000000000000006c6165665f3230366269726477696e675f3030302e6d6d6f7400000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        teleportRelativeX(-150000)
        teleportRelativeY(350000)
        Unknown1056(800)
    sprite('null', 70)	# 1-70
    Unknown23119(6579300, 4, 20)
    Unknown3004(30)
    sprite('null', 20)	# 71-90
    Unknown3004(-13)

@State
def __206birdline1():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f323036626972646c696e65312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        Unknown4015()
        Unknown4007(28)
        Unknown4010(2)
    sprite('null', 65)	# 1-65
    Unknown3004(15)
    sprite('null', 15)	# 66-80
    Unknown3004(-17)

@State
def __206pattern():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f3230367061747465726e412e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        Unknown4015()
        Unknown4007(28)
        Unknown4010(2)
    sprite('null', 20)	# 1-20
    sprite('null', 20)	# 21-40
    Unknown3004(15)
    sprite('null', 15)	# 41-55
    Unknown3004(-17)

@State
def __232uzu():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f323332757a752e44494700000000000000000000000000000000006c6165665f323332757a755f3030302e6d6d6f74000000000000000000000000')
        Unknown21014(100)
        Unknown3032()
        Unknown1096(1600)
        Unknown3001(0)
        teleportRelativeX(-100000)
        teleportRelativeY(300000)
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 14)	# 1-14
    Unknown3004(30)
    sprite('null', 17)	# 15-31
    Unknown23119(16777215, 17, 1)
    Unknown3004(-15)

@State
def __232atk():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3032()
        Unknown1096(1800)
        teleportRelativeY(45000)
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 6)	# 1-6
    Unknown3001(0)
    Unknown3004(50)
    Unknown4003('6c6165665f32333261746b5f612e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 7-11
    Unknown4003('6c6165665f32333261746b5f622e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 16)	# 12-27
    Unknown23119(16777215, 16, 1)
    Unknown3004(-16)

@State
def __232handeff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23067('lpef_232charge')
        Unknown3001(0)
        Unknown3004(30)
        teleportRelativeX(-100000)
        teleportRelativeY(300000)
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 24)	# 1-24
    Unknown3004(30)
    sprite('null', 10)	# 25-34
    Unknown3004(-26)

@State
def __254atk():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('null', 60)	# 1-60
    GFX_0('254lopeatk', 100)
    GFX_0('254lopeatksub', 100)

@State
def __254lopeatk():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f32353461746b2e44494700000000000000000000000000000000006c6165665f32353461746b5f3030302e6d6d6f74000000000000000000000000')
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        Unknown4007(28)
        Unknown4010(28)
    sprite('null', 25)	# 1-25
    Unknown3004(10)
    sprite('null', 10)	# 26-35
    Unknown3004(-26)

@State
def __254lopeatksub():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f32353461746b7375622e44494700000000000000000000000000006c6165665f32353461746b7375625f3030302e6d6d6f74000000000000000000')
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        Unknown4007(28)
        Unknown4010(28)
    sprite('null', 10)	# 1-10
    sprite('null', 10)	# 11-20
    Unknown3004(30)
    sprite('null', 5)	# 21-25
    sprite('null', 10)	# 26-35
    Unknown3004(-26)

@State
def __254circle():

    def upon_IMMEDIATE():
        Unknown4007(28)
        Unknown4010(28)
    sprite('null', 1)	# 1-1
    GFX_1('lpef_254circle', 100)

@State
def __407ready_C():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f34303762616c6c2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown1074(5000)
        Unknown23015(12)
    sprite('null', 32)	# 1-32
    GFX_0('407light', 100)
    GFX_0('407tinkle', 100)
    Unknown1096(0)
    Unknown1099(58)
    SFX_3('distortion_b')
    sprite('null', 80)	# 33-112
    Unknown1096(1800)
    Unknown1099(0)

@State
def __407ready_D():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f34303762616c6c2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4011(3)
        Unknown1074(5000)
        Unknown23015(12)
    sprite('null', 75)	# 1-75
    GFX_0('407light', 100)
    GFX_0('407tinkle', 100)
    Unknown1096(0)
    Unknown1099(24)
    SFX_3('distortion_b')
    sprite('null', 80)	# 76-155
    Unknown1096(1800)
    Unknown1099(0)

@State
def __407add_C():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f3430376164642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(3)
        Unknown23015(12)
        Unknown1073(6000)
    sprite('null', 30)	# 1-30
    Unknown3001(0)
    Unknown3004(24)
    sprite('null', 30)	# 31-60
    Unknown3004(-15)

@State
def __407add_D():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f3430376164642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(12)
        Unknown1073(6000)
    sprite('null', 50)	# 1-50
    Unknown3001(0)
    Unknown3004(24)
    sprite('null', 30)	# 51-80
    Unknown3004(-15)

@State
def __407light():

    def upon_IMMEDIATE():
        Unknown4054(12)
        Unknown23067('lpef_407')
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        Unknown4011(2)
    sprite('null', 32767)	# 1-32767

@State
def __407rope():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f343037726f70652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown23015(12)
    sprite('null', 16)	# 1-16
    Unknown3001(0)
    sprite('null', 120)	# 17-136
    Unknown3004(16)
    label(0)
    sprite('null', 1)	# 137-137
    gotoLabel(0)
    label(10)
    sprite('null', 10)	# 138-147
    Unknown3004(-32)

@State
def __407tinkle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown23015(12)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown4054(12)
    Unknown4045('6c7065665f3430375f74696e6b6c65000000000000000000000000000000000064000000')
    gotoLabel(0)
    label(10)
    sprite('null', 1)	# 2-2

@State
def __407Shot_SB():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f34303762616c6c2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1074(5000)
        Unknown23015(12)
        Unknown4011(3)
        physicsXImpulse(0)
        Unknown53(1)
        Unknown1096(1800)

        def upon_STATE_END():
            if SLOT_51:
                Unknown36(22)
                Unknown23015(0)
                Unknown2019(0)
                Unknown35()
        loopRelated(17, 101)
        sendToLabelUpon(17, 581)
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
        sendToLabelUpon(54, 581)

        def upon_43():
            if (SLOT_48 == 302):
                sendToLabel(581)
                clearUponHandler(43)
            if (SLOT_48 == 303):
                sendToLabel(581)
                clearUponHandler(43)
            if (SLOT_48 == 304):
                sendToLabel(581)
                clearUponHandler(43)
            if (SLOT_48 == 307):
                sendToLabel(581)
                clearUponHandler(43)
        Unknown11063(1)
    sprite('null', 1)	# 1-1
    GFX_0('407Shot_atk_SB', 100)
    GFX_0('407light', 100)
    GFX_0('407tinkle', 100)
    sprite('null', 2)	# 2-3
    sprite('null', 2)	# 4-5
    SFX_3('la000')
    Unknown1028(300)
    Unknown1099(-12)
    physicsYImpulse(-3000)
    setGravity(-20)
    label(1)
    sprite('null', 2)	# 6-7
    sprite('null', 10)	# 8-17
    gotoLabel(1)
    label(581)
    sprite('null', 3)	# 18-20
    clearUponHandler(54)
    Unknown1019(10)
    Unknown1028(0)
    YAccel(10)
    setGravity(0)
    Unknown3004(-16)

@State
def __407Shot_atk_SB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP1(70)
        Unknown11033(1)
        Damage(1500)
        Hitstop(0)
        Unknown11001(0, 26, 26)
        GroundedHitstunAnimation(9)
        Unknown11042(1)
        Unknown1098(110)
        Unknown4010(2)
        Unknown4007(2)

        def upon_STATE_END():
            clearUponHandler(1)
            Unknown21015('34303753686f745f5342000000000000000000000000000000000000000000003301000000000000')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown23029(2, 303, 0)

        def upon_78():
            clearUponHandler(10)
            clearUponHandler(78)
            Unknown4007(0)
            Unknown4010(0)
            Unknown23029(2, 302, 0)
            Unknown23027()
            Unknown36(27)
            Unknown23015(15)
            Unknown2019(1000)
            Unknown35()
            Unknown23151(27, 103)
            if (SLOT_23 <= 150000):
                teleportRelativeY(200000)
            GFX_0('407Shot_SB_Test', -1)
            sendToLabel(100)

        def upon_82():
            clearUponHandler(10)
            clearUponHandler(82)
            Unknown4007(0)
            Unknown23029(2, 302, 0)
            Unknown36(27)
            Unknown23015(15)
            Unknown2019(1000)
            Unknown35()
            Unknown23151(27, 103)
            if (SLOT_23 <= 150000):
                teleportRelativeY(200000)
            GFX_0('407Shot_SB_Test', -1)
            sendToLabel(100)
        Unknown11063(1)
    sprite('vr_la407_atkcol', 30)	# 1-30
    StartMultihit()
    Unknown1099(-3)
    sprite('vr_la407_atkcol', 1)	# 31-31
    RefreshMultihit()
    Unknown11063(0)
    sprite('vr_la407_atkcol', 100)	# 32-131
    ExitState()
    label(100)
    sprite('null', 1)	# 132-132
    sprite('null', 1)	# 133-133

@State
def __407Shot_SB_Test():

    def upon_IMMEDIATE():
        Unknown4003('6c7065665f34303762616c6c2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1074(5000)
        Unknown23015(12)
        physicsXImpulse(0)
        Unknown53(1)
        Unknown1096(1800)

        def upon_STATE_END():
            Unknown36(22)
            Unknown23015(0)
            Unknown2019(0)
            Unknown35()
    sprite('null', 30)	# 1-30
    GFX_0('407light', 100)
    GFX_0('407tinkle', 100)
    Unknown1099(100)
    Unknown1084(1)
    Unknown1028(0)
    SFX_3('la000')
    sprite('null', 5)	# 31-35
    Unknown1099(0)
    Unknown3004(-48)

@State
def __430Ptackle_start():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4007(28)
    sprite('null', 10)	# 1-10
    GFX_0('430rasen', 100)
    sprite('null', 25)	# 11-35
    GFX_0('430line', 100)
    sprite('null', 32767)	# 36-32802

@State
def __430rasen():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('6c6165665f636d6e726173656e2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1800)
        Unknown1007(-75000)
        Unknown3001(0)
        Unknown4015()
    sprite('null', 30)	# 1-30
    Unknown3004(90)
    sprite('null', 10)	# 31-40
    Unknown3004(-26)

@State
def __430line():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
    sprite('null', 8)	# 1-8
    GFX_0('430line3', 100)
    sprite('null', 8)	# 9-16
    GFX_0('430line2', 100)
    sprite('null', 8)	# 17-24
    GFX_0('430line1', 100)

@State
def __430line1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown4003('6c6165665f3433306c696e65312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(-10000)
        Unknown1096(2360)
        Unknown3001(0)
        Unknown4015()
    sprite('null', 25)	# 1-25
    Unknown3004(30)
    sprite('null', 10)	# 26-35
    physicsXImpulse(25000)
    Unknown3004(-26)

@State
def __430line2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown4003('6c6165665f3433306c696e65322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(-10000)
        Unknown1096(2360)
        Unknown3001(0)
        Unknown4015()
    sprite('null', 33)	# 1-33
    Unknown3004(30)
    sprite('null', 10)	# 34-43
    physicsXImpulse(25000)
    Unknown3004(-26)

@State
def __430line3():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown4003('6c6165665f3433306c696e65332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(-10000)
        Unknown1096(2360)
        Unknown3001(0)
        Unknown4015()
    sprite('null', 41)	# 1-41
    Unknown3004(30)
    sprite('null', 10)	# 42-51
    physicsXImpulse(25000)
    Unknown3004(-26)

@State
def __430tackleatk():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown23015(1)
        Unknown4003('6c6165665f3433307461636b6c652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(-10000)
        Unknown1096(2360)
        Unknown3001(0)
        Unknown3004(90)
        Unknown4015()
        GFX_0('Ushimove', 100)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 10)	# 1-10
    sprite('null', 40)	# 11-50
    Unknown3004(-9)

@State
def Ushimove():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown23067('lpef_430tacke')
        Unknown3001(0)
        Unknown3004(30)
        teleportRelativeY(200000)
    sprite('null', 10)	# 1-10
    physicsXImpulse(33000)
    sprite('null', 40)	# 11-50
    Unknown3004(-7)

@State
def __430upperaura():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f34333075707065722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown3032()
        Unknown1072(8000)
        Unknown1096(700)
        GFX_0('upperaura_eff', 100)
    sprite('null', 2)	# 1-2
    sprite('null', 15)	# 3-17
    sprite('null', 5)	# 18-22
    Unknown3004(-50)
    Unknown1059(10)

@State
def upperaura_eff():

    def upon_IMMEDIATE():
        Unknown23067('laef_430upper')
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(8000)
        teleportRelativeX(-85000)
        Unknown1007(65000)
    sprite('null', 70)	# 1-70
    sprite('null', 5)	# 71-75
    Unknown3004(-51)

@State
def __433lopecore():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown4003('6c6165665f34333373746172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(50000)
        Unknown1007(420000)
        Unknown1096(2000)
        Unknown3001(0)
        Unknown3004(30)
        Unknown4010(2)
    sprite('null', 60)	# 1-60
    GFX_0('433charge', 100)
    sprite('null', 10)	# 61-70
    Unknown3004(-26)

@State
def __433charge():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        GFX_2('lpef_433charge')
        Unknown1096(800)
        Unknown3001(0)
        Unknown3004(60)
    sprite('null', 30)	# 1-30
    sprite('null', 15)	# 31-45
    Unknown1099(-20)
    Unknown3004(-7)
    sprite('null', 15)	# 46-60
    GFX_1('lpef_433power', 100)
    GFX_0('spearlineA', 100)
    GFX_0('spearlineB', 100)
    GFX_0('spearlineC', 100)

@State
def __433ringatk():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4007(28)

        def upon_43():
            if (SLOT_48 == 306):
                clearUponHandler(43)
                sendToLabel(580)
    sprite('null', 12)	# 1-12
    GFX_0('433ringA', 100)
    Unknown38(5, 1)
    GFX_0('vr_lp433_01atk', 100)
    sprite('null', 12)	# 13-24
    GFX_0('433ringB', 100)
    Unknown38(6, 1)
    GFX_0('vr_lp433_02atk', 100)
    sprite('null', 12)	# 25-36
    GFX_0('433ringC', 100)
    Unknown38(7, 1)
    GFX_0('vr_lp433_03atk', 100)
    sprite('null', 30)	# 37-66
    ExitState()
    label(580)
    sprite('null', 1)	# 67-67
    ExitState()

@State
def __433ringA():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f34333372696e67412e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1400)
        teleportRelativeY(30000)
        teleportRelativeX(210000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    GFX_0('433floorA', 100)
    Unknown3004(30)
    SFX_3('la002')
    sprite('null', 10)	# 21-30
    SFX_3('chain_snap')
    sprite('null', 10)	# 31-40
    SFX_3('chain_move')
    sprite('null', 10)	# 41-50
    SFX_3('chain_snap')
    sprite('null', 10)	# 51-60
    SFX_3('chain_move')
    sprite('null', 10)	# 61-70
    SFX_3('chain_snap')
    sprite('null', 10)	# 71-80
    SFX_3('chain_move')
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433ringB():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f34333372696e67422e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeY(50000)
        teleportRelativeX(365000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    GFX_0('433floorB', 100)
    Unknown3004(30)
    SFX_3('la002')
    sprite('null', 10)	# 21-30
    SFX_3('chain_snap')
    sprite('null', 10)	# 31-40
    SFX_3('chain_move')
    sprite('null', 10)	# 41-50
    SFX_3('chain_snap')
    sprite('null', 10)	# 51-60
    SFX_3('chain_move')
    sprite('null', 10)	# 61-70
    SFX_3('chain_snap')
    sprite('null', 10)	# 71-80
    SFX_3('chain_move')
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433ringC():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown4003('6c6165665f34333372696e67412e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1400)
        teleportRelativeY(15000)
        teleportRelativeX(450000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    GFX_0('433floorC', 100)
    Unknown3004(30)
    SFX_3('la002')
    sprite('null', 10)	# 21-30
    SFX_3('chain_snap')
    sprite('null', 10)	# 31-40
    SFX_3('chain_move')
    sprite('null', 10)	# 41-50
    SFX_3('chain_snap')
    sprite('null', 10)	# 51-60
    SFX_3('chain_move')
    sprite('null', 10)	# 61-70
    SFX_3('chain_snap')
    sprite('null', 10)	# 71-80
    SFX_3('chain_move')
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433ringB_2nd():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4003('6c6165665f34333372696e67422e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeY(50000)
        teleportRelativeX(625000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    GFX_0('433floorB', 100)
    Unknown3004(30)
    SFX_3('la002')
    sprite('null', 10)	# 21-30
    SFX_3('chain_snap')
    sprite('null', 10)	# 31-40
    SFX_3('chain_move')
    sprite('null', 10)	# 41-50
    SFX_3('chain_snap')
    sprite('null', 10)	# 51-60
    SFX_3('chain_move')
    sprite('null', 10)	# 61-70
    SFX_3('chain_snap')
    sprite('null', 10)	# 71-80
    SFX_3('chain_move')
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433ringC_2nd():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown4003('6c6165665f34333372696e67412e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1400)
        teleportRelativeY(15000)
        teleportRelativeX(700000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    GFX_0('433floorC', 100)
    Unknown3004(30)
    SFX_3('la002')
    sprite('null', 10)	# 21-30
    SFX_3('chain_snap')
    sprite('null', 10)	# 31-40
    SFX_3('chain_move')
    sprite('null', 10)	# 41-50
    SFX_3('chain_snap')
    sprite('null', 10)	# 51-60
    SFX_3('chain_move')
    sprite('null', 10)	# 61-70
    SFX_3('chain_snap')
    sprite('null', 10)	# 71-80
    SFX_3('chain_move')
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433floorA():

    def upon_IMMEDIATE():
        Unknown23067('lpef_433floor')
        Unknown4007(28)
        Unknown4010(2)
    sprite('null', 80)	# 1-80
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433floorB():

    def upon_IMMEDIATE():
        Unknown23067('lpef_433floor')
    sprite('null', 80)	# 1-80
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def __433floorC():

    def upon_IMMEDIATE():
        Unknown23067('lpef_433floor')
    sprite('null', 80)	# 1-80
    sprite('null', 15)	# 81-95
    Unknown3004(-17)

@State
def spearlineA():

    def upon_IMMEDIATE():
        Unknown4010(2)
        physicsXImpulse(14000)
        physicsYImpulse(-35000)
        GFX_0('406linedeleff', 100)
    sprite('null', 9)	# 1-9
    GFX_0('433yariA', 100)
    sprite('null', 6)	# 10-15
    Unknown3004(-43)

@State
def spearlineB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        physicsXImpulse(25000)
        physicsYImpulse(-35000)
        GFX_0('406linedeleff', 100)
    sprite('null', 9)	# 1-9
    GFX_0('433yariB', 100)
    sprite('null', 6)	# 10-15
    Unknown3004(-43)

@State
def spearlineC():

    def upon_IMMEDIATE():
        Unknown4010(2)
        physicsXImpulse(34000)
        physicsYImpulse(-35000)
        GFX_0('406linedeleff', 100)
    sprite('null', 9)	# 1-9
    GFX_0('433yariC', 100)
    sprite('null', 6)	# 10-15
    Unknown3004(-43)

@State
def __433yariA():

    def upon_IMMEDIATE():
        Unknown53(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23067('lpef433_yariA')
        Unknown1096(700)
    sprite('null', 11)	# 1-11
    sprite('null', 3)	# 12-14
    Unknown3004(-85)

@State
def __433yariB():

    def upon_IMMEDIATE():
        Unknown53(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23067('lpef433_yariB')
        Unknown1096(700)
    sprite('null', 11)	# 1-11
    sprite('null', 3)	# 12-14
    Unknown3004(-85)

@State
def __433yariC():

    def upon_IMMEDIATE():
        Unknown53(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23067('lpef433_yariC')
        Unknown1096(700)
    sprite('null', 11)	# 1-11
    sprite('null', 3)	# 12-14
    Unknown3004(-85)

@State
def Cmnrasen():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f636d6e726173656e2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(2000)
        Unknown4015()
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 20)	# 1-20
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def vr_lp232atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(800)
        AttackP2(70)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(2000)
        AirPushbackY(30000)
        AirUntechableTime(24)
        Hitstop(0)
        Unknown11001(11, 11, 13)
        Unknown9016(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 203, 0)
        Unknown4007(3)
        Unknown4010(3)
        teleportRelativeX(-50000)
    sprite('vr_lp232atkcol04', 3)	# 1-3
    RefreshMultihit()
    sprite('vr_lp232atkcol00', 3)	# 4-6
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    sprite('vr_lp232atkcol01', 3)	# 7-9
    RefreshMultihit()
    sprite('vr_lp232atkcol02', 7)	# 10-16
    Unknown23029(3, 6001, 0)
    Unknown23027()

@State
def vr_lp205atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(1000)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Hitstop(0)
        Unknown11001(6, 6, 8)
        Unknown9016(1)
        Unknown11057(800)
        teleportRelativeX(-200000)
        Unknown1056(600)
        physicsXImpulse(20000)
        Unknown4007(3)
        Unknown4010(3)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 204, 0)
    sprite('null', 5)	# 1-5
    sprite('vr_lp205atkcol', 7)	# 6-12
    RefreshMultihit()
    sprite('vr_lp205atkcol', 7)	# 13-19
    RefreshMultihit()
    sprite('vr_lp205atkcol', 5)	# 20-24
    RefreshMultihit()
    sprite('vr_lp205atkcol', 2)	# 25-26
    Unknown1084(1)

@State
def vr_lp205atkUP():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(2)
        AirUntechableTime(35)
        AirPushbackY(20000)
        Hitstop(0)
        Unknown11001(11, 11, 13)
        Unknown4007(2)
        Unknown4010(2)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 204, 0)
    sprite('vr_lp205atkcol_00', 4)	# 1-4
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('vr_lp205atkcol_01', 4)	# 5-8
    sprite('vr_lp205atkcol_02', 4)	# 9-12
    sprite('vr_lp205atkcol_03', 4)	# 13-16
    loopRest()

@State
def vr_lp205atkDOWN():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(2)
        AirUntechableTime(35)
        AirPushbackY(20000)
        Unknown4007(2)
        Unknown4010(2)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 204, 0)
    sprite('vr_lp205atkcol_10', 4)	# 1-4
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('vr_lp205atkcol_11', 4)	# 5-8
    sprite('vr_lp205atkcol_12', 4)	# 9-12
    sprite('vr_lp205atkcol_13', 4)	# 13-16
    loopRest()

@Subroutine
def vr_lp206atk():
    AttackLevel_(4)
    Damage(1000)
    AttackP1(80)
    Unknown11092(1)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(10000)
    AirPushbackY(20000)
    AirUntechableTime(30)
    Hitstop(0)
    Unknown11001(8, 8, 13)
    Unknown9016(1)
    Unknown11057(600)
    Unknown23182(2)
    SFX_3('slash_knife_fast')
    Unknown4007(3)
    Unknown4010(3)

    def upon_ON_HIT_OR_BLOCK():
        Unknown23029(3, 206, 0)

@State
def vr_lp206atk_00():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('vr_lp206atk')
        teleportRelativeX(240000)
        Unknown1007(400000)
        physicsXImpulse(40000)
        setGravity(2000)
    sprite('vr_lp206atkcol', 10)	# 1-10

@State
def vr_lp206atk_01():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('vr_lp206atk')
        AirPushbackY(2000)
        teleportRelativeX(200000)
        Unknown1007(250000)
        physicsXImpulse(40000)
    sprite('vr_lp206atkcol', 10)	# 1-10

@State
def vr_lp206atk_02():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('vr_lp206atk')
        AirPushbackY(-12000)
        teleportRelativeX(150000)
        Unknown1007(350000)
        physicsXImpulse(60000)
        setGravity(2000)
    sprite('vr_lp206atkcol', 10)	# 1-10

@State
def vr_lp206atk_03():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('vr_lp206atk')
        teleportRelativeX(100000)
        Unknown1007(150000)
        physicsXImpulse(50000)
    sprite('vr_lp206atkcol', 10)	# 1-10

@State
def vr_lp206atk_04():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('vr_lp206atk')
        teleportRelativeX(100000)
        Unknown1007(50000)
        physicsXImpulse(50000)
        setGravity(-2000)
    sprite('vr_lp206atkcol', 10)	# 1-10

@State
def vr_lp254atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(800)
        Unknown11092(1)
        AirPushbackX(2000)
        AirPushbackY(10000)
        PushbackX(12000)
        Unknown30055('f04902001e00000000000000')
        Unknown30056('400d03001e00000000000000')
        Hitstop(6)
        Unknown4007(2)
        Unknown4010(2)
    sprite('vr_lp254atkcol', 6)	# 1-6
    RefreshMultihit()
    Unknown1098(120)
    SFX_3('slash_rapier_fast')
    sprite('vr_lp254atkcol', 6)	# 7-12
    RefreshMultihit()
    Unknown1098(90)
    SFX_3('slash_rapier_fast')

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown23029(3, 221, 0)
    sprite('vr_lp254atkcol', 6)	# 13-18
    RefreshMultihit()
    Unknown1098(90)
    SFX_3('slash_rapier_fast')
    loopRest()

@State
def vr_lp433_01atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(300)
        AttackP1(70)
        AttackP2(70)
        AirUntechableTime(30)
        Unknown9154(30)
        GroundedHitstunAnimation(9)
        Hitstop(1)
        Unknown9310(1)
        PushbackX(0)
        AirPushbackX(3000)
        AirPushbackY(5000)
        Unknown9016(1)
        Unknown11042(1)
        Unknown11092(1)
        Unknown23182(2)
        Unknown4007(28)
        Unknown4010(2)
    sprite('vr_lp433_01atkcol', 10)	# 1-10
    sprite('vr_lp433_01atkcol', 10)	# 11-20
    RefreshMultihit()
    sprite('vr_lp433_01atkcol', 10)	# 21-30
    RefreshMultihit()
    sprite('vr_lp433_01atkcol', 10)	# 31-40
    RefreshMultihit()
    sprite('vr_lp433_01atkcol', 10)	# 41-50
    RefreshMultihit()

@State
def vr_lp433_02atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(300)
        AttackP1(70)
        AttackP2(70)
        AirUntechableTime(30)
        Unknown9154(30)
        GroundedHitstunAnimation(9)
        Hitstop(1)
        Unknown9310(1)
        PushbackX(0)
        AirPushbackX(1000)
        AirPushbackY(0)
        Unknown9310(10)
        Unknown9016(1)
        Unknown11068(1)
        Unknown11042(1)
        Unknown11092(1)
        Unknown23182(2)
        Unknown4007(28)
        Unknown4010(2)
    sprite('vr_lp433_02atkcol', 10)	# 1-10
    sprite('vr_lp433_02atkcol', 10)	# 11-20
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 21-30
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 31-40
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 41-50
    RefreshMultihit()

@State
def vr_lp433_03atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(300)
        AttackP1(70)
        AttackP2(70)
        AirUntechableTime(30)
        Unknown9154(30)
        GroundedHitstunAnimation(9)
        Hitstop(1)
        Unknown9310(1)
        PushbackX(0)
        AirPushbackX(-4000)
        AirPushbackY(5000)
        Unknown9310(10)
        Unknown9016(1)
        Unknown11068(1)
        Unknown11092(1)
        Unknown23182(2)
        Unknown4007(28)
        Unknown4010(2)
    sprite('vr_lp433_03atkcol', 10)	# 1-10
    sprite('vr_lp433_03atkcol', 10)	# 11-20
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 21-30
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 31-40
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 41-50
    RefreshMultihit()

@State
def vr_lp433_02atk_2nd():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(130)
        Hitstop(1)
        PushbackX(10000)
        AirPushbackX(1000)
        AirPushbackY(0)
        Unknown9310(10)
        Unknown9016(1)
        teleportRelativeX(260000)
        Unknown11068(1)
        Unknown23182(2)
    sprite('vr_lp433_02atkcol', 10)	# 1-10
    sprite('vr_lp433_02atkcol', 10)	# 11-20
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 21-30
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 31-40
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 41-50
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 51-60
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 61-70
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 10)	# 71-80
    RefreshMultihit()
    sprite('vr_lp433_02atkcol', 5)	# 81-85
    RefreshMultihit()
    loopRest()

@State
def vr_lp433_03atk_2nd():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(130)
        Hitstop(1)
        PushbackX(-8000)
        AirPushbackX(-4000)
        AirPushbackY(5000)
        Unknown9310(10)
        Unknown9016(1)
        teleportRelativeX(250000)
        Unknown11068(1)
        Unknown23182(2)

        def upon_32():
            PushbackX(10000)
    sprite('vr_lp433_03atkcol', 10)	# 1-10
    sprite('vr_lp433_03atkcol', 10)	# 11-20
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 21-30
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 31-40
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 41-50
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 51-60
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 61-70
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 10)	# 71-80
    RefreshMultihit()
    sprite('vr_lp433_03atkcol', 5)	# 81-85
    RefreshMultihit()
    loopRest()

@State
def laef_swing():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 1)	# 1-1
    GFX_1('laef_swing', 100)
    GFX_1('laef_swing_b', 100)

@State
def laef401punch():

    def upon_IMMEDIATE():
        Unknown26('laef401punch')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(2500)
    Unknown1072(235000)
    GFX_1('laef_burner_add401', 100)

@State
def laef401punch_b():

    def upon_IMMEDIATE():
        Unknown26('laef401punch_b')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_0('laef_burner_loop', 100)
    Unknown1056(2000)
    Unknown1064(2500)
    Unknown1072(305000)

@State
def laef401smoke():

    def upon_IMMEDIATE():
        Unknown4007(2)
        teleportRelativeX(256000)
    sprite('null', 1)	# 1-1

@State
def laef401smoke_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        teleportRelativeX(272000)
        Unknown1007(-16000)
    sprite('null', 1)	# 1-1

@State
def laef404clash():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    GFX_1('laef_404_clash', 100)

@State
def laef404clash_r():

    def upon_IMMEDIATE():
        Unknown2005()
    sprite('null', 1)	# 1-1
    Unknown4049(500)
    Unknown4045('6c6165665f3430345f636c61736800000000000000000000000000000000000064000000')

@State
def LandingImpactA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(40)
        AirPushbackX(0)
        AirPushbackY(-50000)
        Unknown9310(1)
        Unknown11056(3)
        Unknown23182(3)
        Unknown1056(1200)
    sprite('vr_la405atkcol', 6)	# 1-6
    ScreenShake(0, 15000)

@State
def LandingImpactB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(40)
        AirPushbackX(0)
        AirPushbackY(-50000)
        Unknown9310(1)
        Unknown11056(3)
        Unknown23182(3)
        Unknown1056(1300)
    sprite('vr_la405atkcol', 6)	# 1-6
    ScreenShake(0, 15000)

@State
def LandingImpactAB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(1200)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(40)
        AirPushbackX(0)
        AirPushbackY(-50000)
        Unknown9310(1)
        Unknown11056(3)
        Unknown23182(3)
        Unknown30065(0)
        Unknown11091(10)
        Unknown1056(1400)
    sprite('vr_la405atkcol', 6)	# 1-6
    ScreenShake(0, 15000)

@State
def laef_405clash_l():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown4049(800)
    Unknown4045('6c6165665f3430345f636c61736800000000000000000000000000000000000064000000')

@State
def laef_405clash_r():

    def upon_IMMEDIATE():
        Unknown2005()
    sprite('null', 1)	# 1-1
    Unknown4049(800)
    Unknown4045('6c6165665f3430345f636c61736800000000000000000000000000000000000064000000')

@State
def laef430slasher():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(16000)
        teleportRelativeX(-8000)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('laef_430_slasher', 100)
    gotoLabel(0)

@State
def laef430slasher_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(48000)
        teleportRelativeX(64000)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('laef_430_slasher_b', 100)
    gotoLabel(0)

@State
def laef432_charge():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    label(0)
    sprite('null', 5)	# 1-5
    GFX_1('laef_432_charge', 100)
    gotoLabel(0)

@State
def laef432_fire():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f3433325f666972652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3033()
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(6)
    sprite('null', 16)	# 1-16
    Unknown1056(1125)

@State
def __450rasen():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f636d6e726173656e2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3032()
        Unknown4015()
    sprite('null', 9)	# 1-9
    GFX_0('Cmnrasen', 100)
    sprite('null', 9)	# 10-18
    GFX_0('Cmnrasen', 100)
    sprite('null', 9)	# 19-27
    GFX_0('Cmnrasen', 100)
    sprite('null', 9)	# 28-36
    GFX_0('Cmnrasen', 100)
    sprite('null', 10)	# 37-46
    Unknown3004(-26)

@State
def Ichigeki_atk():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(100)
        Hitstop(5)
        Unknown11064(1)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(10000)
        Unknown9310(60)
        PushbackX(0)
        Unknown11072(1, 1000000, 80000)
        AirHitstunAnimation(5)
        GroundedHitstunAnimation(5)
        Unknown11094(1)
        Unknown11033(3)
        Unknown11031(0)

        def upon_78():
            clearUponHandler(78)
            Unknown21015('41737472616c48656174000000000000000000000000000000000000000000008913000000000000')
            Unknown21015('504c415f506572736f6e614963686967656b69000000000000000000000000008a13000000000000')
            Unknown36(22)
            Unknown23086(1)
            Unknown1084(1)
            Unknown2017(0)
            Unknown2053(0)
            Unknown2034(0)
            Unknown35()
        GFX_0('450line', 100)
    sprite('vr_lp450atkcol', 10)	# 1-10
    Unknown23027()
    sprite('vr_lp450atkcol', 15)	# 11-25
    RefreshMultihit()
    Unknown1059(120)
    sprite('vr_lp450atkcol', 30)	# 26-55
    Unknown23027()
    loopRest()

@State
def __450zan():

    def upon_IMMEDIATE():
        Unknown1096(1100)
        Unknown23151(22, 103)
    sprite('null', 22)	# 1-22
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 23-44
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 45-66
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 67-88
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 89-110
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 111-132
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 133-154
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 155-176
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 177-198
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 199-220
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 221-242
    GFX_1('laef_450zanE', 100)

@State
def laef450_zanhit():

    def upon_IMMEDIATE():
        Unknown23067('laef450_zanhit')
        Unknown23151(22, 103)
    sprite('null', 15)	# 1-15

@State
def __450zanhit():

    def upon_IMMEDIATE():
        Unknown1096(2000)
        Unknown23151(22, 103)
    sprite('null', 60)	# 1-60
    GFX_1('laef450_zanhit', 100)
    GFX_1('laef450_zanhit', 100)

@State
def __450speedline():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23067('laef_450speedline')
        Unknown4007(2)
        Unknown3001(0)
    sprite('null', 250)	# 1-250
    Unknown3004(20)
    sprite('null', 15)	# 251-265
    Unknown3004(-17)

@State
def __450line():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 70)	# 1-70
    GFX_0('450lineatk', 100)

@State
def __450lineatk():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown4003('6c6165665f3435306c696e652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(2000)
        Unknown3001(0)
        teleportRelativeY(60000)
    sprite('null', 20)	# 1-20
    Unknown3004(50)
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def __450kumonosu():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown4003('6c6165665f3435306b756d6f6e6f73752e4449470000000000000000000000006c6165665f3435306b756d6f6e6f73755f3030302e6d6d6f7400000000000000')
        Unknown3032()
        Unknown3001(0)
        teleportRelativeX(-50000)
        Unknown23151(22, 103)
    sprite('null', 30)	# 1-30
    Unknown3004(30)
    sprite('null', 35)	# 31-65
    Unknown23119(255, 10, 3)
    sprite('null', 15)	# 66-80
    Unknown23117(16711680, 30)
    Unknown3004(-17)

@State
def __450bukinage():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(0)
        Unknown3032()
        physicsXImpulse(55000)
        physicsYImpulse(8000)
    sprite('la450_13a', 1)	# 1-1
    GFX_0('450bukinage_sub', 100)
    SFX_3('slash_blade_fast')
    sprite('la450_13c', 2)	# 2-3
    SFX_3('slash_blade_fast')
    sprite('la450_13b', 2)	# 4-5
    sprite('la450_13a', 2)	# 6-7
    sprite('la450_13c', 2)	# 8-9
    SFX_3('slash_blade_fast')
    sprite('la450_13b', 2)	# 10-11
    sprite('la450_13a', 2)	# 12-13
    sprite('la450_13c', 2)	# 14-15
    sprite('la450_13b', 2)	# 16-17
    Unknown23117(6553600, 34)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SFX_3('slash_blade_fast')
    sprite('la450_13a', 2)	# 18-19
    sprite('la450_13c', 2)	# 20-21
    sprite('la450_13b', 2)	# 22-23
    SFX_3('slash_blade_fast')
    sprite('la450_13a', 2)	# 24-25
    sprite('la450_13c', 2)	# 26-27
    sprite('la450_13b', 2)	# 28-29
    sprite('la450_13a', 2)	# 30-31
    SFX_3('slash_blade_fast')
    sprite('la450_13c', 2)	# 32-33
    sprite('la450_13a', 2)	# 34-35
    sprite('la450_13c', 2)	# 36-37
    sprite('la450_13b', 5)	# 38-42
    Unknown23117(16711680, 5)
    Unknown3004(-51)

@State
def __450bukinage_sub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23067('laef450_bukinage')
        Unknown1096(950)
        Unknown1007(135000)
    sprite('null', 15)	# 1-15
    sprite('null', 24)	# 16-39
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('null', 12)	# 40-51
    Unknown1099(110)
    Unknown23119(16711680, 20, 1)
    Unknown3004(-22)

@State
def __450zan():

    def upon_IMMEDIATE():
        Unknown1096(1100)
    sprite('null', 22)	# 1-22
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 23-44
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 45-66
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 67-88
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 89-110
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 111-132
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 133-154
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 155-176
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 177-198
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 199-220
    GFX_1('laef_450zanE', 100)
    sprite('null', 22)	# 221-242
    GFX_1('laef_450zanE', 100)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
        Unknown2007()
        Unknown6001(1)
        teleportRelativeY(400000)
        Unknown1000(-200000)
        Unknown1096(2000)
        Unknown23013(0)
    sprite('ichigeki', 35)	# 1-35
    sprite('ichigeki', 20)	# 36-55
    GFX_0('450eyelight', 100)
    GFX_0('450onolight', 100)
    physicsXImpulse(-10000)
    physicsYImpulse(-8000)
    GFX_0('450cutinbg', 100)
    GFX_0('450centerline', 100)
    Unknown1099(-50)
    Unknown3004(20)
    sprite('ichigeki', 2)	# 56-57
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('ichigeki', 90)	# 58-147
    physicsYImpulse(-200)
    sprite('ichigeki', 15)	# 148-162
    Unknown21015('3435306579656c696768740000000000000000000000000000000000000000008b13000000000000')
    Unknown21015('3435306f6e6f6c696768740000000000000000000000000000000000000000008b13000000000000')
    sprite('ichigeki', 2)	# 163-164
    Unknown1099(10)
    physicsXImpulse(2500)
    physicsYImpulse(-8000)
    sprite('ichigeki', 2)	# 165-166
    physicsYImpulse(-9000)
    sprite('ichigeki', 2)	# 167-168
    physicsYImpulse(-10000)
    sprite('ichigeki', 2)	# 169-170
    physicsYImpulse(-11000)
    sprite('ichigeki', 12)	# 171-182
    sprite('ichigeki', 30)	# 183-212
    Unknown23119(10198015, 30, 1)
    Unknown3004(-8)

@State
def __450cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f34353062672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 155)	# 1-155
    Unknown3004(10)
    sprite('null', 50)	# 156-205
    Unknown3004(-6)

@State
def __450centerline():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23015(4)
        Unknown23067('laef_syasen')
        teleportRelativeX(250000)
        teleportRelativeY(300000)
        Unknown1096(800)
        Unknown3001(0)
    sprite('null', 170)	# 1-170
    Unknown3004(30)
    physicsYImpulse(250)
    sprite('null', 15)	# 171-185
    Unknown3004(-17)

@State
def __450eyelight():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown4007(2)
        teleportRelativeX(380000)
        teleportRelativeY(85000)
        Unknown1096(700)
        Unknown3001(0)
        Unknown23013(0)

        def upon_43():
            if (SLOT_48 == 5003):
                sendToLabel(0)
    sprite('vr_la450_eye00', 15)	# 1-15
    sprite('vr_la450_eye00', 140)	# 16-155
    Unknown3004(20)
    label(0)
    sprite('vr_la450_eye00', 15)	# 156-170
    clearUponHandler(43)
    Unknown3004(-17)

@State
def __450onolight():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23067('laef_450onoef')
        Unknown4007(2)
        teleportRelativeX(360000)
        teleportRelativeY(570000)
        Unknown1096(580)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 5003):
                sendToLabel(0)
    sprite('null', 27)	# 1-27
    sprite('null', 128)	# 28-155
    Unknown3004(20)
    label(0)
    sprite('null', 15)	# 156-170
    clearUponHandler(43)
    Unknown3004(-17)

@State
def IchigekiBlack():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown3001(0)
        Unknown1096(10000)
        Unknown23015(4)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 5006):
                sendToLabel(0)
        Unknown3004(20)
    sprite('vr_la450_black', 32767)	# 1-32767
    label(0)
    sprite('vr_la450_black', 10)	# 32768-32777
    Unknown3004(-26)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5004):
                sendToLabel(0)
            if (SLOT_48 == 5005):
                sendToLabel(1)
        Unknown20003(1)
        Unknown2053(0)
        Unknown2034(0)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20003(0)
    label(0)
    sprite('null', 32767)	# 1-32767
    Unknown20000(1)

    def upon_3():
        Unknown1086(3)
        teleportRelativeX(420000)
    loopRest()
    label(1)
    sprite('null', 32767)	# 32768-65534
    clearUponHandler(3)
    Unknown20000(1)
    Unknown1000(0)
    loopRest()

@State
def __450todome():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown4003('6c6165665f343530746f646f6d652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1700)
        Unknown3001(0)
        Unknown23151(22, 103)
    sprite('null', 14)	# 1-14
    GFX_1('laef_450todome', 100)
    Unknown3004(80)
    sprite('null', 6)	# 15-20
    Unknown3004(-43)

@State
def Ichigeki_todome():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(12000)
        Unknown11091(100)
        Hitstop(0)
        Unknown11064(3)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(100000)
        Unknown9016(1)
        Unknown11023(1)
        Unknown23151(22, 103)
    sprite('vr_la450_01atkcol', 10)	# 1-10
    RefreshMultihit()
    loopRest()

@State
def __450tvbreak():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        teleportRelativeY(280000)
    sprite('null', 1)	# 1-1
    GFX_1('laef450_break', 100)
    SFX_3('ice_break_fast')
    sprite('null', 1)	# 2-2
    SFX_3('chain_snap')
    sprite('null', 1)	# 3-3
    SFX_3('ice_break_fast')
    sprite('null', 2)	# 4-5
    SFX_3('chain_snap')
    sprite('null', 60)	# 6-65
    GFX_1('laef450_break', 100)

@State
def __450TVnoise():

    def upon_IMMEDIATE():
        Unknown4003('6c6165665f34353074766e6f6973652e444947000000000000000000000000006c6165665f34353074766e6f6973655f3030302e6d6d6f740000000000000000')
        Unknown23015(4)
        Unknown3032()
        Unknown3001(0)
        Unknown1096(1100)
    sprite('null', 15)	# 1-15
    Unknown3004(12)
    SFX_3('whitenoize')
    sprite('null', 15)	# 16-30
    SFX_3('whitenoize')
    sprite('null', 80)	# 31-110
    SFX_3('whitenoize')
    sprite('null', 5)	# 111-115
    Unknown3004(-51)

@State
def __610winline():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23015(1)
        Unknown4003('6c6165665f36313077696e6c696e652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1400)
        Unknown3001(0)
        Unknown4015()
    sprite('null', 25)	# 1-25
    sprite('null', 10)	# 26-35
    GFX_0('610floor', 100)
    GFX_0('610handaura', 100)
    sprite('null', 32767)	# 36-32802
    Unknown3004(8)
    sprite('null', 20)	# 32803-32822
    Unknown3004(-13)

@State
def __610floor():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23067('lpef_433floor')
        Unknown1096(700)
        teleportRelativeX(200000)
        Unknown1007(-40000)
    sprite('null', 32767)	# 1-32767
    sprite('null', 15)	# 32768-32782
    Unknown3004(-17)

@State
def __610handaura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23067('lpef_610handaura')
        teleportRelativeX(95000)
        Unknown1007(450000)
    sprite('null', 32767)	# 1-32767
    sprite('null', 15)	# 32768-32782
    Unknown3004(-17)

@State
def WinCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
    sprite('null', 32767)	# 1-32767

@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)	# 1-1
    GFX_0('P4U_Cutin_Face', 100)

@State
def P4U_Cutin_Face():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown2054(1)
        Unknown13044(0)
        Unknown6001(1)
        Unknown1000(-650000)
        teleportRelativeY(-292000)
        Unknown1096(1350)
        Unknown2037(0)
        Unknown3001(0)

        def upon_3():
            if (SLOT_2 == 2):
                Unknown1007(15000)
                Unknown3001(150)
            if (SLOT_2 == 3):
                Unknown1007(-30000)
                Unknown3001(180)
            if (SLOT_2 == 4):
                Unknown1007(25000)
                Unknown3001(210)
            if (SLOT_2 == 5):
                Unknown1007(-20000)
                Unknown3001(255)
            if (SLOT_2 == 6):
                Unknown1007(10000)
            Unknown2038(1)
    sprite('vr_99p4u_face00', 45)	# 1-45
    SFX_0('spsys_over_power')
    SFX_0('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)	# 46-46
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)	# 47-47
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)	# 48-48
    Unknown3001(60)

@State
def P4U_ka_JPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi', 1)	# 1-1
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)	# 2-2
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)	# 3-3
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)	# 4-4
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)	# 5-5
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)	# 6-6
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)	# 7-7
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)	# 8-45
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)	# 46-46
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi', 1)	# 47-47
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi', 1)	# 48-48
    Unknown3001(60)
    Unknown1096(100)

@State
def P4U_ka_NotJPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 1-1
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 2-2
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 3-3
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 4-4
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 5-5
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 6-6
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 7-7
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)	# 8-45
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 46-46
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 47-47
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 48-48
    Unknown3001(60)
    Unknown1096(100)