@Subroutine
def rwief_slash_func():
    Unknown4010(3)
    Unknown4011(3)
    Unknown4007(2)
    Unknown4009(2)
    Unknown4061(1)
    Unknown3033()

@Subroutine
def rwief_slash_dust_func():
    Unknown4009(2)
    Unknown4007(2)
    Unknown4013(2)
    Unknown4006(2)
    Unknown4025(2)
    Unknown4011(3)
    Unknown4061(1)

@State
def rwief_slash_dust_16():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
    sprite('null', 3)	# 1-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f6475737441000000000000000000000000000000ffffffff')
    sprite('null', 3)	# 4-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f6475737441000000000000000000000000000000ffffffff')
    sprite('null', 3)	# 7-9
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f6475737441000000000000000000000000000000ffffffff')
    sprite('null', 3)	# 10-12
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f360000000000000000000000000000ffffffff')

@State
def rwief_slash_dust_18():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
    sprite('null', 3)	# 1-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')

@State
def rwief_slash_dust_20():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
    sprite('null', 3)	# 1-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000000000000')

@State
def rwief_slash_dust_22():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
    sprite('null', 3)	# 1-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000000000000')

@State
def rwief_slash_dust_24():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
    sprite('null', 3)	# 1-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31340000000000000000000000000000000000')

@State
def rwief_slash_dust_26():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
    sprite('null', 3)	# 1-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')

@State
def rwief_slash_dustA_loop():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_dust_func')
        Unknown2055(60)
        Unknown4010(2)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573744100000000000000000000000000000000000000')
    gotoLabel(0)

@Subroutine
def MagicImage_Func():
    Unknown4061(1)
    Unknown23122(24)
    Unknown3033()
    Unknown23015(15)

@Subroutine
def MagicImageB_Func():
    Unknown3032()
    Unknown4061(1)
    Unknown21004(24)
    Unknown23015(15)

@State
def MagicImage30f_test():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
    sprite('null', 30)	# 1-30
    Unknown4003('72776965665f676c7970685f73746172743330662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 31-32797
    Unknown4003('72776965665f676c7970685f6c6f6f70322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def MagicImageB_30ftest():

    def upon_IMMEDIATE():
        callSubroutine('MagicImageB_Func')
    sprite('null', 30)	# 1-30
    Unknown4003('72776965665f676c797068425f73746172743330662e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 31-32797
    Unknown4003('72776965665f676c797068425f6c6f6f70322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief200_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
    sprite('null', 7)	# 1-7
    GFX_0('rwief200_slash_Model', -1)
    GFX_0('rwief200_slash_Bloom', -1)
    GFX_0('rwief201_EX_Dummy', -1)

@State
def rwief200_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663230305f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(3700)
        Unknown23122(64)
        teleportRelativeX(150000)
        Unknown1007(275000)
    sprite('null', 3)	# 1-3
    sprite('null', 4)	# 4-7
    teleportRelativeX(-5000)
    Unknown1007(1000)

@State
def rwief200_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
    sprite('vref_rwi200_00b', 3)	# 1-3
    Unknown3004(-20)
    sprite('vref_rwi200_01b', 4)	# 4-7
    Unknown3004(-60)

@State
def rwief201_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
    sprite('vref_rwi200_00b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000002000000')

@State
def rwief201_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4009(0)
    sprite('vref_rwi201_00', 3)	# 1-3
    GFX_0('rwief201_slash_Flare', -1)
    sprite('null', 12)	# 4-15
    GFX_0('rwief201_slash_Model', -1)
    GFX_0('rwief201_slash_Bloom', -1)
    GFX_0('rwief201_EX_Dummy', -1)

@State
def rwief201_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663230315f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(4700)
        Unknown23122(64)
        teleportRelativeX(465000)
        Unknown1007(270000)
        physicsXImpulse(4000)
    sprite('null', 1)	# 1-1
    sprite('null', 5)	# 2-6
    Unknown1067(-300)
    Unknown1059(-150)
    sprite('null', 4)	# 7-10
    Unknown1067(-500)

@State
def rwief201_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        physicsXImpulse(2000)
        Unknown1007(3000)
    sprite('vref_rwi201_01b', 1)	# 1-1
    sprite('keep', 5)	# 2-6
    Unknown1067(-63)
    physicsYImpulse(17000)
    Unknown3004(-31)
    sprite('keep', 1)	# 7-7
    Unknown1067(-106)
    physicsYImpulse(28322)

@State
def rwief201_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(700)
    sprite('null', 3)	# 1-3
    teleportRelativeX(240000)
    Unknown1007(275000)
    Unknown1099(-50)
    physicsXImpulse(1000)

@State
def rwief201_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
    sprite('vref_rwi201_01b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    sprite('keep', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000002000000')
    sprite('keep', 12)	# 3-14
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000003000000')

@State
def rwief202_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
    sprite('null', 10)	# 1-10
    GFX_0('rwief202_slash_Model', 0)
    GFX_0('rwief202_slash_Bloom', 0)
    GFX_0('rwief202_EX_Dummy', 0)

@State
def rwief202_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        Unknown1096(3700)
        teleportRelativeX(5000)
        Unknown1007(247000)
    sprite('null', 5)	# 1-5
    Unknown4003('72776965663230325f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(61)
    sprite('null', 5)	# 6-10
    Unknown1099(30)

@State
def rwief202_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(5000)
        Unknown1007(247000)
    sprite('vref_rwi202_00b', 2)	# 1-2
    Unknown1099(16)
    Unknown3001(200)
    sprite('keep', 3)	# 3-5
    Unknown3004(-33)
    sprite('keep', 3)	# 6-8
    Unknown1099(8)

@State
def rwief202_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(5000)
        Unknown1007(247000)
        Unknown1096(1100)
        Unknown3038(1)
    sprite('vref_rwi202_00b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000005000000')
    sprite('vref_rwi202_00b', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000007000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3230000000000000000000000000000a000000')

@State
def rwief203_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(0)
        teleportRelativeX(-30000)
        Unknown1007(270000)
        Unknown3038(1)
    sprite('vref_rwi203_00b', 2)	# 1-2
    GFX_0('rwief203_slash_Model', 100)
    GFX_0('rwief203_slash_Bloom', 100)
    sprite('keep', 1)	# 3-3
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_16', 1)
    GFX_0('rwief_slash_dust_18', 2)
    GFX_0('rwief_slash_dust_16', 3)
    GFX_0('rwief_slash_dust_18', 4)
    GFX_0('rwief_slash_dust_20', 5)
    GFX_0('rwief_slash_dust_18', 6)
    GFX_0('rwief_slash_dust_20', 7)
    GFX_0('rwief_slash_dust_22', 8)
    GFX_0('rwief_slash_dust_24', 9)
    GFX_0('rwief_slash_dust_22', 10)
    GFX_0('rwief_slash_dust_26', 11)
    sprite('null', 7)	# 4-10
    Unknown4007(0)

@State
def rwief203_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663230335f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(0)
        Unknown1096(3500)
        Unknown23122(64)
    sprite('null', 4)	# 1-4
    Unknown1099(87)
    sprite('null', 6)	# 5-10
    Unknown1099(23)

@State
def rwief203_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(0)
    sprite('vref_rwi203_00b', 2)	# 1-2
    Unknown1099(25)
    sprite('keep', 2)	# 3-4
    Unknown3004(-42)
    sprite('keep', 6)	# 5-10
    Unknown1099(6)

@State
def rwief231_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
    sprite('vref_rwi231_00', 2)	# 1-2
    GFX_0('rwief231_slash_Flare', 100)
    sprite('null', 12)	# 3-14
    GFX_0('rwief231_slash_Model', 100)
    GFX_0('rwief231_slash_Bloom', 100)
    GFX_0('rwief231_EX_Dummy', 100)

@State
def rwief231_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663233315f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(5000)
        Unknown1067(-100)
        teleportRelativeX(400000)
        Unknown1007(19000)
        Unknown1072(27000)
        physicsXImpulse(2580)
        physicsYImpulse(-1500)
    sprite('null', 4)	# 1-4
    sprite('null', 8)	# 5-12
    physicsXImpulse(860)
    physicsYImpulse(-500)

@State
def rwief231_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown1067(-20)
        teleportRelativeX(400000)
        Unknown1007(19000)
        Unknown1072(27000)
        physicsXImpulse(2580)
        physicsYImpulse(-1500)
    sprite('vref_rwi231_01b', 2)	# 1-2
    sprite('vref_rwi231_01b', 2)	# 3-4
    Unknown3004(-25)
    sprite('vref_rwi231_02b', 3)	# 5-7
    physicsXImpulse(860)
    physicsYImpulse(-500)
    sprite('vref_rwi231_03b', 5)	# 8-12

@State
def rwief231_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown1067(-20)
        teleportRelativeX(400000)
        Unknown1007(19000)
        Unknown1072(27000)
        physicsXImpulse(2580)
        physicsYImpulse(-1500)
    sprite('vref_rwi231_01b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000003000000')
    sprite('vref_rwi231_01b', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000006000000')
    sprite('vref_rwi231_01b', 1)	# 3-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000007000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000009000000')

@State
def rwief231_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(400)
        Unknown1099(100)
    sprite('null', 2)	# 1-2
    Unknown1000(150000)
    teleportRelativeY(100000)

@State
def rwief232_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(-2000)
        Unknown1007(2000)
    sprite('vref_rwi232_00', 3)	# 1-3
    GFX_0('rwief232_slash_Flare', 100)
    GFX_0('rwief232_EX_Dummy', 100)
    sprite('vref_rwi232_01', 3)	# 4-6
    GFX_0('rwief232_slash_Model', 100)
    GFX_0('rwief232_slash_Bloom', 100)
    sprite('vref_rwi232_02', 3)	# 7-9
    sprite('null', 3)	# 10-12
    Unknown3004(-85)
    sprite('null', 35)	# 13-47

@State
def rwief232_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        Unknown1096(4000)
        teleportRelativeX(-5000)
        Unknown1007(75000)
    sprite('null', 5)	# 1-5
    Unknown4003('72776965663233325f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(30)
    sprite('null', 5)	# 6-10
    Unknown1099(10)
    sprite('null', 2)	# 11-12
    Unknown1099(0)

@State
def rwief232_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
    sprite('vref_rwi232_01b', 3)	# 1-3
    Unknown1099(10)
    sprite('vref_rwi232_01b', 6)	# 4-9
    Unknown3004(-42)

@State
def rwief232_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
    sprite('null', 3)	# 1-3
    teleportRelativeX(-56000)
    Unknown1007(-41000)
    sprite('null', 3)	# 4-6
    teleportRelativeX(22000)
    Unknown1007(270000)
    Unknown1096(600)
    Unknown1099(-66)
    sprite('null', 3)	# 7-9
    teleportRelativeX(90000)
    Unknown1007(7000)
    Unknown3004(-85)

@State
def rwief232_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
    sprite('vref_rwi232_00', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    sprite('keep', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000001000000')
    sprite('keep', 1)	# 3-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000003000000')
    sprite('vref_rwi232_01', 1)	# 4-4
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000001000000')
    sprite('keep', 1)	# 5-5
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000004000000')

@State
def rwief251_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        sendToLabelUpon(32, 0)
    sprite('vref_rwi251_00', 3)	# 1-3
    GFX_0('rwief251_slash_Flare', 0)
    sprite('null', 60)	# 4-63
    label(0)
    sprite('null', 4)	# 64-67
    GFX_0('rwief251_slash_Model', 0)
    GFX_0('rwief251_slash_Bloom', 0)
    GFX_0('rwief251_EX_Dummy', 0)
    sprite('null', 3)	# 68-70
    Unknown4007(0)

@State
def rwief251_slash_Model():

    def upon_IMMEDIATE():
        Unknown4003('72776965663235315f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        teleportRelativeX(390000)
        Unknown1007(297000)
        Unknown1056(3330)
        Unknown1064(4070)
        physicsXImpulse(8000)
        Unknown1059(37)
        Unknown1067(-37)
    sprite('null', 3)	# 1-3
    sprite('null', 4)	# 4-7
    Unknown1059(-123)
    Unknown1066(80)

@State
def rwief251_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(390000)
        Unknown1007(297000)
        Unknown1056(900)
        Unknown1064(1100)
        physicsXImpulse(8000)
        Unknown1059(10)
        Unknown1067(-10)
    sprite('vref_rwi251_01b', 3)	# 1-3
    Unknown3004(-31)
    sprite('vref_rwi251_02b', 2)	# 4-5
    Unknown1066(80)
    Unknown1059(-33)
    sprite('vref_rwi251_03b', 2)	# 6-7

@State
def rwief251_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(300)
        Unknown1099(150)
    sprite('null', 3)	# 1-3
    Unknown1000(180000)
    teleportRelativeY(285000)

@State
def rwief251_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        teleportRelativeX(390000)
        Unknown1007(297000)
        Unknown1056(900)
        Unknown1064(1100)
        physicsXImpulse(8000)
        Unknown1059(10)
        Unknown1067(-10)
    sprite('vref_rwi251_01b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000001000000')
    sprite('vref_rwi251_01b', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000003000000')
    sprite('vref_rwi251_01b', 1)	# 3-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000005000000')

@State
def rwief252_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(-20000)
        Unknown1007(270000)
    sprite('vref_rwi252_00', 3)	# 1-3
    GFX_0('rwief252_slash_Model', 100)
    GFX_0('rwief252_slash_Bloom', 100)
    GFX_0('rwief252_slash_Flare', 100)
    GFX_0('rwief252_EX_Dummy', 100)
    sprite('null', 7)	# 4-10
    Unknown4007(0)

@State
def rwief252_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        Unknown4003('72776965663235325f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(3700)
        physicsXImpulse(-1000)
        physicsYImpulse(1000)
    sprite('null', 1)	# 1-1
    sprite('null', 4)	# 2-5
    Unknown1099(74)
    sprite('null', 5)	# 6-10
    Unknown1099(37)

@State
def rwief252_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(-2000)
        Unknown1007(-5000)
        physicsXImpulse(-600)
        physicsYImpulse(800)
    sprite('vref_rwi252_00b', 1)	# 1-1
    sprite('keep', 4)	# 2-5
    Unknown1099(20)
    Unknown3004(-42)
    sprite('keep', 5)	# 6-10
    Unknown1099(10)

@State
def rwief252_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(800)
        Unknown1099(-150)
    sprite('null', 3)	# 1-3
    teleportRelativeX(-18000)
    Unknown1007(250000)

@State
def rwief252_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
    sprite('vref_rwi252_00', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000001000000')
    sprite('keep', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000003000000')
    sprite('keep', 1)	# 3-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000005000000')
    sprite('keep', 1)	# 4-4
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000007000000')
    sprite('keep', 1)	# 5-5
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000009000000')

@State
def rwief270_wind():

    def upon_IMMEDIATE():
        Unknown4003('72776965663237305f77696e6430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        Unknown1096(4200)
        teleportRelativeX(-30000)
        Unknown1007(340000)
        Unknown3001(200)
        Unknown3007(230)
        Unknown3013(245)
    sprite('null', 10)	# 1-10

@State
def rwief270_wind2():

    def upon_IMMEDIATE():
        Unknown4003('72776965663237305f77696e6430322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        Unknown1056(3700)
        Unknown1064(4000)
        teleportRelativeX(-125000)
        Unknown1007(130000)
        Unknown3001(200)
        Unknown3007(230)
        Unknown3013(245)
    sprite('null', 11)	# 1-11

@State
def rwief271_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4009(2)
        Unknown1000(-50000)
        teleportRelativeY(5000)
        Unknown23015(1)
    sprite('vref_rwi271_00', 3)	# 1-3
    GFX_0('rwief271_slash_Flare', 100)
    sprite('keep', 1)	# 4-4
    Unknown3038(1)
    GFX_0('rwief271_slash_Model', 100)
    GFX_0('rwief271_slash_Bloom', 100)
    GFX_0('rwief271_Bloom', 100)
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_18', 1)
    GFX_0('rwief_slash_dust_20', 2)
    sprite('keep', 1)	# 5-5
    GFX_0('rwief_slash_dust_20', 3)
    GFX_0('rwief_slash_dust_22', 4)
    sprite('keep', 13)	# 6-18
    GFX_0('rwief_slash_dust_24', 5)
    GFX_0('rwief_slash_dust_26', 6)

@State
def rwief271_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4009(2)
        Unknown4003('72776965663237315f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1056(6000)
        Unknown1064(4400)
        Unknown23122(64)
        teleportRelativeX(440000)
        Unknown1007(145000)
        physicsXImpulse(8000)
        Unknown1066(80)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1059(-100)
    Unknown1067(-200)
    sprite('null', 3)	# 4-6
    Unknown1058(80)
    Unknown1066(70)
    sprite('null', 7)	# 7-13
    Unknown1099(-120)

@State
def rwief271_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4009(2)
        teleportRelativeX(440000)
        Unknown1007(145000)
        physicsXImpulse(8000)
        Unknown1056(1500)
        Unknown1064(1100)
        Unknown1066(80)
        Unknown23015(6)
    sprite('vref_rwi271_01b', 1)	# 1-1
    sprite('keep', 2)	# 2-3
    Unknown1059(-25)
    Unknown1067(-50)
    Unknown3004(-21)
    sprite('keep', 3)	# 4-6
    Unknown1058(80)
    Unknown1066(70)
    sprite('vref_rwi271_02b', 7)	# 7-13
    Unknown1099(-30)

@State
def rwief271_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4009(2)
        teleportRelativeX(130000)
        Unknown1007(145000)
        physicsXImpulse(13000)
        Unknown1056(6500)
        Unknown1064(1000)
        Unknown21004(64)
    sprite('null', 2)	# 1-2
    Unknown4054(15)
    Unknown4047(64, 64, 64)
    Unknown23067('rwief271_bloom')
    sprite('null', 13)	# 3-15
    Unknown3004(-19)

@State
def rwief271_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(900)
    sprite('null', 3)	# 1-3
    teleportRelativeX(310000)
    Unknown1007(185000)
    Unknown1099(-50)
    physicsXImpulse(1000)

@State
def rwief272_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(-2000)
        Unknown1007(2000)
    sprite('vref_rwi272_00', 2)	# 1-2
    GFX_0('rwief272_slash_Flare', 0)
    sprite('null', 11)	# 3-13
    GFX_0('rwief272_slash_Model', 0)
    GFX_0('rwief272_slash_Bloom', 0)
    GFX_0('rwief272_EX_Dymmu', 0)

@State
def rwief272_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        Unknown1096(3800)
        teleportRelativeX(57000)
        Unknown1007(265000)
        physicsXImpulse(1500)
    sprite('null', 5)	# 1-5
    Unknown4003('72776965663237325f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(30)
    sprite('null', 5)	# 6-10
    Unknown1099(10)
    sprite('null', 1)	# 11-11
    Unknown1099(0)

@State
def rwief272_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        physicsXImpulse(1500)
        physicsYImpulse(-2000)
    sprite('vref_rwi272_01b', 3)	# 1-3
    Unknown1099(10)
    Unknown3001(200)
    sprite('vref_rwi272_01b', 6)	# 4-9
    Unknown3004(-36)

@State
def rwief272_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
    sprite('null', 2)	# 1-2
    teleportRelativeX(228000)
    Unknown1007(242000)

@State
def rwief272_EX_Dymmu():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        teleportRelativeX(15000)
    sprite('vref_rwi272_01b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000004000000')
    sprite('vref_rwi272_01b', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000007000000')

@State
def rwief272_slash_b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown3033()
    sprite('vref_rwi272_00b', 16)	# 1-16
    Unknown3004(-16)

@State
def __5AAAAObj():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4061(2)
        AttackLevel_(4)
        Damage(2000)
        AirPushbackY(20000)
        AirPushbackX(-7500)
        PushbackX(-12000)
        Hitstop(18)
        AirUntechableTime(30)
        Unknown11058('0000000000000000000000000100000000000000')
        if (SLOT_19 > 500000):
            Unknown48('190000000200000053000000160000000200000053000000')
            teleportRelativeX(350000)
        else:
            teleportRelativeX(450000)
        Unknown3033()
        Unknown9021(1)
        Unknown9266(9)
        Unknown1096(1000)
        Unknown3001(255)
        Unknown23089('0100000000000000000000000000000000000000010000000100000001000000')

        def upon_54():
            Unknown23027()
        Unknown2034(1)
        Unknown2053(1)
        Unknown3038(1)
    sprite('vrjnef233atk_00', 3)	# 1-3
    Unknown1099(-5)
    SFX_3('rwise_42')
    sprite('vrjnef233atk_01', 3)	# 4-6
    GFX_0('rwief_Afinish', -1)
    Unknown1096(800)
    Unknown1099(-5)
    sprite('vrjnef233atk_02ex01', 3)	# 7-9
    Unknown1096(900)
    Unknown1099(0)
    sprite('vrjnef233atk_02', 3)	# 10-12	 **attackbox here**
    Unknown1096(1000)
    Unknown1099(5)
    sprite('vrjnef233atk_03', 3)	# 13-15
    Unknown1099(0)
    Unknown3001(200)
    Unknown3004(-15)
    sprite('vrjnef233atk_04', 3)	# 16-18
    sprite('vrjnef233atk_05', 10)	# 19-28

@State
def rwief_Afinish():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4011(3)
        Unknown4007(2)
        Unknown4015()
        Unknown23015(9)
        Unknown4061(1)
        Unknown1096(3500)
        Unknown1099(35)
        Unknown3032()
        teleportRelativeY(10000)
        teleportRelativeX(-50000)
    sprite('null', 1)	# 1-1
    Unknown4003('72776965665f4166696e69736830312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(4)
    GFX_0('rwief_Afinish_Bloom', -1)
    GFX_0('rwief_Afinish_Ground', -1)
    GFX_0('rwief_Afinish_Create', -1)
    GFX_0('rwief_Afinish_Break', -1)
    GFX_0('rwief_Afinish_IcedGround', -1)
    sprite('null', 1)	# 2-2
    Unknown23122(16)
    sprite('null', 1)	# 3-3
    Unknown23122(32)
    sprite('null', 2)	# 4-5
    Unknown4003('72776965665f4166696e69736830322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    sprite('null', 1)	# 6-6
    sprite('null', 19)	# 7-25
    Unknown4003('72776965665f4166696e69736830332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(6)
    Unknown1099(0)

@State
def rwief_Afinish_Bloom():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown23015(10)
        Unknown4061(1)
        Unknown1096(1000)
        Unknown1099(10)
        Unknown3033()
        Unknown3003(30)
    sprite('vref_rwi_Afinish00', 3)	# 1-3
    sprite('vref_rwi_Afinish01', 3)	# 4-6
    sprite('vref_rwi_Afinish02', 19)	# 7-25
    Unknown1099(0)

@State
def rwief_Afinish_Ground():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown23015(10)
        Unknown3000(0)
        Unknown4061(3)
        Unknown1096(1000)
        Unknown1099(10)
        Unknown3033()
        Unknown3003(100)
    sprite('vref_rwi_Afinish_ground00', 3)	# 1-3
    sprite('vref_rwi_Afinish_ground01', 3)	# 4-6
    sprite('vref_rwi_Afinish_ground02', 19)	# 7-25
    Unknown1099(0)

@State
def rwief_Afinish_Create():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4061(1)
        Unknown1096(1000)
        Unknown3038(1)
    sprite('vref_rwi_Afinish02', 3)	# 1-3
    Unknown4045('72776965663332305f636f6c6472696e67000000000000000000000000000000ffffffff')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000001000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000002000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000003000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000004000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000005000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000006000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000007000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000008000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000009000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000c000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000000000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000001000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000002000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000003000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000004000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000005000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000006000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000007000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000008000000')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000009000000')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000a000000')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000b000000')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000c000000')

@State
def rwief_Afinish_Break():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(2)
        Unknown4061(1)
        Unknown1096(1000)
        Unknown3038(1)
    sprite('vref_rwi_Afinish02', 3)	# 1-3

    def upon_STATE_END():
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000008000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000009000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000a000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000b000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000c000000')
    sprite('vref_rwi_Afinish02', 22)	# 4-25
    clearUponHandler(1)

    def upon_STATE_END():
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000000000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000001000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000002000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000003000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000004000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000005000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000006000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000007000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000008000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000009000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000a000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000b000000')
        Unknown4047(56, 56, 56)
        Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000c000000')

@State
def rwief_Afinish_IcedGround():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6963656467726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown3038(1)
        Unknown23015(15)
        Unknown3033()
        teleportRelativeY(0)
        teleportRelativeX(-20000)
        Unknown1096(3000)
        Unknown1088(2000)
        Unknown3001(200)
    sprite('null', 84)	# 1-84
    sprite('null', 60)	# 85-144
    Unknown3004(-4)

@State
def rwief320():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(75000)
        teleportRelativeY(10000)
        Unknown4061(1)

        def upon_32():
            Unknown4007(0)
    sprite('null', 4)	# 1-4
    sprite('null', 3)	# 5-7
    SFX_3('rwise_42')
    sprite('null', 1)	# 8-8
    GFX_0('rwief320_IceSpikeN', 0)
    GFX_0('rwief320_IceSpikeN_Bloom', 0)
    GFX_0('rwief320_IceSpikeF', 0)
    GFX_0('rwief320_IceSpikeF_Bloom', 0)
    GFX_0('rwief320_IcedGround', 0)
    sprite('null', 1)	# 9-9
    Unknown4045('72776965663332305f636f6c6472696e6700000000000000000000000000000000000000')
    sprite('null', 4)	# 10-13
    GFX_0('rwief320_Dust', 0)

    def upon_STATE_END():
        GFX_0('rwief320_Debris', 0)
        Unknown4007(0)
        clearUponHandler(1)
    sprite('null', 25)	# 14-38
    Unknown4007(0)
    sprite('null', 10)	# 39-48
    clearUponHandler(1)
    Unknown26('rwief320_IceSpikeN')
    Unknown26('rwief320_IceSpikeN_Bloom')
    Unknown26('rwief320_IceSpikeF')
    Unknown26('rwief320_IceSpikeF_Bloom')
    GFX_0('rwief320_Debris', 0)
    Unknown21012('72776965663332305f476c79706800000000000000000000000000000000000020000000')
    Unknown21012('72776965663332305f426c6f6f6d00000000000000000000000000000000000020000000')

@State
def rwief320_Glyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown1064(1100)
        Unknown1056(400)
        Unknown1072(-90000)
        teleportRelativeY(-15000)
        Unknown3001(0)
        Unknown3004(30)
        Unknown23015(15)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1067(220)
    Unknown1059(80)
    sprite('null', 2)	# 4-5
    Unknown1067(110)
    Unknown1059(40)
    sprite('null', 2)	# 6-7
    Unknown1067(55)
    Unknown1059(20)
    Unknown3004(0)
    sprite('null', 12)	# 8-19
    Unknown1067(0)
    Unknown1059(0)
    sprite('null', 120)	# 20-139
    label(0)
    sprite('null', 4)	# 140-143
    sprite('null', 10)	# 144-153
    Unknown3004(-30)
    Unknown1067(55)
    Unknown1059(20)

@State
def rwief320_Bloom():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(1)
        Unknown1096(5000)
        Unknown3001(0)
        sendToLabelUpon(32, 0)
    sprite('null', 4)	# 1-4
    Unknown4054(2)
    Unknown4047(50, 50, 50)
    Unknown23067('rwief320_bloom')
    Unknown3004(64)
    sprite('null', 120)	# 5-124
    Unknown3004(0)
    label(0)
    sprite('null', 20)	# 125-144
    Unknown3004(-16)

@State
def rwief320_IcedGround():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6963656467726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4022(2)
        Unknown3038(1)
        Unknown23015(15)
        teleportRelativeY(0)
        teleportRelativeX(-20000)
        Unknown1096(4200)
        Unknown1088(2500)
        Unknown3001(255)
    sprite('null', 84)	# 1-84
    sprite('null', 60)	# 85-144
    Unknown3004(-4)

@State
def rwief320_IceSpikeN():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown23015(9)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(2466)
    sprite('null', 1)	# 1-1
    Unknown4003('72776965663332305f6963657370696b6530314e2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(20)
    Unknown23122(4)
    sprite('null', 1)	# 2-2
    Unknown23122(16)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663332305f6963657370696b6530324e2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    sprite('null', 1)	# 4-4
    Unknown23122(32)
    sprite('null', 1)	# 5-5
    Unknown23122(16)
    sprite('null', 1)	# 6-6
    Unknown23122(8)
    sprite('null', 120)	# 7-126
    Unknown1099(0)
    Unknown23122(6)

@State
def rwief320_IceSpikeF():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown23015(15)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(2466)
    sprite('null', 1)	# 1-1
    Unknown1099(20)
    GFX_0('rwief320_Bloom', 0)
    Unknown23122(4)
    Unknown4003('72776965663332305f6963657370696b653031462e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown23122(16)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663332305f6963657370696b653032462e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    sprite('null', 1)	# 4-4
    Unknown23122(32)
    sprite('null', 1)	# 5-5
    Unknown23122(16)
    sprite('null', 1)	# 6-6
    Unknown23122(8)
    sprite('null', 120)	# 7-126
    Unknown1099(0)
    Unknown23122(6)

@State
def rwief320_IceSpikeN_Bloom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown23015(10)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(5000)
        Unknown3003(30)
    sprite('vref_rwi320_00n', 2)	# 1-2
    Unknown1099(5)
    sprite('vref_rwi320_01n', 4)	# 3-6
    sprite('vref_rwi320_01n', 120)	# 7-126
    Unknown1099(0)

@State
def rwief320_IceSpikeF_Bloom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown23015(14)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(5000)
        Unknown3003(30)
    sprite('vref_rwi320_00f', 2)	# 1-2
    Unknown1099(5)
    sprite('vref_rwi320_01f', 4)	# 3-6
    sprite('vref_rwi320_01f', 120)	# 7-126
    Unknown1099(0)

@Subroutine
def IceSpikeCold():
    Unknown4054(15)

@State
def rwief320_Cold():

    def upon_IMMEDIATE():
        Unknown4061(1)
        teleportRelativeX(5000)
        Unknown3038(1)
        Unknown4009(2)
    sprite('vref_rwi320_01f', 23)	# 1-23
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000000000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000001000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000002000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000003000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000004000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000005000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000006000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000007000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000008000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000009000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000a000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000b000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000c000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000d000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000e000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000f000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000010000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000011000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000012000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000013000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000014000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000015000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000016000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000017000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000018000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000019000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000001a000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000001b000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000001c000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000001d000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000001e000000')

@State
def rwief320_Debris():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown3038(1)
        Unknown4061(1)
        teleportRelativeX(5000)
        Unknown1007(20000)
    sprite('vref_rwi320_01f', 1)	# 1-1
    SFX_0('018_ice_break_1')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000001000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000002000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000003000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000004000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000005000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000006000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000007000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000008000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000009000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000e000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000f000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000010000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000011000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000013000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000014000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000015000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b42000000000000000000000000000016000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b42000000000000000000000000000017000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b42000000000000000000000000000018000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b42000000000000000000000000000019000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b4200000000000000000000000000001a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b4200000000000000000000000000001b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b4200000000000000000000000000001c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b4200000000000000000000000000001d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b4200000000000000000000000000001e000000')

@State
def rwief320_Dust():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown3038(1)
        Unknown4061(1)
        teleportRelativeX(5000)
        Unknown1007(0)
    sprite('vref_rwi320_01f', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000001000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000002000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000003000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000004000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000005000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000006000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000007000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000008000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000009000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000e000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000f000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000010000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000011000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000012000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000013000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000014000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000015000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430314200000000000000000000000016000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430314200000000000000000000000017000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430314200000000000000000000000018000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430314200000000000000000000000019000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031420000000000000000000000001a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031420000000000000000000000001b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031420000000000000000000000001c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031420000000000000000000000001d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031420000000000000000000000001e000000')

@State
def rwief405C():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown4010(3)
        teleportRelativeY(200000)
        teleportRelativeX(130000)
        Unknown4061(1)
        sendToLabelUpon(32, 0)
    sprite('null', 47)	# 1-47
    GFX_0('rwief405_Glyph01', 0)
    GFX_0('rwief405_Glyph02', 0)
    sprite('null', 1)	# 48-48
    Unknown14()
    label(0)
    sprite('null', 50)	# 49-98
    Unknown4007(0)
    Unknown4047(48, 64, 64)
    Unknown4045('72776965663430355f686974000000000000000000000000000000000000000000000000')
    GFX_0('rwief405_Glyph03', 0)
    Unknown21012('72776965663430355f476c79706830310000000000000000000000000000000020000000')
    Unknown21012('72776965663430355f476c79706830320000000000000000000000000000000020000000')

@State
def rwief405_Glyph01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f636f756e7465725f676c79706830312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('MagicImage_Func')
        Unknown4022(2)
        Unknown4010(3)
        Unknown23015(6)
        Unknown1056(1520)
        Unknown1064(1900)
        Unknown1088(304)
        Unknown3001(0)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1059(-160)
    Unknown1067(-200)
    Unknown1091(-32)
    Unknown3004(60)
    sprite('null', 31)	# 4-34
    Unknown3004(0)
    Unknown1099(0)
    Unknown1091(0)
    label(10)
    sprite('null', 4)	# 35-38
    Unknown1059(-40)
    Unknown1067(-50)
    Unknown1091(-8)
    Unknown3004(-30)
    sprite('null', 4)	# 39-42
    Unknown1059(-80)
    Unknown1067(-100)
    Unknown1091(-16)
    Unknown3004(-20)
    sprite('null', 1)	# 43-43
    Unknown14()
    label(0)
    sprite('null', 4)	# 44-47
    Unknown1059(80)
    Unknown1067(100)
    Unknown1091(16)
    Unknown3004(-45)
    sprite('null', 1)	# 48-48
    Unknown14()

@State
def rwief405_Glyph02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f636f756e7465725f676c79706830322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('MagicImage_Func')
        Unknown4022(2)
        Unknown4010(3)
        Unknown23015(6)
        Unknown23122(40)
        Unknown1056(1280)
        Unknown1064(1600)
        Unknown1088(256)
        Unknown3001(0)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1059(-160)
    Unknown1067(-200)
    Unknown1091(-32)
    Unknown3004(30)
    sprite('null', 31)	# 4-34
    Unknown3004(0)
    Unknown1099(0)
    Unknown1091(0)
    label(10)
    sprite('null', 8)	# 35-42
    Unknown1059(20)
    Unknown1067(25)
    Unknown1091(4)
    Unknown3004(-15)
    sprite('null', 1)	# 43-43
    Unknown14()
    label(0)
    sprite('null', 4)	# 44-47
    Unknown1059(80)
    Unknown1067(100)
    Unknown1091(16)
    Unknown3004(-25)
    sprite('null', 1)	# 48-48
    Unknown14()

@State
def rwief405_Glyph03():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f636f756e7465725f676c79706830332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('MagicImage_Func')
        Unknown23015(6)
        Unknown1056(960)
        Unknown1064(1200)
        Unknown1088(192)
        Unknown3001(255)
    sprite('null', 1)	# 1-1
    Unknown1059(40)
    Unknown1067(50)
    Unknown1091(8)
    physicsXImpulse(-2000)
    sprite('null', 1)	# 2-2
    Unknown21004(63)
    sprite('null', 1)	# 3-3
    Unknown21004(58)
    sprite('null', 1)	# 4-4
    Unknown21004(52)
    sprite('null', 1)	# 5-5
    Unknown21004(46)
    sprite('null', 1)	# 6-6
    Unknown21004(40)
    sprite('null', 1)	# 7-7
    Unknown21004(32)
    sprite('null', 1)	# 8-8
    Unknown21004(26)
    sprite('null', 1)	# 9-9
    Unknown21004(20)
    sprite('null', 1)	# 10-10
    Unknown21004(14)
    sprite('null', 1)	# 11-11
    Unknown21004(8)
    sprite('null', 1)	# 12-12
    Unknown21004(2)
    Unknown14()

@State
def ThrowMagic():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Unknown9021(1)
        Damage(1000)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackX(65000)
        AirPushbackY(15000)
        AirUntechableTime(40)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(60)
        Unknown30048(1)
        Unknown1086(22)
        teleportRelativeX(50000)
        Unknown1007(200000)
        Unknown23015(2)
        Unknown11044(1)
        Unknown3038(1)
    sprite('ThrowMagicAtk', 15)	# 1-15	 **attackbox here**
    StartMultihit()
    sprite('ThrowMagicAtk', 6)	# 16-21	 **attackbox here**
    RefreshMultihit()

@State
def rwief310_glyph():

    def upon_IMMEDIATE():
        teleportRelativeX(180000)
        Unknown1007(250000)
        Unknown4011(3)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(41, 10)
    sprite('null', 120)	# 1-120
    GFX_0('rwief310_glyph01', 0)
    GFX_0('rwief310_glyph02', 0)
    GFX_0('rwief310_glyph03', 0)
    label(1)
    sprite('null', 3)	# 121-123
    Unknown4022(22)
    label(0)
    sprite('null', 10)	# 124-133
    Unknown4022(22)
    sprite('null', 33)	# 134-166
    sprite('null', 6)	# 167-172
    Unknown4022(0)
    Unknown21012('72776965663331305f676c79706830310000000000000000000000000000000020000000')
    Unknown21012('72776965663331305f676c79706830320000000000000000000000000000000020000000')
    Unknown21012('72776965663331305f676c79706830330000000000000000000000000000000020000000')
    GFX_0('rwief310_glyphB01', 0)
    GFX_0('rwief310_glyphB02', 0)
    GFX_0('rwief310_glyphB03', 0)
    sprite('null', 1)	# 173-173
    GFX_0('rwief310_GlyphBurst', 0)
    Unknown26('rwief310_glyphB01')
    Unknown26('rwief310_glyphB02')
    Unknown26('rwief310_glyphB03')
    Unknown14()
    label(10)
    sprite('null', 16)	# 174-189
    Unknown21012('72776965663331305f676c79706830310000000000000000000000000000000029000000')
    Unknown21012('72776965663331305f676c79706830320000000000000000000000000000000029000000')
    Unknown21012('72776965663331305f676c79706830330000000000000000000000000000000029000000')

@State
def rwief310_GlyphBurst():

    def upon_IMMEDIATE():
        Unknown23023()
    sprite('null', 1)	# 1-1
    GFX_1('rwief310_throw', 0)

@State
def rwief310_glyph01():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4003('72776965663331305f676c7970683031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
        Unknown23015(6)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(41, 10)
        Unknown3001(0)
        Unknown1056(400)
        Unknown1064(400)
    sprite('null', 3)	# 1-3
    Unknown3004(50)
    Unknown1059(100)
    Unknown1067(100)
    sprite('null', 3)	# 4-6
    Unknown1059(20)
    Unknown1067(20)
    sprite('null', 5)	# 7-11
    Unknown1059(13)
    Unknown1067(13)
    sprite('null', 180)	# 12-191
    Unknown1059(0)
    Unknown1067(0)
    label(0)
    sprite('null', 4)	# 192-195
    Unknown3004(-85)
    sprite('null', 1)	# 196-196
    Unknown14()
    label(10)
    sprite('null', 7)	# 197-203
    sprite('null', 2)	# 204-205
    Unknown1059(-94)
    Unknown1067(-94)
    sprite('null', 7)	# 206-212
    Unknown3004(-40)

@State
def rwief310_glyph02():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4003('72776965663331305f676c7970683032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
        Unknown23015(12)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(41, 10)
        Unknown3001(0)
        Unknown1056(500)
        Unknown1064(-400)
    sprite('null', 2)	# 1-2
    sprite('null', 3)	# 3-5
    Unknown3004(50)
    physicsXImpulse(8000)
    Unknown1059(100)
    Unknown1067(-100)
    sprite('null', 3)	# 6-8
    Unknown3004(0)
    physicsXImpulse(4000)
    Unknown1059(33)
    Unknown1067(-33)
    sprite('null', 5)	# 9-13
    physicsXImpulse(666)
    Unknown1059(0)
    Unknown1067(0)
    sprite('null', 180)	# 14-193
    physicsXImpulse(0)
    label(0)
    sprite('null', 4)	# 194-197
    Unknown3004(-75)
    sprite('null', 1)	# 198-198
    Unknown14()
    label(10)
    sprite('null', 5)	# 199-203
    sprite('null', 2)	# 204-205
    physicsXImpulse(-4000)
    Unknown1059(-113)
    Unknown1067(101)
    sprite('null', 6)	# 206-211
    Unknown3004(-50)

@State
def rwief310_glyph03():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4003('72776965663331305f676c7970683032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
        Unknown23015(6)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(41, 10)
        Unknown3001(0)
        Unknown1056(300)
        Unknown1064(400)
    sprite('null', 2)	# 1-2
    sprite('null', 3)	# 3-5
    Unknown3004(50)
    physicsXImpulse(-10000)
    Unknown1059(100)
    Unknown1067(100)
    sprite('null', 3)	# 6-8
    physicsXImpulse(-5000)
    Unknown1059(33)
    Unknown1067(33)
    Unknown3004(0)
    sprite('null', 5)	# 9-13
    physicsXImpulse(-1000)
    Unknown1059(0)
    Unknown1067(0)
    sprite('null', 180)	# 14-193
    physicsXImpulse(0)
    label(0)
    sprite('null', 4)	# 194-197
    Unknown3004(-75)
    sprite('null', 1)	# 198-198
    Unknown14()
    label(10)
    sprite('null', 5)	# 199-203
    sprite('null', 2)	# 204-205
    physicsXImpulse(5000)
    Unknown1059(-88)
    Unknown1067(-101)
    sprite('null', 6)	# 206-211
    Unknown3004(-50)

@State
def rwief310_glyphB01():

    def upon_IMMEDIATE():
        callSubroutine('MagicImageB_Func')
        Unknown4003('72776965663331305f676c7970684230310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(7)
        Unknown3001(0)
        Unknown1056(800)
        Unknown1064(800)
    sprite('null', 6)	# 1-6
    Unknown3004(42)
    sprite('null', 3)	# 7-9
    Unknown3004(0)
    Unknown1059(200)
    Unknown1067(200)
    Unknown3004(-28)
    sprite('null', 3)	# 10-12
    Unknown1059(100)
    Unknown1067(100)
    sprite('null', 3)	# 13-15
    Unknown1059(50)
    Unknown1067(50)

@State
def rwief310_glyphB02():

    def upon_IMMEDIATE():
        callSubroutine('MagicImageB_Func')
        Unknown4003('72776965663331305f676c7970684230320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(11)
        Unknown3001(0)
        Unknown1056(900)
        Unknown1064(-800)
        teleportRelativeX(40000)
    sprite('null', 6)	# 1-6
    Unknown3004(25)
    sprite('null', 3)	# 7-9
    Unknown1059(160)
    Unknown1067(-160)
    Unknown3004(-16)
    sprite('null', 3)	# 10-12
    Unknown1059(80)
    Unknown1067(-80)
    sprite('null', 3)	# 13-15
    Unknown1059(30)
    Unknown1067(-30)

@State
def rwief310_glyphB03():

    def upon_IMMEDIATE():
        callSubroutine('MagicImageB_Func')
        Unknown4003('72776965663331305f676c7970684230320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(7)
        Unknown3001(0)
        Unknown1056(700)
        Unknown1064(800)
        teleportRelativeX(-50000)
    sprite('null', 6)	# 1-6
    Unknown3004(25)
    sprite('null', 3)	# 7-9
    Unknown1059(160)
    Unknown1067(160)
    Unknown3004(-16)
    sprite('null', 3)	# 10-12
    Unknown1059(80)
    Unknown1067(80)
    sprite('null', 3)	# 13-15
    Unknown1059(30)
    Unknown1067(30)

@State
def rwief311_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(210000)
    sprite('vref_rwi311_00', 6)	# 1-6
    GFX_0('rwief311_slash_Flare', 100)
    sprite('vref_rwi311_01', 3)	# 7-9
    sprite('null', 3)	# 10-12
    GFX_0('rwief311_slash_Model', 100)
    GFX_0('rwief311_slash_Bloom', 100)
    GFX_0('rwief311_EX_Dummy', 100)
    sprite('vref_rwi311_03', 3)	# 13-15
    sprite('vref_rwi311_04', 3)	# 16-18
    sprite('null', 9)	# 19-27

@State
def rwief311_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        Unknown4003('72776965663331315f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(28000)
        Unknown1007(-18000)
        Unknown1096(3700)
    sprite('null', 3)	# 1-3
    sprite('null', 5)	# 4-8
    physicsXImpulse(10000)
    Unknown1099(46)
    sprite('null', 7)	# 9-15
    physicsXImpulse(5000)
    Unknown1099(23)

@State
def rwief311_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(28000)
        Unknown1007(-18000)
    sprite('vref_rwi311_02b', 3)	# 1-3
    sprite('vref_rwi311_03b', 2)	# 4-5
    physicsXImpulse(10000)
    Unknown1099(12)
    sprite('vref_rwi311_03b', 3)	# 6-8
    Unknown3004(-36)
    sprite('vref_rwi311_03b', 7)	# 9-15
    physicsXImpulse(5000)
    Unknown1099(6)

@State
def rwief311_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(600)
    sprite('null', 6)	# 1-6
    Unknown1000(-420000)
    teleportRelativeY(195000)
    Unknown1099(40)
    sprite('null', 3)	# 7-9
    Unknown1000(-350000)
    teleportRelativeY(35000)
    sprite('null', 3)	# 10-12
    Unknown1096(0)
    Unknown1099(0)
    sprite('null', 3)	# 13-15
    Unknown1000(-435000)
    teleportRelativeY(332000)
    Unknown1096(1000)
    Unknown1099(-100)
    sprite('null', 3)	# 16-18
    Unknown1000(-490000)
    teleportRelativeY(200000)
    Unknown1099(-200)

@State
def rwief311_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown1096(1050)
        teleportRelativeX(110000)
        physicsXImpulse(-10000)
        Unknown1007(-13000)
    sprite('vref_rwi311_03b', 3)	# 1-3
    sprite('vref_rwi311_03b', 1)	# 4-4
    physicsXImpulse(10000)
    Unknown1099(12)
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000003000000')
    sprite('vref_rwi311_03b', 1)	# 5-5
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000007000000')
    sprite('vref_rwi311_03b', 1)	# 6-6
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3138000000000000000000000000000a000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3232000000000000000000000000000b000000')
    sprite('vref_rwi311_03b', 1)	# 7-7
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3234000000000000000000000000000c000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3232000000000000000000000000000d000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3138000000000000000000000000000e000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3236000000000000000000000000000f000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000010000000')

@State
def rwief313_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown2005()
        teleportRelativeX(210000)
    sprite('vref_rwi311_01', 3)	# 1-3
    GFX_0('rwief313_slash_Flare', 100)
    sprite('null', 3)	# 4-6
    GFX_0('rwief311_slash_Model', 100)
    GFX_0('rwief311_slash_Bloom', 100)
    GFX_0('rwief311_EX_Dummy', 100)
    sprite('vref_rwi311_03', 3)	# 7-9
    sprite('vref_rwi311_04', 3)	# 10-12
    Unknown3004(-32)
    sprite('null', 9)	# 13-21

@State
def rwief313_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(840)
    sprite('null', 3)	# 1-3
    Unknown1000(-300000)
    teleportRelativeY(10000)
    Unknown1099(40)
    sprite('null', 3)	# 4-6
    Unknown1096(0)
    Unknown1099(0)
    sprite('null', 3)	# 7-9
    Unknown1000(-435000)
    teleportRelativeY(332000)
    Unknown1096(1000)
    Unknown1099(-100)
    sprite('null', 3)	# 10-12
    Unknown1000(-498000)
    teleportRelativeY(168000)
    Unknown1099(-200)

@State
def rwief312_Glyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImageB_Func')
        Unknown23015(6)
        sendToLabelUpon(32, 10)
        teleportRelativeX(100000)
        Unknown1007(250000)
        Unknown26('rwief310_glyph')
    sprite('null', 7)	# 1-7
    Unknown4003('72776965665f676c797068425f73746172743230662e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    physicsXImpulse(50000)
    sprite('null', 5)	# 11-15
    physicsXImpulse(0)
    Unknown3004(-25)
    sprite('null', 5)	# 16-20

@State
def IceShieldA():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(2)
        Unknown2019(500)
        teleportRelativeX(600000)
        Unknown3038(1)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0000000000000000000000000000000000000000')
        SLOT_89 = 10
        Unknown2053(1)
        Unknown2017(1)
        Unknown2016(10)
        Unknown2015(200)
        Unknown2021(1)
        Unknown23020(150)
        Unknown23021(150)

        def upon_19():
            clearUponHandler(19)
            Unknown23022(1)
            sendToLabel(0)

        def upon_43():
            if (SLOT_48 == 4051):
                sendToLabel(0)

        def upon_44():
            sendToLabel(0)

        def upon_53():
            sendToLabel(0)
    sprite('vrrwi_test_def', 6)	# 1-6	 **attackbox here**
    GFX_0('rwief405A_IceWall', 0)
    Unknown3001(0)
    Unknown3004(42)
    Unknown1096(0)
    Unknown1099(133)
    sprite('vrrwi_test_def', 120)	# 7-126	 **attackbox here**
    Unknown1096(800)
    Unknown1099(0)
    label(0)
    sprite('vrrwi_test_def', 6)	# 127-132	 **attackbox here**
    clearUponHandler(53)
    clearUponHandler(44)
    clearUponHandler(19)
    Unknown3004(-42)

@State
def IceShieldB():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(2)
        Unknown2019(500)
        teleportRelativeX(500000)
        Unknown3038(1)
        Unknown2053(1)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0000000000000000000000000000000000000000')
        SLOT_89 = 68
        Unknown23020(1700)
        Unknown23021(1700)

        def upon_19():
            clearUponHandler(19)
            Unknown23022(1)
            sendToLabel(0)
        Unknown2053(1)
        Unknown2017(1)
        Unknown2016(250)
        Unknown2015(200)
        Unknown2021(1)

        def upon_43():
            if (SLOT_48 == 4051):
                sendToLabel(0)

        def upon_44():
            sendToLabel(0)

        def upon_53():
            sendToLabel(0)
    sprite('vrrwi_test_def', 6)	# 1-6	 **attackbox here**
    GFX_0('rwief405B_IceWall', 0)
    Unknown3001(0)
    Unknown3004(42)
    Unknown1096(0)
    Unknown1099(183)
    sprite('vrrwi_test_def', 120)	# 7-126	 **attackbox here**
    Unknown1096(1100)
    Unknown1099(0)
    label(0)
    sprite('vrrwi_test_def', 6)	# 127-132	 **attackbox here**
    clearUponHandler(53)
    clearUponHandler(44)
    clearUponHandler(19)

@State
def rwief405A_IceWall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2005()
        Unknown1096(2044)
        Unknown1088(1300)
        teleportRelativeX(280000)
        teleportRelativeY(0)
        Unknown4061(1)

        def upon_STATE_END():
            Unknown4007(0)
            Unknown1096(0)
            GFX_0('rwief405A_IceWall_Break', 0)
            GFX_0('rwief405A_IcedGround_End', 0)
        sendToLabelUpon(32, 0)
    sprite('null', 7)	# 1-7
    GFX_0('rwief405_IceWall_A', 0)
    GFX_0('rwief405_IceWall_A_Bloom', 0)
    GFX_0('rwief405_IceWall_B', 0)
    GFX_0('rwief405_IceWall_B_Bloom', 0)
    GFX_0('rwief405_IceWall_C', 0)
    GFX_0('rwief405_IceWall_C_Bloom', 0)
    GFX_0('rwief405A_IceWall_Cold', 0)
    GFX_0('rwief405A_IceWall_ColdRing', 0)
    GFX_0('rwief405A_IceWall_Ground', 0)
    GFX_0('rwief405A Icewall_Dust', 0)
    GFX_0('rwief405A_IcedGround', 0)
    Unknown1099(20)
    SFX_3('rwise_42')
    sprite('null', 500)	# 8-507
    Unknown1099(0)

@State
def rwief405A_IceWall_Break():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown3038(1)
        Unknown4061(1)
        teleportRelativeX(-5000)
        Unknown1007(60000)
        Unknown1098(73)
    sprite('vref_rwi405_particle', 1)	# 1-1
    SFX_0('018_ice_break_1')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000001000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000003000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000006000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000007000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000009000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000f000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000010000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000011000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000012000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000013000000')

@State
def rwief405A_IceWall_Cold():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        teleportRelativeX(5000)
        Unknown1098(73)
        Unknown3038(1)
        Unknown4009(2)
    sprite('vref_rwi405_particle', 5)	# 1-5
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000000000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000002000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000004000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000006000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000008000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000a000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000c000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000e000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000010000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000012000000')
    label(0)
    sprite('vref_rwi405_particle', 4)	# 6-9
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000000000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000008000000')
    sprite('vref_rwi405_particle', 4)	# 10-13
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000001000000')
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000009000000')
    sprite('vref_rwi405_particle', 4)	# 14-17
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000002000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000a000000')
    sprite('vref_rwi405_particle', 4)	# 18-21
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000003000000')
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000b000000')
    sprite('vref_rwi405_particle', 4)	# 22-25
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000004000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000c000000')
    sprite('vref_rwi405_particle', 4)	# 26-29
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000005000000')
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000d000000')
    sprite('vref_rwi405_particle', 4)	# 30-33
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000006000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000e000000')
    sprite('vref_rwi405_particle', 4)	# 34-37
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000007000000')
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000f000000')
    sprite('vref_rwi405_particle', 4)	# 38-41
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000010000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000011000000')
    sprite('vref_rwi405_particle', 4)	# 42-45
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000012000000')
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000013000000')
    gotoLabel(0)

@State
def rwief405A__sp__Icewall_Dust():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown3038(1)
        Unknown4061(1)
        teleportRelativeX(-20000)
        Unknown1007(20000)
        Unknown1098(73)
    sprite('vref_rwi405_particle', 2)	# 1-2
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000000000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000006000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000c000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000012000000')
    sprite('vref_rwi405_particle', 2)	# 3-4
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000004000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000a000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000010000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000013000000')
    sprite('vref_rwi405_particle', 2)	# 5-6
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000002000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000008000000')
    Unknown4054(11)
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000e000000')

@State
def rwief405A_IceWall_ColdRing():

    def upon_IMMEDIATE():
        Unknown4061(1)
        teleportRelativeX(-60000)
        Unknown1098(73)
        Unknown4009(2)
    sprite('null', 90)	# 1-90
    Unknown23067('rwief405_coldring')

@State
def rwief405A_IceWall_Ground():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        teleportRelativeX(-30000)
        Unknown1098(57)
        Unknown4009(2)
    sprite('null', 5)	# 1-5
    GFX_0('rwief405A_IceWall_GroundB', 0)
    Unknown4054(15)
    Unknown23067('rwief405_bloomC')
    sprite('null', 500)	# 6-505

@State
def rwief405A_IceWall_GroundB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4061(1)
    sprite('null', 5)	# 1-5
    Unknown4054(10)
    Unknown23067('rwief405_bloomB')
    sprite('null', 500)	# 6-505

@State
def rwief405A_IcedGround():

    def upon_IMMEDIATE():
        Unknown4003('72776965663430355f6963656467726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23015(15)
        Unknown3032()
        teleportRelativeY(0)
        teleportRelativeX(-80000)
        Unknown1096(2190)
        Unknown1088(1825)
        Unknown3001(160)
    sprite('null', 500)	# 1-500

@State
def rwief405A_IcedGround_End():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown23015(15)
        teleportRelativeY(0)
        teleportRelativeX(-80000)
        Unknown1096(2190)
        Unknown1088(1825)
        Unknown3001(160)
    sprite('null', 1)	# 1-1
    sprite('null', 59)	# 2-60
    Unknown4003('72776965663430355f6963656467726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 60)	# 61-120
    Unknown3004(-3)

@State
def rwief405B_IceWall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2005()
        Unknown1096(2800)
        Unknown1088(1300)
        teleportRelativeX(320000)
        teleportRelativeY(0)
        Unknown4061(1)

        def upon_STATE_END():
            Unknown4007(0)
            Unknown1096(0)
            Unknown3001(0)
            GFX_0('rwief405B_IceWall_Break', 0)
            GFX_0('rwief405B_IcedGround_End', 0)
        sendToLabelUpon(32, 0)
    sprite('null', 7)	# 1-7
    GFX_0('rwief405_IceWall_A', 0)
    GFX_0('rwief405_IceWall_A_Bloom', 0)
    GFX_0('rwief405_IceWall_B', 0)
    GFX_0('rwief405_IceWall_B_Bloom', 0)
    GFX_0('rwief405_IceWall_C', 0)
    GFX_0('rwief405_IceWall_C_Bloom', 0)
    GFX_0('rwief405B_IceWall_Cold', 0)
    GFX_0('rwief405B_IceWall_ColdRing', 0)
    GFX_0('rwief405B_IceWall_Ground', 0)
    GFX_0('rwief405B Icewall_Dust', 0)
    GFX_0('rwief405B_IcedGround', 0)
    Unknown1099(28)
    SFX_3('rwise_42')
    sprite('null', 500)	# 8-507
    Unknown1099(0)

@State
def rwief405_IceWall_A():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(9)
        Unknown3032()
        Unknown4061(1)
    sprite('null', 1)	# 1-1
    Unknown4003('72776965663430355f69636577616c6c4130312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(4)
    sprite('null', 1)	# 2-2
    Unknown23122(16)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663430355f69636577616c6c4130322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown4003('72776965663430355f69636577616c6c4130332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 6-6
    Unknown23122(32)
    sprite('null', 1)	# 7-7
    Unknown23122(16)
    sprite('null', 1)	# 8-8
    Unknown23122(8)
    sprite('null', 500)	# 9-508
    Unknown23122(6)

@State
def rwief405_IceWall_B():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(15)
        Unknown3032()
        Unknown4061(1)
        Unknown4015()
    sprite('null', 1)	# 1-1
    Unknown4003('72776965663430355f69636577616c6c4230312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(4)
    sprite('null', 1)	# 2-2
    Unknown23122(16)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663430355f69636577616c6c4230322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown4003('72776965663430355f69636577616c6c4230332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 6-6
    Unknown23122(32)
    sprite('null', 1)	# 7-7
    Unknown23122(16)
    sprite('null', 1)	# 8-8
    Unknown23122(8)
    sprite('null', 500)	# 9-508
    Unknown23122(6)

@State
def rwief405_IceWall_C():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(15)
        Unknown3032()
        Unknown4061(1)
    sprite('null', 2)	# 1-2
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663430355f69636577616c6c4330322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown4003('72776965663430355f69636577616c6c4330332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 6-6
    Unknown23122(32)
    sprite('null', 1)	# 7-7
    Unknown23122(16)
    sprite('null', 1)	# 8-8
    Unknown23122(8)
    sprite('null', 500)	# 9-508
    Unknown23122(6)

@State
def rwief405_IceWall_A_Bloom():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(10)
        Unknown3033()
        Unknown4061(1)
        Unknown21004(80)
        Unknown3003(30)
    sprite('null', 2)	# 1-2
    Unknown4003('72776965663430355f69636577616c6c4130315f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72776965663430355f69636577616c6c4130325f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 500)	# 5-504
    Unknown4003('72776965663430355f69636577616c6c4130335f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief405_IceWall_B_Bloom():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(9)
        Unknown3033()
        Unknown4061(1)
        Unknown21004(80)
        Unknown3003(30)
    sprite('null', 2)	# 1-2
    Unknown4003('72776965663430355f69636577616c6c4230315f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72776965663430355f69636577616c6c4230325f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 500)	# 5-504
    Unknown4003('72776965663430355f69636577616c6c4230335f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief405_IceWall_C_Bloom():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(15)
        Unknown3033()
        Unknown4061(1)
        Unknown21004(80)
        Unknown3003(30)
    sprite('null', 2)	# 1-2
    sprite('null', 2)	# 3-4
    Unknown4003('72776965663430355f69636577616c6c4330325f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 500)	# 5-504
    Unknown4003('72776965663430355f69636577616c6c4330335f426c6f6f6d2e4449470000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief405B_IceWall_Break():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown3038(1)
        Unknown4061(1)
        teleportRelativeX(-5000)
        Unknown1007(60000)
    sprite('vref_rwi405_particle', 1)	# 1-1
    SFX_0('018_ice_break_1')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000001000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000002000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000003000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000004000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000005000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000006000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000007000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000008000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000009000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000e000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b0000000000000000000000000000000f000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000010000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000011000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000012000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f696365627265616b00000000000000000000000000000013000000')

@State
def rwief405B_IceWall_Cold():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        teleportRelativeX(5000)
        Unknown3038(1)
        Unknown4009(2)
    sprite('vref_rwi405_particle', 5)	# 1-5
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000000000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000002000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000004000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000006000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000008000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000a000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000c000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c64000000000000000000000000000000000000000000000e000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000010000000')
    callSubroutine('IceSpikeCold')
    Unknown4045('72776965665f636f6c640000000000000000000000000000000000000000000012000000')
    label(0)
    sprite('vref_rwi405_particle', 3)	# 6-8
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000000000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000008000000')
    sprite('vref_rwi405_particle', 3)	# 9-11
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000001000000')
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000009000000')
    sprite('vref_rwi405_particle', 3)	# 12-14
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000002000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000a000000')
    sprite('vref_rwi405_particle', 3)	# 15-17
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000003000000')
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000b000000')
    sprite('vref_rwi405_particle', 3)	# 18-20
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000004000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000c000000')
    sprite('vref_rwi405_particle', 3)	# 21-23
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000005000000')
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000d000000')
    sprite('vref_rwi405_particle', 3)	# 24-26
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000006000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000e000000')
    sprite('vref_rwi405_particle', 3)	# 27-29
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000007000000')
    Unknown4045('72776965665f636f6c64420000000000000000000000000000000000000000000f000000')
    sprite('vref_rwi405_particle', 3)	# 30-32
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000010000000')
    Unknown4054(7)
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000011000000')
    sprite('vref_rwi405_particle', 3)	# 33-35
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000012000000')
    Unknown4045('72776965665f636f6c644200000000000000000000000000000000000000000013000000')
    gotoLabel(0)

@State
def rwief405B__sp__Icewall_Dust():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown3038(1)
        Unknown4061(1)
        teleportRelativeX(-20000)
    sprite('vref_rwi405_particle', 2)	# 1-2
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000000000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000003000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000006000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000009000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000c000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000f000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000012000000')
    sprite('vref_rwi405_particle', 2)	# 3-4
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000001000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000004000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000007000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000a000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000d000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000010000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000013000000')
    sprite('vref_rwi405_particle', 2)	# 5-6
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000002000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000005000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000008000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000b000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f647573743031000000000000000000000000000e000000')
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663332305f6963655f6475737430310000000000000000000000000011000000')

@State
def rwief405B_IceWall_ColdRing():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        teleportRelativeX(-80000)
        Unknown4009(2)
    sprite('null', 3)	# 1-3
    Unknown4045('72776965663430355f636f6c6472696e6700000000000000000000000000000000000000')

@State
def rwief405B_IceWall_Ground():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        teleportRelativeX(-80000)
        Unknown4009(2)
    sprite('null', 5)	# 1-5
    GFX_0('rwief405B_IceWall_GroundB', 0)
    Unknown4054(15)
    Unknown23067('rwief405_bloomA')
    sprite('null', 500)	# 6-505

@State
def rwief405B_IceWall_GroundB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4061(1)
    sprite('null', 5)	# 1-5
    Unknown4054(10)
    Unknown23067('rwief405_bloomB')
    sprite('null', 500)	# 6-505

@State
def rwief405B_IcedGround():

    def upon_IMMEDIATE():
        Unknown4003('72776965663430355f6963656467726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4022(2)
        Unknown4010(2)
        Unknown23015(15)
        teleportRelativeY(0)
        teleportRelativeX(-80000)
        Unknown1096(3000)
        Unknown1088(2500)
        Unknown3001(160)
    sprite('null', 500)	# 1-500
    Unknown3004(0)

@State
def rwief405B_IcedGround_End():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown23015(15)
        teleportRelativeY(0)
        teleportRelativeX(-80000)
        Unknown1096(3000)
        Unknown1088(2500)
        Unknown3001(160)
    sprite('null', 1)	# 1-1
    sprite('null', 59)	# 2-60
    Unknown4003('72776965663430355f6963656467726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 60)	# 61-120
    Unknown3004(-3)

@State
def InstallationMagic():

    def upon_IMMEDIATE():
        Unknown2053(1)
        Unknown23089('0100000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 4061):
                teleportRelativeX(600000)
                Unknown30070('496e7374616c6c6174696f6e4d61676963410000000000000000000000000000')
            if (SLOT_48 == 4062):
                teleportRelativeX(750000)
                Unknown1007(300000)
                Unknown30070('496e7374616c6c6174696f6e4d61676963420000000000000000000000000000')
            if (SLOT_48 == 4063):
                Unknown1086(22)
                teleportRelativeX(300000)
                teleportRelativeY(0)
                Unknown30070('496e7374616c6c6174696f6e4d61676963430000000000000000000000000000')
                Unknown2037(1)
            if (SLOT_48 == 4064):
                Unknown1086(22)
                teleportRelativeX(100000)
                teleportRelativeY(300000)
                Unknown30070('496e7374616c6c6174696f6e4d61676963440000000000000000000000000000')
                Unknown2037(1)
            if (SLOT_48 == 4065):
                teleportRelativeX(250000)
                Unknown1007(300000)
                Unknown30070('496e7374616c6c6174696f6e4d61676963417373697374000000000000000000')
                Unknown2037(2)
            if (SLOT_48 == 4066):
                sendToLabel(100)
            if (SLOT_48 == 4069):
                sendToLabel(1)
    sprite('null', 1)	# 1-1
    SFX_3('rwise_43')
    sprite('null', 6)	# 2-7
    GFX_0('MagicImage', -1)
    Unknown38(4, 1)
    label(0)
    sprite('null', 5)	# 8-12
    sprite('null', 10)	# 13-22
    GFX_0('MagicShot', -1)
    if (SLOT_2 == 1):
        Unknown23029(1, 4067, 0)
    if (SLOT_2 == 2):
        Unknown23029(1, 4068, 0)
    gotoLabel(1)
    label(100)
    sprite('null', 3)	# 23-25
    Unknown21007(4, 33)
    SFX_3('rwise_21')
    clearUponHandler(54)
    label(101)
    sprite('null', 3)	# 26-28
    gotoLabel(101)
    label(1)
    sprite('null', 6)	# 29-34
    Unknown21007(4, 32)

@State
def MagicImage():

    def upon_IMMEDIATE():
        Unknown1096(1000)
        Unknown1007(200000)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(100)
    sprite('null', 50)	# 1-50
    GFX_0('rwief406_Glyph', 0)
    label(0)
    sprite('null', 20)	# 51-70
    sprite('null', 10)	# 71-80
    Unknown21007(1, 32)
    ExitState()
    label(100)
    sprite('null', 10)	# 81-90
    Unknown21007(1, 32)
    sprite('null', 10)	# 91-100
    enterState('MagicImage_Black')

@State
def MagicImage_Black():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown1096(1000)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    GFX_0('rwief406_Glyph_Black', 0)
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown21007(1, 32)

@State
def rwief406_Glyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        sendToLabelUpon(32, 10)
    sprite('null', 25)	# 1-25
    Unknown4003('72776965665f676c7970685f73746172743235662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 26-32792
    Unknown4003('72776965665f676c7970685f6c6f6f70322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(10)
    sprite('null', 10)	# 32793-32802
    Unknown3004(-25)
    Unknown1099(-100)

@State
def rwief406_Glyph_Black():

    def upon_IMMEDIATE():
        callSubroutine('MagicImageB_Func')
        sendToLabelUpon(32, 10)
    sprite('null', 25)	# 1-25
    Unknown4003('72776965665f676c797068425f73746172743235662e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 26-32792
    Unknown4003('72776965665f676c797068425f6c6f6f70322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(10)
    sprite('null', 10)	# 32793-32802
    Unknown3004(-25)
    Unknown1099(-100)

@State
def MagicShot():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3001(0)
        AttackLevel_(3)
        Hitstop(8)
        Unknown9021(1)
        Unknown9266(9)
        Unknown12051(2)
        Unknown11056(3)
        AirUntechableTime(40)
        Unknown1086(2)
        Unknown1007(200000)
        Unknown23027()

        def upon_43():
            if (SLOT_48 == 4067):
                AttackLevel_(4)
                Hitstop(12)
                Unknown11091(10)
                Unknown30065(0)
            if (SLOT_48 == 4068):
                AttackP1(70)
                Unknown11042(1)

        def upon_11():
            if (SLOT_13 < (-20000)):
                AirPushbackY(-40000)
                Unknown9310(15)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            clearUponHandler(2)
            sendToLabel(0)
        Unknown23013(1)

        def upon_LANDING():
            clearUponHandler(17)
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(0)
    sprite('null', 7)	# 1-7
    sprite('null', 3)	# 8-10
    Unknown1111(25000, 22)
    Unknown1108(0)
    Unknown1019(1)
    YAccel(1)
    GFX_0('rwief400_Sword_shot', 100)
    sprite('vrrwi_test_atk', 3)	# 11-13	 **attackbox here**
    Unknown1019(5000)
    YAccel(5000)
    GFX_0('rwief400_Sword', 100)
    sprite('vrrwi_test_atk', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(400)
    YAccel(400)
    sprite('vrrwi_test_atk', 32767)	# 17-32783	 **attackbox here**
    Unknown1019(200)
    YAccel(200)
    label(0)
    sprite('vrrwi_test_atk', 6)	# 32784-32789	 **attackbox here**
    Unknown3004(-42)

@State
def rwief400_Sword():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4015()
        Unknown1096(1080)
        GFX_0('rwief400_Sword_pt', 100)
        Unknown4061(1)
        Unknown21004(48)

        def upon_STATE_END():
            Unknown4007(0)
    sprite('null', 3)	# 1-3
    Unknown4003('72776965663430305f53776f726453746172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 4-32770
    Unknown4003('72776965663430305f53776f72642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief400_Sword_shot():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(7000)
        Unknown4061(1)
    sprite('null', 1)	# 1-1
    Unknown4047(52, 52, 52)
    Unknown4045('7277695f34303053776f72645f73686f7400000000000000000000000000000064000000')

@State
def rwief400_Sword_pt():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4061(1)
    label(0)
    sprite('null', 2)	# 1-2
    Unknown4047(52, 52, 52)
    Unknown4045('7277695f34303053776f7264000000000000000000000000000000000000000064000000')
    gotoLabel(0)

@State
def rwief400_dash():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown1072(-20000)
    sprite('null', 1)	# 1-1
    GFX_1('rwi_400dash', -1)
    GFX_0('rwief400_dashring03', 0)
    sprite('null', 1)	# 2-2
    GFX_0('rwief400_dashring01', 0)
    sprite('null', 1)	# 3-3
    GFX_0('rwief400_dashring02', 0)
    sprite('null', 3)	# 4-6
    GFX_1('rwi_400dash', -1)
    sprite('null', 3)	# 7-9
    GFX_1('rwi_400dash', -1)
    sprite('null', 3)	# 10-12
    GFX_1('rwi_400dash', -1)
    sprite('null', 3)	# 13-15
    GFX_1('rwi_400dash', -1)
    sprite('null', 3)	# 16-18
    GFX_1('rwi_400dash', -1)

@State
def rwief400_dashring01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(20000)
        teleportRelativeY(170000)
        physicsXImpulse(-5000)
        Unknown1096(2200)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(900)
    Unknown3004(-12)
    sprite('null', 13)	# 4-16
    Unknown1099(450)

@State
def rwief400_dashring02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(100000)
        teleportRelativeY(170000)
        physicsXImpulse(-5000)
        Unknown1096(2000)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(700)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(350)

@State
def rwief400_dashring03():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(0)
        teleportRelativeY(170000)
        physicsXImpulse(-5000)
        Unknown1096(1400)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(600)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(300)

@State
def rwief407_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    GFX_0('rwief407_slash_Flare', 0)
    sprite('vref_rwi407_00', 3)	# 4-6
    sprite('null', 6)	# 7-12
    GFX_0('rwief407_slash_Model', 0)
    GFX_0('rwief407_slash_Bloom', 0)
    GFX_0('rwief407_EX_Dummy', 0)
    sprite('null', 3)	# 13-15
    Unknown4007(0)

@State
def rwief407_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23122(64)
        Unknown4003('72776965663430375f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(20000)
        Unknown1007(315000)
        Unknown1096(3071)
    sprite('null', 5)	# 1-5
    Unknown1099(61)
    physicsXImpulse(3000)
    sprite('null', 5)	# 6-10
    Unknown1099(30)

@State
def rwief407_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(20000)
        Unknown1007(315000)
        Unknown1096(830)
    sprite('vref_rwi407_01b', 2)	# 1-2
    Unknown1099(16)
    physicsXImpulse(3000)
    Unknown3001(200)
    sprite('vref_rwi407_01b', 3)	# 3-5
    Unknown3004(-28)
    sprite('vref_rwi407_01b', 4)	# 6-9
    Unknown1099(8)

@State
def rwief407_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4007(3)
        Unknown3038(1)

        def upon_32():
            Unknown4007(0)
        teleportRelativeX(20000)
        Unknown1007(315000)
        Unknown1096(830)
    sprite('null', 1)	# 1-1
    Unknown1099(16)
    physicsXImpulse(3000)
    sprite('vref_rwi407_01b', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000003000000')
    sprite('vref_rwi407_01b', 1)	# 3-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31340000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000007000000')
    sprite('vref_rwi407_01b', 1)	# 4-4
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3236000000000000000000000000000a000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3234000000000000000000000000000b000000')
    sprite('vref_rwi407_01b', 1)	# 5-5
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3232000000000000000000000000000c000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3236000000000000000000000000000d000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3138000000000000000000000000000e000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3234000000000000000000000000000f000000')

@State
def rwief407_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1096(0)
    sprite('null', 3)	# 4-6
    Unknown1000(120000)
    teleportRelativeY(345000)
    Unknown1096(400)
    Unknown1099(150)

@State
def rwief408_Glyph():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown2053(1)
        Unknown1007(515000)
        teleportRelativeX(-450000)
        Unknown1073(30000)
        callSubroutine('MagicImage_Func')

        def upon_41():
            GFX_0('rwief408_Speed', 0)

        def upon_43():
            if (SLOT_48 == 4071):
                Unknown4007(0)
                Unknown1086(2)
                teleportRelativeX(-75000)
                Unknown1007(250000)
                Unknown4007(3)
            if (SLOT_48 == 4072):
                Unknown4007(0)
    sprite('null', 25)	# 1-25
    Unknown4003('72776965665f676c7970685f73746172743235662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(1000)
    sprite('null', 30)	# 26-55
    Unknown4003('72776965665f676c7970685f6c6f6f70322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)	# 56-63
    Unknown1099(-125)
    sprite('null', 0)	# 64-63
    Unknown13(25)

@State
def rwief408_Speed():

    def upon_IMMEDIATE():
        Unknown1007(-30000)
        teleportRelativeX(60000)
        Unknown1072(30000)
        Unknown4061(1)
    sprite('null', 2)	# 1-2
    Unknown4048(30000)
    Unknown4045('7277695f3430336461736800000000000000000000000000000000000000000064000000')
    Unknown4047(48, 32, 16)
    Unknown4048(30000)
    Unknown4045('7277695f3430336461736842000000000000000000000000000000000000000064000000')
    GFX_0('rwief408_dashring01', 0)
    sprite('null', 1)	# 3-3
    GFX_0('rwief408_dashring02', 0)

@State
def rwief408_dashring01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(1200, 1500)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(900)
    Unknown3004(-12)
    sprite('null', 12)	# 5-16
    Unknown1099(500)

@State
def rwief408_dashring02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(100000)
        Unknown1007(-57700)
        Unknown1102(600, 800)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(700)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(400)

@State
def rwief408_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    GFX_0('rwief408_slash_Flare', 0)
    sprite('vref_rwi408_00', 3)	# 4-6
    Unknown1000(-9000)
    teleportRelativeY(30000)
    GFX_0('rwief408_slash_Speed', 100)
    sprite('vref_rwi408_01', 3)	# 7-9
    GFX_0('rwief_slash_dustA_loop', 9)
    GFX_0('rwief_slash_dustA_loop', 6)
    GFX_0('rwief_slash_dustA_loop', 3)
    GFX_0('rwief_slash_dustA_loop', 0)
    Unknown1000(0)
    teleportRelativeY(0)
    sprite('vref_rwi408_02', 32767)	# 10-32776
    label(0)
    sprite('vref_rwi408_03', 3)	# 32777-32779
    GFX_0('rwief408_EX_Dummy', 0)
    Unknown4007(0)
    Unknown26('rwief_slash_dustA_loop')
    Unknown1099(-20)
    physicsXImpulse(7000)
    sprite('vref_rwi408_04', 3)	# 32780-32782

@State
def rwief408_slash_Speed():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663430315f73706565642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        Unknown1072(120000)
        Unknown1096(3700)
        Unknown1056(2500)
        teleportRelativeX(100000)
        Unknown1007(150000)
    sprite('null', 3)	# 1-3
    Unknown3001(0)
    sprite('null', 3)	# 4-6
    physicsXImpulse(-10000)
    physicsYImpulse(5750)
    Unknown1059(50)
    Unknown1067(300)
    Unknown3001(255)
    sprite('null', 7)	# 7-13
    Unknown3004(-31)

@State
def rwief408_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4007(3)
        Unknown3038(1)

        def upon_32():
            Unknown4007(0)
    sprite('null', 1)	# 1-1
    sprite('vref_rwi408_01', 20)	# 2-21
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31340000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000007000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3236000000000000000000000000000a000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3234000000000000000000000000000b000000')

@State
def rwief408_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1096(0)
    sprite('null', 3)	# 4-6
    Unknown1000(200000)
    teleportRelativeY(100000)
    Unknown1096(400)
    Unknown1099(150)

@State
def rwief409_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')

        def upon_STATE_END():
            Unknown21012('72776965663430395f45585f44756d6d7900000000000000000000000000000020000000')
    sprite('vref_rwi409_00', 3)	# 1-3
    GFX_0('rwief409_slash_Model01', 0)
    GFX_0('rwief409_slash_Bloom', 0)
    GFX_0('rwief409_EX_Dummy', 0)
    sprite('null', 7)	# 4-10
    sprite('vref_rwi409_02', 2)	# 11-12
    GFX_0('rwief409_slash_Model02', 0)
    sprite('null', 12)	# 13-24

@State
def rwief409_slash_Model01():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        Unknown23122(64)
        Unknown4003('72776965663430395f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1000(11000)
        teleportRelativeY(275000)
    sprite('null', 3)	# 1-3
    Unknown1096(0)
    sprite('null', 5)	# 4-8
    Unknown4003('72776965663430395f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(3515)
    Unknown1099(52)
    sprite('null', 4)	# 9-12
    Unknown1099(26)

@State
def rwief409_slash_Model02():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        Unknown23122(64)
        Unknown4003('72776965663430395f736c61736830322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1000(20000)
        teleportRelativeY(340000)
    sprite('null', 2)	# 1-2
    Unknown1096(0)
    sprite('null', 5)	# 3-7
    Unknown4003('72776965663430395f736c61736830322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(3441)
    Unknown1099(74)
    sprite('null', 7)	# 8-14
    Unknown1099(37)

@State
def rwief409_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
    sprite('null', 3)	# 1-3
    sprite('vref_rwi409_01b', 2)	# 4-5
    Unknown1000(11000)
    teleportRelativeY(275000)
    Unknown1096(950)
    Unknown1099(14)
    sprite('vref_rwi409_01b', 3)	# 6-8
    Unknown3004(-36)
    sprite('vref_rwi409_01b', 4)	# 9-12
    Unknown1099(7)
    sprite('vref_rwi409_03b', 2)	# 13-14
    Unknown1000(20000)
    teleportRelativeY(340000)
    Unknown1096(930)
    Unknown1099(20)
    Unknown3001(255)
    Unknown3004(0)
    sprite('vref_rwi409_03b', 3)	# 15-17
    Unknown3004(-31)
    sprite('vref_rwi409_03b', 4)	# 18-21
    Unknown1099(10)

@State
def rwief409_EX_Dummy():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown3038(1)

        def upon_32():
            Unknown4007(0)
    sprite('null', 3)	# 1-3
    sprite('vref_rwi409_01b', 1)	# 4-4
    Unknown1000(11000)
    teleportRelativeY(275000)
    Unknown1096(950)
    Unknown1099(7)
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_20', 1)
    GFX_0('rwief_slash_dust_16', 2)
    GFX_0('rwief_slash_dust_18', 3)
    GFX_0('rwief_slash_dust_22', 4)
    GFX_0('rwief_slash_dust_16', 5)
    GFX_0('rwief_slash_dust_18', 6)
    GFX_0('rwief_slash_dust_22', 8)
    GFX_0('rwief_slash_dust_24', 7)
    GFX_0('rwief_slash_dust_26', 9)
    GFX_0('rwief_slash_dust_20', 10)
    GFX_0('rwief_slash_dust_22', 11)
    GFX_0('rwief_slash_dust_26', 12)
    sprite('vref_rwi409_01b', 8)	# 5-12
    sprite('vref_rwi409_03b', 1)	# 13-13
    Unknown1000(0)
    teleportRelativeY(325000)
    Unknown1096(930)
    Unknown1099(20)
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_20', 1)
    GFX_0('rwief_slash_dust_16', 2)
    GFX_0('rwief_slash_dust_18', 3)
    sprite('vref_rwi409_03b', 1)	# 14-14
    GFX_0('rwief_slash_dust_22', 4)
    GFX_0('rwief_slash_dust_16', 5)
    GFX_0('rwief_slash_dust_18', 6)
    GFX_0('rwief_slash_dust_22', 8)
    sprite('vref_rwi409_03b', 1)	# 15-15
    GFX_0('rwief_slash_dust_24', 7)
    GFX_0('rwief_slash_dust_26', 9)
    GFX_0('rwief_slash_dust_20', 10)
    GFX_0('rwief_slash_dust_26', 11)
    sprite('vref_rwi409_03b', 1)	# 16-16
    GFX_0('rwief_slash_dust_18', 12)
    GFX_0('rwief_slash_dust_22', 13)
    GFX_0('rwief_slash_dust_24', 14)
    GFX_0('rwief_slash_dust_26', 15)
    sprite('vref_rwi409_03b', 9)	# 17-25
    GFX_0('rwief_slash_dust_20', 16)
    GFX_0('rwief_slash_dust_26', 17)

@State
def rwief400_GlyphMaster():

    def upon_IMMEDIATE():
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(20)
            if (SLOT_48 == 4003):
                sendToLabel(30)
            if (SLOT_48 == 4004):
                clearUponHandler(43)
                sendToLabel(40)
    sprite('null', 32767)	# 1-32767
    GFX_0('rwief400_Glyph_Root', 100)
    label(10)
    sprite('null', 32767)	# 32768-65534
    GFX_0('rwief400_dash', 100)
    Unknown21012('72776965663430305f476c7970685f706c75733031000000000000000000000020000000')
    label(20)
    sprite('null', 32767)	# 65535-98301
    Unknown21012('72776965663430305f476c7970685f706c75733032000000000000000000000020000000')
    label(30)
    sprite('null', 32767)	# 98302-131068
    Unknown26('rwief400_dash')
    Unknown26('rwief400_Glyph_Root')
    label(40)
    sprite('null', 1)	# 131069-131069
    Unknown21012('72776965663430305f476c79706800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430305f476c7970685f706c75733031000000000000000000000021000000')
    Unknown21012('72776965663430305f476c7970685f706c75733032000000000000000000000021000000')
    Unknown26('rwief400_Glyph_Root')

@State
def rwief400_Glyph_Root():

    def upon_IMMEDIATE():
        Unknown4011(2)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 4)	# 1-4
    GFX_0('rwief400_Glyph', 100)
    GFX_0('rwief400_Glyph_plus01', 100)
    GFX_0('rwief400_Glyph_plus02', 100)
    sprite('null', 32767)	# 5-32771
    SFX_3('rwise_43')

@State
def rwief400_Glyph():

    def upon_IMMEDIATE():
        Unknown4011(2)
        callSubroutine('MagicImage_Func')
        Unknown1064(1100)
        Unknown1056(500)
        Unknown1072(-90000)
        teleportRelativeY(-10000)
        Unknown3001(160)
        Unknown23015(15)
        GFX_0('rwief400_Glyph_light', 100)
        GFX_1('rwi_400GlyphLight_pt', 100)
        teleportRelativeX(-25000)
        sendToLabelUpon(32, 0)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743230662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 21-32787
    Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 4)	# 32788-32791
    sprite('null', 6)	# 32792-32797
    Unknown1067(-183)
    Unknown1059(-83)

@State
def rwief400_Glyph_plus01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4011(2)
        callSubroutine('MagicImage_Func')
        Unknown1064(1100)
        Unknown1056(500)
        Unknown1072(-90000)
        teleportRelativeY(-10000)
        teleportRelativeX(390000)
        Unknown3001(0)
        Unknown23015(15)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 9)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 20)	# 32768-32787
    Unknown3001(160)
    GFX_0('rwief400_Glyph_light', 100)
    Unknown4047(60, 60, 60)
    Unknown4045('7277695f343030476c7970684c696768745f707400000000000000000000000064000000')
    Unknown4003('72776965665f676c7970685f73746172743230662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 32788-65554
    Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(9)
    sprite('null', 7)	# 65555-65561
    sprite('null', 6)	# 65562-65567
    Unknown1067(-183)
    Unknown1059(-83)

@State
def rwief400_Glyph_plus02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4011(2)
        callSubroutine('MagicImage_Func')
        Unknown1064(1100)
        Unknown1056(500)
        Unknown1072(-90000)
        teleportRelativeY(-10000)
        teleportRelativeX(800000)
        Unknown3001(0)
        Unknown23015(15)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 9)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 20)	# 32768-32787
    Unknown3001(160)
    GFX_0('rwief400_Glyph_light', 100)
    Unknown4047(60, 60, 60)
    Unknown4045('7277695f343030476c7970684c696768745f707400000000000000000000000064000000')
    Unknown4003('72776965665f676c7970685f73746172743230662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 32788-65554
    Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(9)
    sprite('null', 10)	# 65555-65564
    sprite('null', 6)	# 65565-65570
    Unknown1067(-183)
    Unknown1059(-83)

@State
def rwief400_Glyph_light():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4061(1)
    sprite('null', 32767)	# 1-32767
    Unknown4047(60, 60, 60)
    Unknown23067('rwi_400GlyphLight')

@State
def rwief400_Slash_Hit():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('72776965663430305f736c61736800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430305f736c6173685f466c61726500000000000000000000000020000000')
    Unknown21012('72776965663430305f736c6173685f4d6f64656c00000000000000000000000020000000')
    Unknown21012('72776965663430305f736c6173685f426c6f6f6d00000000000000000000000020000000')
    Unknown21012('72776965663430305f45585f44756d6d7900000000000000000000000000000021000000')

@State
def rwief400_Slash_Cancel():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief400_slash')
    Unknown26('rwief400_slash_Flare')
    Unknown26('rwief400_slash_Model')
    Unknown26('rwief400_slash_Bloom')
    Unknown21012('72776965663430305f45585f44756d6d7900000000000000000000000000000020000000')

@State
def rwief400_Slash_End():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief400_slash')
    Unknown21012('72776965663430305f45585f44756d6d7900000000000000000000000000000020000000')

@State
def rwief400_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        sendToLabelUpon(32, 0)
        Unknown2055(120)

        def upon_STATE_END():
            teleportRelativeY(-2000000)
    sprite('vref_rwi400_00', 2)	# 1-2
    GFX_0('rwief400_slash_Flare', 0)
    GFX_0('rwief400_slash_Model', 100)
    GFX_0('rwief400_slash_Bloom', 100)
    GFX_0('rwief400_EX_Dummy', 0)
    sprite('vref_rwi400_01', 1)	# 3-3
    sprite('vref_rwi400_02', 2)	# 4-5
    sprite('vref_rwi400_03', 3)	# 6-8
    sprite('vref_rwi400_04', 1)	# 9-9
    sprite('vref_rwi400_04', 1)	# 10-10
    GFX_0('rwief_slash_dustA_loop', 0)
    GFX_0('rwief_slash_dustA_loop', 0)
    sprite('vref_rwi400_05', 32767)	# 11-32777
    label(0)
    sprite('null', 3)	# 32778-32780
    Unknown3038(1)
    Unknown26('rwief_slash_dustA_loop')
    sprite('null', 20)	# 32781-32800

@State
def rwief400_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663430305f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        teleportRelativeX(-25000)
        Unknown1007(171000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    Unknown1096(0)
    label(0)
    sprite('null', 3)	# 32768-32770
    Unknown4003('72776965663430305f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(3700)
    physicsXImpulse(2000)
    Unknown1099(74)
    sprite('null', 7)	# 32771-32777
    Unknown1099(37)
    sprite('null', 2)	# 32778-32779
    Unknown1099(0)

@State
def rwief400_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        teleportRelativeX(-25000)
        Unknown1007(171000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('vref_rwi400_06b', 2)	# 32768-32769
    physicsXImpulse(2000)
    Unknown1099(20)
    sprite('keep', 1)	# 32770-32770
    Unknown3004(-42)
    sprite('keep', 6)	# 32771-32776
    Unknown1099(10)

@State
def rwief400_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4007(3)
        teleportRelativeX(-15000)
        Unknown1007(171000)
        physicsXImpulse(2000)
        Unknown3038(1)

        def upon_32():
            Unknown4007(0)
        sendToLabelUpon(33, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 1)	# 32768-32768
    sprite('vref_rwi400_06b', 20)	# 32769-32788
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_16', 1)
    GFX_0('rwief_slash_dust_18', 2)
    GFX_0('rwief_slash_dust_16', 3)
    GFX_0('rwief_slash_dust_18', 4)
    GFX_0('rwief_slash_dust_22', 5)
    GFX_0('rwief_slash_dust_18', 6)
    GFX_0('rwief_slash_dust_22', 7)
    GFX_0('rwief_slash_dust_24', 8)
    GFX_0('rwief_slash_dust_22', 9)
    GFX_0('rwief_slash_dust_26', 10)

@State
def rwief400_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 2)	# 1-2
    Unknown1000(-42000)
    teleportRelativeY(92000)
    sprite('null', 3)	# 3-5
    Unknown1000(161000)
    teleportRelativeY(267000)
    sprite('null', 3)	# 6-8
    Unknown1099(-100)
    Unknown1000(144000)
    teleportRelativeY(227000)
    sprite('null', 32767)	# 9-32775
    Unknown1056(1400)
    Unknown1099(0)
    Unknown1000(264000)
    teleportRelativeY(119000)
    label(0)
    sprite('null', 3)	# 32776-32778
    Unknown1056(1800)
    Unknown1064(1400)
    Unknown1099(-300)
    Unknown1000(-275000)
    teleportRelativeY(236000)

@State
def rwief400_Hit():

    def upon_IMMEDIATE():
        Unknown1056(1200)
        Unknown1064(700)
        Unknown1007(-20000)
        Unknown3001(128)
        Unknown4061(1)
    sprite('null', 20)	# 1-20
    Unknown4054(15)
    Unknown4047(48, 32, 16)
    Unknown23067('rwief400_hit')

@State
def rwief401_GlyphMaster():

    def upon_IMMEDIATE():
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(20)
            if (SLOT_48 == 4003):
                sendToLabel(30)
            if (SLOT_48 == 4004):
                clearUponHandler(43)
                sendToLabel(40)
    sprite('null', 32767)	# 1-32767
    GFX_0('rwief400_Glyph_Root', 100)
    label(10)
    sprite('null', 32767)	# 32768-65534
    GFX_0('rwief400_dash', 100)
    Unknown21012('72776965663430305f476c7970685f706c75733031000000000000000000000020000000')
    label(20)
    sprite('null', 32767)	# 65535-98301
    Unknown21012('72776965663430305f476c7970685f706c75733032000000000000000000000020000000')
    label(30)
    sprite('null', 32767)	# 98302-131068
    Unknown26('rwief400_dash')
    Unknown26('rwief400_Glyph_Root')
    label(40)
    sprite('null', 3)	# 131069-131071
    Unknown21012('72776965663430305f476c79706800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430305f476c7970685f706c75733031000000000000000000000021000000')
    Unknown21012('72776965663430305f476c7970685f706c75733032000000000000000000000021000000')
    Unknown26('rwief400_Glyph_Root')
    Unknown26('rwief401_slash')
    Unknown21012('72776965663430315f45585f44756d6d7900000000000000000000000000000020000000')
    Unknown26('rwief_slash_dustA_loop')
    sprite('null', 20)	# 131072-131091

@State
def rwief401_GlyphB():

    def upon_IMMEDIATE():
        Unknown4022(3)
        callSubroutine('MagicImage_Func')
        Unknown1064(1100)
        Unknown1056(500)
        Unknown1072(-90000)
        teleportRelativeY(-10000)
        Unknown1000(0)
        sendToLabelUpon(32, 0)
    sprite('null', 12)	# 1-12
    Unknown4003('72776965665f676c7970685f73746172743230662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)	# 13-20
    Unknown4022(0)
    sprite('null', 32767)	# 21-32787
    Unknown4022(0)
    Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 4)	# 32788-32791
    sprite('null', 6)	# 32792-32797
    Unknown1067(-183)
    Unknown1059(-83)

@State
def rwief401_Slash_Hit():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('72776965663430315f736c61736800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430315f736c6173685f466c61726500000000000000000000000020000000')

@State
def rwief401_Slash_PreHit():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('72776965663430305f736c61736800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430305f736c6173685f4d6f64656c00000000000000000000000020000000')
    Unknown21012('72776965663430305f736c6173685f426c6f6f6d00000000000000000000000020000000')
    Unknown21012('72776965663430305f45585f44756d6d7900000000000000000000000000000021000000')

@State
def rwief401_Slash_Cancel():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief400_slash')
    Unknown26('rwief401_slash')
    Unknown26('rwief400_slash_Model')
    Unknown26('rwief400_slash_Bloom')
    Unknown21012('72776965663430315f45585f44756d6d7900000000000000000000000000000020000000')

@State
def rwief401_Slash_End():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief401_slash')
    Unknown21012('72776965663430315f45585f44756d6d7900000000000000000000000000000020000000')

@State
def rwief401_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        sendToLabelUpon(32, 0)
        Unknown2055(120)
    sprite('vref_rwi400_00', 2)	# 1-2
    GFX_0('rwief400_slash_Model', 100)
    GFX_0('rwief400_slash_Bloom', 100)
    GFX_0('rwief400_EX_Dummy', 0)
    GFX_0('rwief401_slash_Flare', 0)
    sprite('vref_rwi400_01', 4)	# 3-6
    sprite('vref_rwi400_02', 3)	# 7-9
    sprite('vref_rwi400_03', 2)	# 10-11
    sprite('vref_rwi400_03A', 2)	# 12-13
    sprite('vref_rwi400_03B', 2)	# 14-15
    sprite('null', 1)	# 16-16
    sprite('vref_rwi400_04', 2)	# 17-18
    sprite('vref_rwi400_04', 2)	# 19-20
    GFX_0('rwief_slash_dustA_loop', 0)
    GFX_0('rwief_slash_dustA_loop', 0)
    sprite('vref_rwi400_05', 32767)	# 21-32787
    label(0)
    sprite('null', 6)	# 32788-32793
    Unknown26('rwief_slash_dustA_loop')
    sprite('vref_rwi401_00', 6)	# 32794-32799
    GFX_0('rwief401_slash_Speed', 100)
    sprite('vref_rwi401_01', 5)	# 32800-32804
    sprite('vref_rwi401_02', 3)	# 32805-32807
    GFX_0('rwief401_EX_Dummy', 100)
    sprite('vref_rwi401_03', 3)	# 32808-32810
    sprite('null', 20)	# 32811-32830

@State
def rwief401_slash_Speed():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663430315f73706565642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        Unknown1096(3700)
        Unknown1056(-4200)
        Unknown1059(170)
        Unknown1067(100)
        Unknown1072(24000)
        teleportRelativeX(40000)
        Unknown1007(300000)
    sprite('null', 6)	# 1-6
    Unknown3001(0)
    sprite('null', 7)	# 7-13
    Unknown4003('72776965663430315f73706565642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3001(255)
    sprite('null', 4)	# 14-17
    Unknown3004(-51)

@State
def rwief401_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)

        def upon_32():
            Unknown4007(0)
            Unknown13(25)
    sprite('vref_rwi401_01', 20)	# 1-20
    GFX_0('rwief_slash_dust_16', 12)
    GFX_0('rwief_slash_dust_16', 11)
    GFX_0('rwief_slash_dust_18', 10)
    GFX_0('rwief_slash_dust_18', 9)
    GFX_0('rwief_slash_dust_20', 8)
    GFX_0('rwief_slash_dust_18', 7)
    GFX_0('rwief_slash_dust_20', 6)
    GFX_0('rwief_slash_dust_22', 5)
    GFX_0('rwief_slash_dust_20', 4)
    GFX_0('rwief_slash_dust_22', 3)
    GFX_0('rwief_slash_dust_24', 2)
    GFX_0('rwief_slash_dust_22', 1)
    GFX_0('rwief_slash_dust_26', 0)

@State
def rwief401_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 2)	# 1-2
    Unknown1000(-42000)
    teleportRelativeY(92000)
    sprite('null', 7)	# 3-9
    Unknown1000(161000)
    teleportRelativeY(267000)
    sprite('null', 6)	# 10-15
    Unknown1099(-120)
    Unknown1000(150000)
    teleportRelativeY(220000)
    sprite('null', 0)	# 16-15
    Unknown1099(0)
    Unknown1096(0)
    sprite('null', 32767)	# 16-32782
    Unknown1056(1400)
    Unknown1099(0)
    Unknown1000(264000)
    teleportRelativeY(119000)
    label(0)
    sprite('null', 6)	# 32783-32788
    Unknown1096(0)
    Unknown1099(0)
    sprite('null', 6)	# 32789-32794
    Unknown1096(500)
    Unknown1099(100)
    Unknown1000(93000)
    teleportRelativeY(240000)

@State
def rwief401_Hit():

    def upon_IMMEDIATE():
        Unknown1073(-70000)
        Unknown1096(1200)
        teleportRelativeX(25000)
        Unknown3001(192)
        Unknown4061(1)
    sprite('null', 20)	# 1-20
    Unknown4054(15)
    Unknown4047(48, 32, 16)
    Unknown23067('rwief400_hit')

@State
def rwief402_GlyphMaster():

    def upon_IMMEDIATE():
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(20)
            if (SLOT_48 == 4003):
                sendToLabel(30)
            if (SLOT_48 == 4004):
                clearUponHandler(43)
                sendToLabel(40)
    sprite('null', 32767)	# 1-32767
    GFX_0('rwief400_Glyph_Root', 100)
    label(10)
    sprite('null', 32767)	# 32768-65534
    GFX_0('rwief400_dash', 100)
    Unknown21012('72776965663430305f476c7970685f706c75733031000000000000000000000020000000')
    label(20)
    sprite('null', 32767)	# 65535-98301
    Unknown21012('72776965663430305f476c7970685f706c75733032000000000000000000000020000000')
    label(30)
    sprite('null', 32767)	# 98302-131068
    Unknown26('rwief400_dash')
    Unknown26('rwief400_Glyph_Root')
    label(40)
    sprite('null', 20)	# 131069-131088
    Unknown21012('72776965663430305f476c79706800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430305f476c7970685f706c75733031000000000000000000000021000000')
    Unknown21012('72776965663430305f476c7970685f706c75733032000000000000000000000021000000')

@State
def rwief402_Slash_Hit():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('72776965663430325f736c6173685f4d6f64656c30310000000000000000000020000000')
    Unknown21012('72776965663430325f736c6173685f426c6f6f6d30310000000000000000000020000000')
    Unknown21012('72776965663430325f736c61736800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430325f736c6173685f466c61726500000000000000000000000020000000')
    Unknown21012('72776965663430325f45585f44756d6d7930310000000000000000000000000021000000')

@State
def rwief402_Slash_End():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief402_slash')
    Unknown21012('72776965663430325f45585f44756d6d7930310000000000000000000000000020000000')
    Unknown21012('72776965663430325f45585f44756d6d7930320000000000000000000000000020000000')
    Unknown21012('72776965663430325f45585f44756d6d7930330000000000000000000000000020000000')

@State
def rwief402_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        sendToLabelUpon(32, 0)
        Unknown2055(120)
    sprite('vref_rwi400_00', 2)	# 1-2
    GFX_0('rwief402_slash_Flare', 0)
    GFX_0('rwief402_slash_Model01', 0)
    GFX_0('rwief402_slash_Bloom01', 0)
    GFX_0('rwief402_EX_Dummy01', 0)
    sprite('vref_rwi400_01', 1)	# 3-3
    sprite('vref_rwi400_02', 2)	# 4-5
    sprite('vref_rwi400_03', 3)	# 6-8
    sprite('vref_rwi400_04', 2)	# 9-10
    GFX_0('rwief_slash_dustA_loop', 0)
    GFX_0('rwief_slash_dustA_loop', 0)
    sprite('vref_rwi400_05', 32767)	# 11-32777
    label(0)
    sprite('null', 14)	# 32778-32791
    Unknown26('rwief_slash_dustA_loop')
    sprite('null', 1)	# 32792-32792
    GFX_0('rwief402_slash_Model02', 0)
    GFX_0('rwief402_slash_Bloom02', 0)
    GFX_0('rwief402_EX_Dummy02', 0)
    sprite('vref_rwi402_03', 3)	# 32793-32795
    sprite('vref_rwi402_04', 3)	# 32796-32798
    sprite('null', 3)	# 32799-32801
    sprite('vref_rwi402_05', 2)	# 32802-32803
    sprite('vref_rwi402_05', 1)	# 32804-32804
    GFX_0('rwief402_slash_Speed', 0)
    GFX_0('rwief402_EX_Dummy03', 0)
    sprite('vref_rwi402_06', 3)	# 32805-32807
    physicsXImpulse(10000)
    sprite('vref_rwi402_07', 2)	# 32808-32809
    Unknown4007(0)
    sprite('vref_rwi402_08', 2)	# 32810-32811
    sprite('vref_rwi402_09', 2)	# 32812-32813
    sprite('vref_rwi402_10', 2)	# 32814-32815
    sprite('null', 2)	# 32816-32817

@State
def rwief402_slash_Model01():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        Unknown4003('72776965663430325f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(420000)
        Unknown1007(224000)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    Unknown1096(0)
    label(0)
    sprite('null', 12)	# 32768-32779
    Unknown1096(3700)
    Unknown1064(5550)
    Unknown1059(92)
    Unknown1067(-92)
    physicsXImpulse(4000)
    Unknown4003('72776965663430325f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief402_slash_Bloom01():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        teleportRelativeX(420000)
        Unknown1007(224000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    Unknown1096(0)
    label(0)
    sprite('vref_rwi402_00b', 5)	# 32768-32772
    Unknown1056(1000)
    Unknown1064(1500)
    Unknown1059(25)
    Unknown1067(-25)
    physicsXImpulse(4000)
    sprite('vref_rwi402_01b', 3)	# 32773-32775
    Unknown3004(-36)
    sprite('vref_rwi402_02b', 4)	# 32776-32779

@State
def rwief402_EX_Dummy01():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)
        Unknown1056(1000)
        Unknown1064(1500)
        Unknown1059(25)
        Unknown1067(-25)
        physicsXImpulse(4000)
        teleportRelativeX(420000)
        Unknown1007(224000)

        def upon_32():
            Unknown4007(0)
            Unknown13(25)
        sendToLabelUpon(33, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 1)	# 32768-32768
    sprite('vref_rwi402_00b', 20)	# 32769-32788
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_18', 1)
    GFX_0('rwief_slash_dust_16', 2)
    GFX_0('rwief_slash_dust_18', 3)
    GFX_0('rwief_slash_dust_20', 4)
    GFX_0('rwief_slash_dust_22', 5)
    GFX_0('rwief_slash_dust_24', 6)
    GFX_0('rwief_slash_dust_26', 7)

@State
def rwief402_slash_Model02():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        Unknown1096(3700)
        teleportRelativeX(-10000)
        Unknown1007(360000)
        Unknown23122(64)
    sprite('null', 1)	# 1-1
    sprite('null', 5)	# 2-6
    Unknown4003('72776965663430325f736c61736830322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(52)
    sprite('null', 5)	# 7-11
    Unknown1099(18)
    sprite('null', 2)	# 12-13
    Unknown1099(0)

@State
def rwief402_slash_Bloom02():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        teleportRelativeX(-10000)
        Unknown1007(360000)
    sprite('null', 1)	# 1-1
    sprite('vref_rwi402_03b', 3)	# 2-4
    Unknown1099(14)
    sprite('keep', 2)	# 5-6
    Unknown3004(-42)
    sprite('keep', 4)	# 7-10
    Unknown1099(5)

@State
def rwief402_EX_Dummy02():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)
        teleportRelativeX(-10000)
        Unknown1007(360000)

        def upon_32():
            Unknown4007(0)
            Unknown13(25)
    sprite('null', 1)	# 1-1
    sprite('null', 5)	# 2-6
    sprite('vref_rwi402_03b', 2)	# 7-8
    Unknown1099(14)
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_16', 1)
    GFX_0('rwief_slash_dust_18', 2)
    GFX_0('rwief_slash_dust_18', 3)
    GFX_0('rwief_slash_dust_20', 4)
    GFX_0('rwief_slash_dust_20', 5)
    GFX_0('rwief_slash_dust_22', 6)
    GFX_0('rwief_slash_dust_20', 7)
    GFX_0('rwief_slash_dust_22', 8)
    GFX_0('rwief_slash_dust_22', 9)
    GFX_0('rwief_slash_dust_24', 10)
    GFX_0('rwief_slash_dust_22', 11)
    GFX_0('rwief_slash_dust_24', 12)
    GFX_0('rwief_slash_dust_24', 13)
    GFX_0('rwief_slash_dust_26', 14)
    GFX_0('rwief_slash_dust_26', 15)
    sprite('null', 5)	# 9-13
    Unknown1099(5)
    sprite('null', 10)	# 14-23

@State
def rwief402_slash_Speed():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4010(2)
        Unknown23122(64)
        Unknown1056(-3000)
        Unknown1064(3700)
        Unknown1059(80)
        Unknown1067(100)
        Unknown1072(90000)
        teleportRelativeX(10000)
        Unknown1007(320000)
    sprite('null', 1)	# 1-1
    sprite('null', 3)	# 2-4
    Unknown4003('72776965663430315f73706565642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 5-9
    Unknown3004(-42)

@State
def rwief402_EX_Dummy03():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)

        def upon_32():
            Unknown4007(0)
            Unknown13(25)
    sprite('null', 1)	# 1-1
    sprite('vref_rwi402_06', 20)	# 2-21
    Unknown1099(14)
    GFX_0('rwief_slash_dust_16', 0)
    GFX_0('rwief_slash_dust_18', 1)
    GFX_0('rwief_slash_dust_20', 2)
    GFX_0('rwief_slash_dust_18', 3)
    GFX_0('rwief_slash_dust_20', 4)
    GFX_0('rwief_slash_dust_22', 5)
    GFX_0('rwief_slash_dust_24', 6)
    GFX_0('rwief_slash_dust_22', 7)
    GFX_0('rwief_slash_dust_26', 8)

@State
def rwief402_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 2)	# 1-2
    Unknown1000(-42000)
    teleportRelativeY(92000)
    sprite('null', 3)	# 3-5
    Unknown1000(161000)
    teleportRelativeY(267000)
    sprite('null', 3)	# 6-8
    Unknown1099(-100)
    Unknown1000(144000)
    teleportRelativeY(227000)
    sprite('null', 32767)	# 9-32775
    Unknown1056(1400)
    Unknown1099(0)
    Unknown1000(264000)
    teleportRelativeY(119000)
    label(0)
    sprite('null', 15)	# 32776-32790
    Unknown1096(0)
    sprite('null', 3)	# 32791-32793
    Unknown1096(1400)
    Unknown1099(-150)
    Unknown1000(150000)
    teleportRelativeY(370000)
    sprite('null', 3)	# 32794-32796
    Unknown1000(190000)
    teleportRelativeY(325000)
    sprite('null', 3)	# 32797-32799
    Unknown1096(0)
    Unknown1099(0)
    sprite('null', 3)	# 32800-32802
    Unknown1096(1200)
    Unknown1000(260000)
    teleportRelativeY(285000)

@State
def rwief402_Hit():

    def upon_IMMEDIATE():
        Unknown1056(1200)
        Unknown1064(800)
        Unknown3001(128)
        Unknown4061(1)
    sprite('null', 20)	# 1-20
    Unknown4054(15)
    Unknown4047(48, 32, 16)
    Unknown23067('rwief400_hit')

@State
def rwief403A_GlyphMaster():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(45000)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(20)
            if (SLOT_48 == 4003):
                sendToLabel(30)
            if (SLOT_48 == 4004):
                clearUponHandler(43)
                sendToLabel(40)
    sprite('null', 8)	# 1-8
    GFX_0('rwief403_Glyph', 0)
    sprite('null', 32767)	# 9-32775
    label(10)
    sprite('null', 32767)	# 32776-65542
    GFX_0('rwief403A_Speed', 0)
    label(20)
    sprite('null', 32767)	# 65543-98309
    label(30)
    sprite('null', 32767)	# 98310-131076
    label(40)
    sprite('null', 3)	# 131077-131079
    Unknown26('rwief403_Glyph')
    Unknown26('rwief403A_slash')
    Unknown21012('72776965663430335f476c79706800000000000000000000000000000000000020000000')
    Unknown21012('7277696566343033415f45585f44756d6d79000000000000000000000000000020000000')

@State
def rwief403_Glyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4007(3)
        Unknown4006(2)
        Unknown1007(295000)
        teleportRelativeX(-65000)
    sprite('null', 4)	# 1-4
    Unknown4003('72776965665f676c7970685f73746172743230660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)	# 5-12
    SFX_3('rwise_43')
    sprite('null', 8)	# 13-20
    Unknown4007(0)
    sprite('null', 10)	# 21-30
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)	# 31-36
    Unknown1099(-183)

@State
def rwief403A_Speed():

    def upon_IMMEDIATE():
        Unknown1007(230000)
        teleportRelativeX(0)
        Unknown1072(45000)
        Unknown4061(1)
    sprite('null', 2)	# 1-2
    Unknown4048(45000)
    Unknown4045('7277695f3430336461736800000000000000000000000000000000000000000064000000')
    Unknown4047(48, 32, 16)
    Unknown4048(45000)
    Unknown4045('7277695f3430336461736842000000000000000000000000000000000000000064000000')
    GFX_0('rwief403A_dashring01', 0)
    sprite('null', 2)	# 3-4
    GFX_0('rwief403A_dashring02', 0)

@State
def rwief403A_dashring01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(1200, 1500)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(900)
    Unknown3004(-12)
    sprite('null', 12)	# 5-16
    Unknown1099(500)

@State
def rwief403A_dashring02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(99998)
        Unknown1007(-57701)
        Unknown1102(600, 800)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(700)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(400)

@State
def rwief403A_Slash_Signal():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('7277696566343033415f736c617368000000000000000000000000000000000020000000')

@State
def rwief403A_Slash_End():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief403A_slash')
    Unknown21012('7277696566343033415f45585f44756d6d79000000000000000000000000000020000000')

@State
def rwief403A_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown2055(120)
        sendToLabelUpon(32, 0)
    sprite('vref_rwi403_00', 3)	# 1-3
    GFX_0('rwief403A_slash_Flare', 100)
    sprite('vref_rwi403_01', 3)	# 4-6
    Unknown1073(13000)
    teleportRelativeX(-43000)
    sprite('vref_rwi403_02', 32767)	# 7-32773
    GFX_0('rwief_slash_dustA_loop', 0)
    GFX_0('rwief_slash_dustA_loop', 2)
    GFX_0('rwief_slash_dustA_loop', 4)
    label(0)
    sprite('null', 3)	# 32774-32776
    GFX_0('rwief403A_slash_2D', 0)
    GFX_0('rwief403A_EX_Dummy', 100)
    Unknown26('rwief_slash_dustA_loop')
    sprite('null', 12)	# 32777-32788

@State
def rwief403A_slash_2D():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        physicsXImpulse(1500)
        physicsYImpulse(-950)
    sprite('vref_rwi403_03', 3)	# 1-3
    Unknown1072(40000)
    Unknown1000(290000)
    teleportRelativeY(10000)
    sprite('vref_rwi403_04', 3)	# 4-6
    Unknown1000(340000)
    Unknown1096(1020)
    Unknown1059(-20)
    Unknown1067(-20)
    sprite('vref_rwi403_05', 3)	# 7-9
    sprite('vref_rwi403_06', 3)	# 10-12
    Unknown1007(-8000)

@State
def rwief403A_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    sprite('vref_rwi403_04', 20)	# 4-23
    Unknown1072(40000)
    Unknown1000(340000)
    teleportRelativeY(10000)
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000007000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3232000000000000000000000000000a000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3138000000000000000000000000000b000000')
    sprite('null', 1)	# 24-24
    Unknown14()
    label(0)
    sprite('null', 1)	# 25-25
    Unknown4007(0)
    sprite('null', 1)	# 26-26
    Unknown14()

@State
def rwief403A_Hit():

    def upon_IMMEDIATE():
        Unknown1056(1800)
        Unknown1072(-70000)
        teleportRelativeX(15000)
        Unknown3001(255)
        Unknown4061(1)
    sprite('null', 20)	# 1-20
    Unknown4054(15)
    Unknown4047(48, 32, 16)
    Unknown23067('rwief400_hit')

@State
def rwief403A_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
    sprite('null', 3)	# 1-3
    Unknown1000(200000)
    teleportRelativeY(128000)
    Unknown1096(400)
    Unknown1099(150)

@State
def rwief403B_GlyphMaster():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(30000)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(20)
            if (SLOT_48 == 4003):
                sendToLabel(30)
            if (SLOT_48 == 4004):
                clearUponHandler(43)
                sendToLabel(40)
    sprite('null', 8)	# 1-8
    GFX_0('rwief403_Glyph', 0)
    sprite('null', 32767)	# 9-32775
    label(10)
    sprite('null', 32767)	# 32776-65542
    GFX_0('rwief403B_Speed', 0)
    label(20)
    sprite('null', 32767)	# 65543-98309
    label(30)
    sprite('null', 32767)	# 98310-131076
    label(40)
    sprite('null', 3)	# 131077-131079
    Unknown26('rwief403_Glyph')
    Unknown26('rwief403B_slash')
    sprite('null', 20)	# 131080-131099
    Unknown21012('72776965663430345f476c7970685f506c75730000000000000000000000000020000000')

@State
def rwief403B_Speed():

    def upon_IMMEDIATE():
        Unknown1007(230000)
        teleportRelativeX(50000)
        Unknown1072(30000)
        Unknown4061(1)
    sprite('null', 2)	# 1-2
    Unknown4048(30000)
    Unknown4045('7277695f3430336461736800000000000000000000000000000000000000000064000000')
    Unknown4047(48, 32, 16)
    Unknown4048(30000)
    Unknown4045('7277695f3430336461736842000000000000000000000000000000000000000064000000')
    GFX_0('rwief403B_dashring01', 0)
    sprite('null', 2)	# 3-4
    GFX_0('rwief403B_dashring02', 0)

@State
def rwief403B_dashring01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(1200, 1500)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(900)
    Unknown3004(-12)
    sprite('null', 12)	# 5-16
    Unknown1099(500)

@State
def rwief403B_dashring02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(99998)
        Unknown1007(-57701)
        Unknown1102(600, 800)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(700)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(400)

@State
def rwief403B_Slash_Signal():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('7277696566343033425f736c617368000000000000000000000000000000000020000000')

@State
def rwief403B_Slash_End():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief403B_slash')
    Unknown21012('7277696566343033425f45585f44756d6d79000000000000000000000000000020000000')

@State
def rwief403B_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown2055(120)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    sprite('vref_rwi403_00', 3)	# 4-6
    GFX_0('rwief403B_slash_Flare', 100)
    sprite('vref_rwi403_01', 3)	# 7-9
    sprite('vref_rwi403_02', 32767)	# 10-32776
    GFX_0('rwief_slash_dustA_loop', 0)
    GFX_0('rwief_slash_dustA_loop', 2)
    GFX_0('rwief_slash_dustA_loop', 4)
    label(0)
    sprite('null', 3)	# 32777-32779
    GFX_0('rwief403B_slash_2D', 0)
    GFX_0('rwief403B_EX_Dummy', 100)
    Unknown26('rwief_slash_dustA_loop')
    sprite('null', 12)	# 32780-32791

@State
def rwief403B_slash_2D():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown1072(35000)
        teleportRelativeX(320000)
        Unknown1007(10000)
        physicsXImpulse(1500)
        physicsYImpulse(-950)
    sprite('vref_rwi403_03', 3)	# 1-3
    sprite('vref_rwi403_04', 3)	# 4-6
    Unknown1096(1020)
    Unknown1059(-20)
    Unknown1067(-20)
    sprite('vref_rwi403_05', 3)	# 7-9
    sprite('vref_rwi403_06', 3)	# 10-12
    Unknown1007(-8000)

@State
def rwief403B_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    sprite('vref_rwi403_04', 20)	# 4-23
    Unknown1072(40000)
    Unknown1000(340000)
    teleportRelativeY(10000)
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000007000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3232000000000000000000000000000a000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3138000000000000000000000000000b000000')
    sprite('null', 1)	# 24-24
    Unknown14()
    label(0)
    sprite('null', 1)	# 25-25
    Unknown4007(0)
    sprite('null', 1)	# 26-26
    Unknown14()

@State
def rwief403B_Hit():

    def upon_IMMEDIATE():
        Unknown1056(1800)
        Unknown1072(-70000)
        teleportRelativeX(15000)
        Unknown3001(255)
        Unknown4061(1)
    sprite('null', 20)	# 1-20
    Unknown4054(15)
    Unknown4047(48, 32, 16)
    Unknown23067('rwief400_hit')

@State
def rwief403B_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
    sprite('null', 3)	# 1-3
    Unknown1000(200000)
    teleportRelativeY(128000)
    Unknown1096(400)
    Unknown1099(150)

@State
def rwief404_GlyphMaster():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(30000)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(20)
            if (SLOT_48 == 4003):
                sendToLabel(30)
            if (SLOT_48 == 4004):
                clearUponHandler(43)
                sendToLabel(40)
    sprite('null', 8)	# 1-8
    GFX_0('rwief403_Glyph', 0)
    sprite('null', 32767)	# 9-32775
    label(10)
    sprite('null', 32767)	# 32776-65542
    GFX_0('rwief404_Speed', 0)
    label(20)
    sprite('null', 32767)	# 65543-98309
    label(30)
    sprite('null', 6)	# 98310-98315
    sprite('null', 32767)	# 98316-131082
    GFX_0('rwief404_Glyph_Plus', 100)
    label(40)
    sprite('null', 3)	# 131083-131085
    Unknown26('rwief403_Glyph')
    Unknown21012('72776965663430335f476c79706800000000000000000000000000000000000020000000')
    sprite('null', 20)	# 131086-131105
    Unknown21012('72776965663430345f476c7970685f506c75730000000000000000000000000020000000')

@State
def rwief404_Glyph_Plus():

    def upon_IMMEDIATE():
        Unknown4022(3)
        callSubroutine('MagicImage_Func')
        Unknown1064(1100)
        Unknown1056(500)
        Unknown1072(-90000)
        teleportRelativeY(-10000)
        Unknown1000(0)
        sendToLabelUpon(32, 0)
    sprite('null', 18)	# 1-18
    Unknown4003('72776965665f676c7970685f73746172743235662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 7)	# 19-25
    Unknown4022(0)
    sprite('null', 20)	# 26-45
    Unknown4003('72776965665f676c7970685f6c6f6f702e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 4)	# 46-49
    sprite('null', 6)	# 50-55
    Unknown1067(-183)
    Unknown1059(-83)

@State
def rwief404_Speed():

    def upon_IMMEDIATE():
        Unknown1007(230000)
        teleportRelativeX(50000)
        Unknown1072(30000)
        Unknown4061(1)
    sprite('null', 2)	# 1-2
    Unknown4048(30000)
    Unknown4045('7277695f3430336461736800000000000000000000000000000000000000000064000000')
    Unknown4047(48, 32, 16)
    Unknown4048(30000)
    Unknown4045('7277695f3430336461736842000000000000000000000000000000000000000064000000')
    GFX_0('rwief404_dashring01', 0)
    sprite('null', 2)	# 3-4
    GFX_0('rwief404_dashring02', 0)
    sprite('null', 2)	# 5-6
    GFX_0('rwief404_dashring03', 0)

@State
def rwief404_dashring01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(1200, 1500)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(900)
    Unknown3004(-12)
    sprite('null', 12)	# 5-16
    Unknown1099(500)

@State
def rwief404_dashring02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(100000)
        Unknown1007(-57700)
        Unknown1102(400, 600)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(700)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(400)

@State
def rwief404_dashring03():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        teleportRelativeX(180000)
        Unknown1007(-103860)
        Unknown1102(700, 900)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(750)
    Unknown3004(-14)
    sprite('null', 10)	# 5-14
    Unknown1099(450)

@State
def rwief404_Slash_Signal():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown21012('72776965663430345f736c61736800000000000000000000000000000000000020000000')
    Unknown21012('72776965663430345f736c6173685f466c61726500000000000000000000000020000000')

@State
def rwief404_Slash_End():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown26('rwief404_slash')
    Unknown21012('72776965663430345f45585f44756d6d7900000000000000000000000000000020000000')

@State
def rwief404_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown2055(120)
        sendToLabelUpon(32, 0)
    sprite('vref_rwi403_00', 3)	# 1-3
    GFX_0('rwief404_slash_Flare', 100)
    sprite('vref_rwi403_01', 3)	# 4-6
    sprite('vref_rwi403_02', 32767)	# 7-32773
    GFX_0('rwief_slash_dustA_loop', 0)
    GFX_0('rwief_slash_dustA_loop', 2)
    GFX_0('rwief_slash_dustA_loop', 4)
    label(0)
    sprite('null', 3)	# 32774-32776
    GFX_0('rwief404_slash_2D', 0)
    GFX_0('rwief404_EX_Dummy', 100)
    Unknown26('rwief_slash_dustA_loop')
    sprite('null', 12)	# 32777-32788
    sprite('vref_rwi401_00', 6)	# 32789-32794
    GFX_0('rwief404_slash_Speed', 100)
    sprite('vref_rwi401_01', 5)	# 32795-32799
    sprite('vref_rwi401_02', 3)	# 32800-32802
    sprite('vref_rwi401_03', 3)	# 32803-32805

@State
def rwief404_slash_2D():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown1072(35000)
        teleportRelativeX(320000)
        Unknown1007(10000)
        physicsXImpulse(1500)
        physicsYImpulse(-950)
    sprite('vref_rwi403_03', 3)	# 1-3
    sprite('vref_rwi403_04', 3)	# 4-6
    Unknown1096(1020)
    Unknown1059(-20)
    Unknown1067(-20)
    sprite('vref_rwi403_05', 3)	# 7-9
    sprite('vref_rwi403_06', 3)	# 10-12
    Unknown1007(-8000)

@State
def rwief404_slash_Speed():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663430315f73706565642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        Unknown1096(3700)
        Unknown1056(-4200)
        Unknown1059(170)
        Unknown1067(100)
        Unknown1072(24000)
        teleportRelativeX(40000)
        Unknown1007(300000)
    sprite('null', 6)	# 1-6
    Unknown3001(0)
    sprite('null', 7)	# 7-13
    Unknown4003('72776965663430315f73706565642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3001(255)
    sprite('null', 4)	# 14-17
    Unknown3004(-51)

@State
def rwief404_EX_Dummy():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown3038(1)
        Unknown4007(3)

        def upon_32():
            Unknown4007(0)
            Unknown13(25)
    sprite('null', 3)	# 1-3
    sprite('vref_rwi403_04', 17)	# 4-20
    Unknown1072(35000)
    Unknown1000(320000)
    teleportRelativeY(10000)
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000001000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000003000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31300000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31340000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000006000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31380000000000000000000000000007000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000008000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32320000000000000000000000000009000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3234000000000000000000000000000a000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f3236000000000000000000000000000b000000')
    sprite('vref_rwi401_01', 20)	# 21-40
    Unknown1072(0)
    Unknown1000(0)
    teleportRelativeY(0)
    GFX_0('rwief_slash_dust_16', 12)
    GFX_0('rwief_slash_dust_16', 11)
    GFX_0('rwief_slash_dust_18', 10)
    GFX_0('rwief_slash_dust_18', 9)
    GFX_0('rwief_slash_dust_20', 8)
    GFX_0('rwief_slash_dust_18', 7)
    GFX_0('rwief_slash_dust_20', 6)
    GFX_0('rwief_slash_dust_22', 5)
    GFX_0('rwief_slash_dust_20', 4)
    GFX_0('rwief_slash_dust_22', 3)
    GFX_0('rwief_slash_dust_24', 2)
    GFX_0('rwief_slash_dust_22', 1)
    GFX_0('rwief_slash_dust_26', 0)
    sprite('null', 1)	# 41-41
    Unknown14()

@State
def rwief404_Hit():

    def upon_IMMEDIATE():
        Unknown1056(1800)
        Unknown1072(-70000)
        teleportRelativeX(15000)
        Unknown3001(255)
        Unknown4061(1)
    sprite('null', 20)	# 1-20
    Unknown4054(15)
    Unknown4047(48, 32, 16)
    Unknown23067('rwief400_hit')

@State
def rwief404_slash_Flare():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965665f666c61726530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown23122(64)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1000(200000)
    teleportRelativeY(128000)
    Unknown1096(400)
    Unknown1099(150)
    sprite('null', 32767)	# 4-32770
    Unknown1096(0)
    Unknown1099(0)
    label(0)
    sprite('null', 15)	# 32771-32785
    sprite('null', 6)	# 32786-32791
    Unknown1096(500)
    Unknown1099(100)
    Unknown1000(93000)
    teleportRelativeY(240000)

@State
def rwief430():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
        sendToLabelUpon(37, 5)
        sendToLabelUpon(38, 6)
        sendToLabelUpon(41, 9)

        def upon_40():
            GFX_0('rwief430_Glyph02', -1)
        loopRelated(17, 360)

        def upon_17():
            sendToLabel(9)
    sprite('null', 32767)	# 1-32767
    GFX_0('rwief430_Glyph01', -1)
    label(0)
    sprite('null', 32767)	# 32768-65534
    GFX_0('rwief430_01', -1)
    label(1)
    sprite('null', 2)	# 65535-65536
    GFX_0('rwief430_02', -1)
    sprite('null', 32767)	# 65537-98303
    GFX_0('rwief430_Glyph03', -1)
    label(2)
    sprite('null', 2)	# 98304-98305
    GFX_0('rwief430_03', -1)
    sprite('null', 32767)	# 98306-131072
    GFX_0('rwief430_Glyph04', -1)
    label(3)
    sprite('null', 2)	# 131073-131074
    GFX_0('rwief430_04', -1)
    sprite('null', 32767)	# 131075-163841
    GFX_0('rwief430_Glyph05', -1)
    label(4)
    sprite('null', 15)	# 163842-163856
    GFX_0('rwief430_05', -1)
    sprite('null', 1)	# 163857-163857
    GFX_0('rwief430_End_dust', -1)
    gotoLabel(9)
    label(5)
    sprite('null', 2)	# 163858-163859
    GFX_0('rwief430_05', -1)
    sprite('null', 32767)	# 163860-196626
    GFX_0('rwief430_Glyph06', -1)
    label(6)
    sprite('null', 10)	# 196627-196636
    GFX_0('rwief430_06', -1)
    GFX_0('rwief430_Wind', -1)
    sprite('null', 30)	# 196637-196666
    GFX_0('rwief430_DustOD', -1)
    label(9)
    sprite('null', 30)	# 196667-196696
    GFX_0('rwief430_GlyphEnd', -1)

@State
def rwief430_GlyphEnd():

    def upon_IMMEDIATE():
        pass
    sprite('null', 3)	# 1-3
    Unknown21012('72776965663433305f476c79706830310000000000000000000000000000000020000000')
    Unknown21012('72776965663433305f476c79706830320000000000000000000000000000000020000000')
    Unknown21012('72776965663433305f476c79706830330000000000000000000000000000000020000000')
    Unknown21012('72776965663433305f476c79706830340000000000000000000000000000000020000000')
    Unknown21012('72776965663433305f476c79706830350000000000000000000000000000000020000000')
    Unknown21012('72776965663433305f476c79706830360000000000000000000000000000000020000000')

@Subroutine
def rwief430_Bake_Func():
    Unknown3033()
    Unknown4061(1)
    Unknown1056(1200)
    Unknown1064(600)
    Unknown1059(40)

@State
def rwief430_01_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        Unknown4061(1)
        Unknown1007(-1000)
        Unknown3033()
        Unknown4013(2)
        Unknown4006(2)
        Unknown4007(2)
        Unknown23122(64)
    sprite('null', 8)	# 1-8
    Unknown4003('72776965663433305f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief430_01():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        Unknown1007(120000)
        Unknown3033()
        Unknown1056(1000)
        physicsXImpulse(10000)
    sprite('vref_rwi430_00A', 2)	# 1-2
    GFX_0('rwief430_Flash', -1)
    Unknown21012('72776965663433305f476c79706830310000000000000000000000000000000029000000')
    sprite('vref_rwi430_01', 3)	# 3-5
    teleportRelativeX(1100000)
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing01', 0)
    GFX_0('rwief430_DashRing02', 1)
    GFX_0('rwief430_01_dust', -1)
    Unknown1056(1500)
    Unknown1064(1000)
    Unknown1067(-40)
    sprite('vref_rwi430_02', 3)	# 6-8
    sprite('vref_rwi430_03', 2)	# 9-10
    sprite('vref_rwi430_04', 2)	# 11-12
    sprite('vref_rwi430_05', 2)	# 13-14
    sprite('vref_rwi430_06', 2)	# 15-16

@State
def rwief430_02():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        teleportRelativeX(-900000)
        Unknown1007(400000)
        Unknown1072(-16000)
        Unknown2005()
    sprite('vref_rwi430_00', 2)	# 1-2
    GFX_0('rwief430_Flash', -1)
    Unknown21012('72776965663433305f476c79706830320000000000000000000000000000000029000000')
    sprite('vref_rwi430_01', 3)	# 3-5
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing01', 0)
    GFX_0('rwief430_DashRing03', 1)
    GFX_0('rwief430_02_dust', -1)
    Unknown1064(1000)
    Unknown1067(-40)
    sprite('vref_rwi430_02', 3)	# 6-8
    sprite('vref_rwi430_03', 2)	# 9-10
    sprite('vref_rwi430_04', 2)	# 11-12
    sprite('vref_rwi430_05', 2)	# 13-14
    sprite('vref_rwi430_06', 2)	# 15-16

@State
def rwief430_03():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        teleportRelativeX(1200000)
        Unknown1007(560000)
        Unknown1072(-16000)
    sprite('vref_rwi430_00', 2)	# 1-2
    GFX_0('rwief430_Flash', -1)
    Unknown21012('72776965663433305f476c79706830330000000000000000000000000000000029000000')
    sprite('vref_rwi430_01', 3)	# 3-5
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing01', 1)
    GFX_0('rwief430_DashRing02', 2)
    GFX_0('rwief430_DashRing03', 4)
    GFX_0('rwief430_02_dust', -1)
    Unknown1064(1000)
    Unknown1067(-40)
    sprite('vref_rwi430_02', 3)	# 6-8
    sprite('vref_rwi430_03', 2)	# 9-10
    sprite('vref_rwi430_04', 2)	# 11-12
    sprite('vref_rwi430_05', 2)	# 13-14
    sprite('vref_rwi430_06', 2)	# 15-16

@State
def rwief430_04():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        teleportRelativeX(-900000)
        Unknown1007(500000)
        Unknown1072(-16000)
        Unknown2005()
    sprite('vref_rwi430_00', 2)	# 1-2
    GFX_0('rwief430_Flash', -1)
    Unknown21012('72776965663433305f476c79706830340000000000000000000000000000000029000000')
    sprite('vref_rwi430_01', 3)	# 3-5
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing01', 1)
    GFX_0('rwief430_DashRing02', 2)
    GFX_0('rwief430_DashRing03', 4)
    GFX_0('rwief430_02_dust', -1)
    Unknown1064(1000)
    Unknown1067(-40)
    sprite('vref_rwi430_02', 3)	# 6-8
    sprite('vref_rwi430_03', 2)	# 9-10
    sprite('vref_rwi430_04', 2)	# 11-12
    sprite('vref_rwi430_05', 2)	# 13-14
    sprite('vref_rwi430_06', 2)	# 15-16

@State
def rwief430_05():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        teleportRelativeX(650000)
        Unknown1007(700000)
        Unknown1072(-30000)
    sprite('vref_rwi430_00', 2)	# 1-2
    GFX_0('rwief430_Flash', -1)
    Unknown21012('72776965663433305f476c79706830350000000000000000000000000000000029000000')
    sprite('vref_rwi430_01', 3)	# 3-5
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing01', 1)
    GFX_0('rwief430_DashRing02', 2)
    GFX_0('rwief430_DashRing03', 4)
    GFX_0('rwief430_05_dust', -1)
    Unknown1064(1000)
    Unknown1067(-40)
    sprite('vref_rwi430_02', 3)	# 6-8
    sprite('vref_rwi430_03', 2)	# 9-10
    sprite('vref_rwi430_04', 2)	# 11-12
    sprite('vref_rwi430_05', 2)	# 13-14
    sprite('vref_rwi430_06', 2)	# 15-16

@State
def rwief430_06():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        teleportRelativeX(0)
        Unknown1007(-500000)
        physicsYImpulse(-10000)
        Unknown1072(90000)
    sprite('vref_rwi430_00', 2)	# 1-2
    GFX_0('rwief430_Flash', -1)
    Unknown21012('72776965663433305f476c79706830360000000000000000000000000000000029000000')
    sprite('vref_rwi430_01', 1)	# 3-3
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing05', 4)
    GFX_0('rwief430_DashRing04', 5)
    GFX_0('rwief430_DashRing03', 7)
    GFX_0('rwief430_06_dust', -1)
    Unknown1064(1200)
    Unknown1067(-40)
    sprite('vref_rwi430_01', 2)	# 4-5
    GFX_0('rwief430_DashRing04', 8)
    GFX_0('rwief430_DashRing02', 10)
    sprite('vref_rwi430_02', 3)	# 6-8
    sprite('vref_rwi430_03', 3)	# 9-11
    sprite('vref_rwi430_04', 3)	# 12-14
    sprite('vref_rwi430_05', 3)	# 15-17
    sprite('vref_rwi430_06', 3)	# 18-20

@State
def rwief430_Glyph01():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4009(2)
        Unknown1072(-90000)
        Unknown1056(500)
        Unknown1064(1100)
        sendToLabelUpon(32, 0)

        def upon_41():
            GFX_0('rwief430_Glyph_Particle', -1)
    sprite('null', 25)	# 1-25
    Unknown4003('72776965665f676c7970685f73746172743235660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 26-32792
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 6)	# 32793-32798
    Unknown1059(-83)
    Unknown1067(-183)
    Unknown1091(-166)

@State
def rwief430_Glyph02():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown1072(-164000)
        Unknown1056(350)
        Unknown1064(1100)
        teleportRelativeX(830000)
        Unknown1007(70000)
        sendToLabelUpon(32, 0)

        def upon_41():
            GFX_0('rwief430_Glyph_Particle', -1)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743230660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 21-32787
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 6)	# 32788-32793
    Unknown1059(-58)
    Unknown1067(-183)
    Unknown1091(-166)

@State
def rwief430_Glyph03():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown1072(-16000)
        Unknown1056(800)
        Unknown1064(1100)
        teleportRelativeX(-800000)
        Unknown1007(250000)
        sendToLabelUpon(32, 0)

        def upon_41():
            GFX_0('rwief430_Glyph_Particle', -1)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743230660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 21-32787
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 6)	# 32788-32793
    Unknown1059(-133)
    Unknown1067(-183)
    Unknown1091(-166)

@State
def rwief430_Glyph04():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown1072(-164000)
        Unknown1056(800)
        Unknown1064(1100)
        teleportRelativeX(900000)
        Unknown1007(250000)
        sendToLabelUpon(32, 0)

        def upon_41():
            GFX_0('rwief430_Glyph_Particle', -1)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743230660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 21-32787
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 6)	# 32788-32793
    Unknown1059(-133)
    Unknown1067(-183)
    Unknown1091(-166)

@State
def rwief430_Glyph05():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown1072(-30000)
        Unknown1056(350)
        Unknown1064(1100)
        teleportRelativeX(-800000)
        Unknown1007(270000)
        sendToLabelUpon(32, 0)

        def upon_41():
            GFX_0('rwief430_Glyph_Particle', -1)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743230660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)	# 21-32787
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 6)	# 32788-32793
    Unknown1059(-58)
    Unknown1067(-183)
    Unknown1091(-166)

@State
def rwief430_Glyph06():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown1072(90000)
        Unknown1056(700)
        Unknown1064(1400)
        teleportRelativeX(180000)
        Unknown1007(500000)
        sendToLabelUpon(32, 0)

        def upon_41():
            GFX_0('rwief430_Glyph_Particle', -1)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743230660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f676c7970685f7a697a6f6b750000000000000000000000ffffffff')
    sprite('null', 32767)	# 21-32787
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 6)	# 32788-32793
    Unknown1059(-116)
    Unknown1067(-233)
    Unknown1091(-166)

@State
def rwief430_Flash():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4006(2)
    sprite('null', 40)	# 1-40
    Unknown4047(48, 32, 64)
    Unknown23067('rwief430_flash')
    GFX_0('rwief430_Speed', -1)

@State
def rwief430_Speed():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4006(2)
    sprite('null', 40)	# 1-40
    Unknown4047(48, 40, 32)
    Unknown23067('rwief430_speed')

@State
def rwief430_01_dust():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown3038(1)
        Unknown4061(1)
    sprite('vref_rwi430_01', 1)	# 1-1
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000000000000')
    sprite('vref_rwi430_01', 1)	# 2-2
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000001000000')
    sprite('vref_rwi430_01', 1)	# 3-3
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000002000000')
    sprite('vref_rwi430_01', 1)	# 4-4
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000003000000')
    sprite('vref_rwi430_01', 1)	# 5-5
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000004000000')
    sprite('vref_rwi430_01', 1)	# 6-6
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000005000000')
    sprite('vref_rwi430_01', 1)	# 7-7
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000006000000')
    sprite('vref_rwi430_01', 1)	# 8-8
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000007000000')
    sprite('vref_rwi430_01', 1)	# 9-9
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000008000000')
    sprite('vref_rwi430_01', 1)	# 10-10
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000009000000')

@State
def rwief430_02_dust():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown3038(1)
        Unknown4061(1)
    sprite('vref_rwi430_01', 1)	# 1-1
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000000000000')
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000001000000')
    sprite('vref_rwi430_01', 1)	# 2-2
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000002000000')
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000003000000')
    sprite('vref_rwi430_01', 1)	# 3-3
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000004000000')
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000005000000')
    sprite('vref_rwi430_01', 1)	# 4-4
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000006000000')
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000007000000')
    sprite('vref_rwi430_01', 1)	# 5-5
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000008000000')
    Unknown4048(-16000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000009000000')

@State
def rwief430_05_dust():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown3038(1)
        Unknown4061(1)
    sprite('vref_rwi430_01', 1)	# 1-1
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000002000000')
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000003000000')
    sprite('vref_rwi430_01', 1)	# 2-2
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000004000000')
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000005000000')
    sprite('vref_rwi430_01', 1)	# 3-3
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000006000000')
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000007000000')
    sprite('vref_rwi430_01', 1)	# 4-4
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000008000000')
    Unknown4048(-30000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000009000000')

@State
def rwief430_06_dust():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown3038(1)
        Unknown4061(1)
    sprite('vref_rwi430_01', 1)	# 1-1
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000002000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000003000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000004000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000005000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000006000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000007000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000008000000')
    Unknown4048(90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573740000000000000000000000000000000000000009000000')

@State
def rwief430_End_dust():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4061(1)
    sprite('null', 4)	# 1-4
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')
    sprite('null', 4)	# 5-8
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')
    sprite('null', 4)	# 9-12
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')
    sprite('null', 5)	# 13-17
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')
    sprite('null', 5)	# 18-22
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')
    sprite('null', 5)	# 23-27
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')
    sprite('null', 5)	# 28-32
    Unknown4048(-90000)
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744200000000000000000000000000000000000009000000')

@State
def rwief430_DustOD():

    def upon_IMMEDIATE():
        Unknown4061(1)
    sprite('null', 1)	# 1-1
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663433305f647573744f440000000000000000000000000000000000ffffffff')

@State
def rwief430_Glyph_Particle():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4006(2)
        Unknown1073(90000)
    sprite('null', 80)	# 1-80
    Unknown4047(48, 40, 32)
    Unknown23067('rwief430_glyph')

@State
def rwief430_Wind():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown1096(5000)
        Unknown1056(6000)
        Unknown1099(-50)
        Unknown2005()
        Unknown4003('72776965663433305f77696e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
    sprite('null', 2)	# 1-2
    sprite('null', 5)	# 3-7
    Unknown3004(36)
    sprite('null', 13)	# 8-20
    Unknown3004(0)
    sprite('null', 10)	# 21-30
    Unknown1099(-200)
    Unknown3004(-18)

@State
def rwief430_DashRing01():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(1200, 1500)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(900)
    Unknown3004(-12)
    sprite('null', 12)	# 5-16
    Unknown1099(500)

@State
def rwief430_DashRing02():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(400, 600)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(700)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(400)

@State
def rwief430_DashRing03():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(700, 900)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(750)
    Unknown3004(-14)
    sprite('null', 10)	# 5-14
    Unknown1099(450)

@State
def rwief430_DashRing04():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(1200, 1500)
        Unknown3001(200)
    sprite('null', 4)	# 1-4
    Unknown1099(1300)
    Unknown3004(-12)
    sprite('null', 12)	# 5-16
    Unknown1099(600)

@State
def rwief430_DashRing05():

    def upon_IMMEDIATE():
        Unknown4003('72776965665f6461736872696e6730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3033()
        Unknown1102(400, 600)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    Unknown1099(1100)
    Unknown3004(-16)
    sprite('null', 9)	# 4-12
    Unknown1099(500)

@State
def UltimateShotMaster():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(4)
        Damage(5000)
        AttackP2(60)
        Unknown11091(30)
        Unknown9021(1)
        Unknown9266(9)
        Unknown12051(2)
        GroundedHitstunAnimation(1)
        AirPushbackY(25000)
        Unknown9168(19)
        Unknown9156(19)
        Hitstop(0)
        Unknown11001(15, 40, 40)
        Unknown3001(0)
        teleportRelativeX(150000)
        Unknown3038(1)
        loopRelated(17, 45)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 4316):
                Unknown11064(1)
                Unknown11069('UltimateShotSP_Add')

                def upon_3():
                    if Unknown2065(25):
                        clearUponHandler(3)
                        Unknown23029(3, 4317, 0)

        def upon_12():
            Unknown23029(3, 4314, 0)

        def upon_61():
            Unknown23029(3, 4315, 0)
    sprite('vrrwi_test_ultimateatk', 2)	# 1-2	 **attackbox here**
    SFX_3('rwise_47')
    GFX_0('rwief431', 0)
    Unknown1096(500)
    GFX_0('UltimateShotImage', -1)
    Unknown23029(1, 4311, 0)
    sprite('vrrwi_test_ultimateatk', 2)	# 3-4	 **attackbox here**
    teleportRelativeX(150000)
    GFX_0('UltimateShotImage', -1)
    Unknown23029(1, 4312, 0)
    Unknown1096(750)
    label(0)
    sprite('vrrwi_test_ultimateatk', 2)	# 5-6	 **attackbox here**
    teleportRelativeX(150000)
    GFX_0('UltimateShotImage', -1)
    Unknown1096(800)
    gotoLabel(0)
    label(1)
    sprite('null', 30)	# 7-36

@State
def UltimateShotImage():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(192)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 4311):
                Unknown1096(500)
            if (SLOT_48 == 4312):
                Unknown1096(750)
    sprite('vrrwi_test_ultimateatk', 32767)	# 1-32767	 **attackbox here**

@State
def rwief431():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2005()
        teleportRelativeX(20000)
        teleportRelativeY(0)

        def upon_32():
            Unknown4009(3)
            Unknown14()
            Unknown26('rwief431_IceSpikeA_Far')
            Unknown26('rwief431_IceSpikeA_Near')
            Unknown26('rwief431_IceSpikeB_Far')
            Unknown26('rwief431_IceSpikeB_Near')
            Unknown26('rwief431_IceSpikeC_Far')
            Unknown26('rwief431_IceSpikeC_Near')
            Unknown26('rwief431_IceSpikeD_Far')
            Unknown26('rwief431_IceSpikeD_Near')
            Unknown26('rwief431_IceSpikeE_Far')
            Unknown26('rwief431_IceSpikeE_Near')
            Unknown26('rwief431_IceSpikeF_Far')
            Unknown26('rwief431_IceSpikeF_Near')
            Unknown26('rwief431_IceSpikeD2_Far')
            Unknown26('rwief431_IceSpikeD2_Near')
            Unknown26('rwief431_IceSpikeE2_Far')
            Unknown26('rwief431_IceSpikeE2_Near')
            Unknown26('rwief431_IceSpikeF2_Far')
            Unknown26('rwief431_IceSpikeF2_Near')
            Unknown26('rwief431_IceSpikeA_Near_Bloom')
            Unknown26('rwief431_IceSpikeA_Far_Bloom')
            Unknown26('rwief431_IceSpikeB_Near_Bloom')
            Unknown26('rwief431_IceSpikeB_Far_Bloom')
            Unknown26('rwief431_IceSpikeC_Near_Bloom')
            Unknown26('rwief431_IceSpikeC_Far_Bloom')
            Unknown26('rwief431_IceSpikeD_Near_Bloom')
            Unknown26('rwief431_IceSpikeD_Far_Bloom')
            Unknown26('rwief431_IceSpikeE_Near_Bloom')
            Unknown26('rwief431_IceSpikeE_Far_Bloom')
            Unknown26('rwief431_IceSpikeF_Near_Bloom')
            Unknown26('rwief431_IceSpikeF_Far_Bloom')
            Unknown26('rwief431_IceSpikeD2_Near_Bloom')
            Unknown26('rwief431_IceSpikeD2_Far_Bloom')
            Unknown26('rwief431_IceSpikeE2_Near_Bloom')
            Unknown26('rwief431_IceSpikeE2_Far_Bloom')
            Unknown26('rwief431_IceSpikeF2_Near_Bloom')
            Unknown26('rwief431_IceSpikeF2_Far_Bloom')
    sprite('null', 2)	# 1-2
    GFX_0('rwief431_IceSpikeA_Far', 0)
    GFX_0('rwief431_IceSpikeA_Near', 0)
    GFX_0('rwief431_IceSpikeB_Far', 0)
    GFX_0('rwief431_IceSpikeB_Near', 0)
    GFX_0('rwief431_IceSpikeC_Far', 0)
    GFX_0('rwief431_IceSpikeC_Near', 0)
    sprite('null', 2)	# 3-4
    GFX_0('rwief431_IceSpikeD_Far', 0)
    GFX_0('rwief431_IceSpikeD_Near', 0)
    sprite('null', 2)	# 5-6
    GFX_0('rwief431_IceSpikeE_Far', 0)
    GFX_0('rwief431_IceSpikeE_Near', 0)
    sprite('null', 2)	# 7-8
    GFX_0('rwief431_IceSpikeF_Far', 0)
    GFX_0('rwief431_IceSpikeF_Near', 0)
    sprite('null', 2)	# 9-10
    teleportRelativeX(-450000)
    GFX_0('rwief431_IceSpikeD2_Far', 0)
    GFX_0('rwief431_IceSpikeD2_Near', 0)
    sprite('null', 2)	# 11-12
    GFX_0('rwief431_IceSpikeF2_Far', 0)
    GFX_0('rwief431_IceSpikeE2_Near', 0)
    sprite('null', 2)	# 13-14
    GFX_0('rwief431_IceSpikeE2_Far', 0)
    GFX_0('rwief431_IceSpikeF2_Near', 0)
    sprite('null', 2)	# 15-16
    teleportRelativeX(-450000)
    GFX_0('rwief431_IceSpikeD_Far', 0)
    GFX_0('rwief431_IceSpikeD_Near', 0)
    sprite('null', 2)	# 17-18
    GFX_0('rwief431_IceSpikeE_Far', 0)
    GFX_0('rwief431_IceSpikeE_Near', 0)
    sprite('null', 2)	# 19-20
    GFX_0('rwief431_IceSpikeF_Far', 0)
    GFX_0('rwief431_IceSpikeF_Near', 0)
    sprite('null', 2)	# 21-22
    teleportRelativeX(-450000)
    GFX_0('rwief431_IceSpikeD2_Far', 0)
    GFX_0('rwief431_IceSpikeD2_Near', 0)
    sprite('null', 2)	# 23-24
    GFX_0('rwief431_IceSpikeF2_Far', 0)
    GFX_0('rwief431_IceSpikeE2_Near', 0)
    sprite('null', 200)	# 25-224
    GFX_0('rwief431_IceSpikeE2_Far', 0)
    GFX_0('rwief431_IceSpikeF2_Near', 0)

@Subroutine
def rwief431_IceSpike_Func():
    Unknown4061(1)
    Unknown23122(4)
    Unknown3032()
    Unknown4015()
    Unknown1096(2300)
    Unknown1088(500)
    Unknown4011(3)
    Unknown4009(2)
    Unknown2055(77)

@State
def rwief431_IceSpikeA_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(170000)
        Unknown1066(90)
        Unknown1007(-10000)
        Unknown2055(73)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeA_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65415f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65415f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeA_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(170000)
        Unknown1066(90)
        Unknown1007(-10000)
        Unknown2055(73)

        def upon_STATE_END():
            GFX_0('rwief431_BreakA', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeA_Far_Bloom', 0)
    GFX_0('rwief431_ColdA', 0)
    Unknown4003('72776965663433315f6963657370696b65415f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65415f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeB_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        Unknown2055(75)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeB_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65425f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    Unknown1059(20)
    Unknown1067(20)
    sprite('null', 1)	# 2-2
    Unknown23122(32)
    sprite('null', 1)	# 3-3
    Unknown23122(16)
    sprite('null', 1)	# 4-4
    Unknown23122(8)
    sprite('null', 500)	# 5-504
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(6)

@State
def rwief431_IceSpikeB_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        Unknown2055(75)

        def upon_STATE_END():
            GFX_0('rwief431_BreakB', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeB_Far_Bloom', 0)
    GFX_0('rwief431_ColdB', 0)
    Unknown4003('72776965663433315f6963657370696b65425f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23122(63)
    Unknown1059(20)
    Unknown1067(20)
    sprite('null', 1)	# 2-2
    Unknown23122(32)
    sprite('null', 1)	# 3-3
    Unknown23122(16)
    sprite('null', 1)	# 4-4
    Unknown23122(8)
    sprite('null', 500)	# 5-504
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(6)

@State
def rwief431_IceSpikeC_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-130000)
        Unknown1007(-20000)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeC_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65435f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65435f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeC_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-130000)
        Unknown1007(-20000)

        def upon_STATE_END():
            GFX_0('rwief431_BreakC', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeC_Far_Bloom', 0)
    GFX_0('rwief431_ColdC', 0)
    Unknown4003('72776965663433315f6963657370696b65435f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65435f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeD_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-310000)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeD_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65445f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65445f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeD_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-310000)

        def upon_STATE_END():
            GFX_0('rwief431_BreakD', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeD_Far_Bloom', 0)
    GFX_0('rwief431_ColdD', 0)
    Unknown4003('72776965663433315f6963657370696b65445f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65445f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeE_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-450000)
        Unknown1066(90)
        Unknown1007(-20000)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeE_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65455f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65455f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeE_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-450000)
        Unknown1066(90)
        Unknown1007(-20000)

        def upon_STATE_END():
            GFX_0('rwief431_BreakE', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeE_Far_Bloom', 0)
    GFX_0('rwief431_ColdE', 0)
    Unknown4003('72776965663433315f6963657370696b65455f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65455f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeF_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-600000)
        Unknown1098(107)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeF_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65465f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65465f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeF_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-600000)
        Unknown1098(107)

        def upon_STATE_END():
            GFX_0('rwief431_BreakF', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeF_Far_Bloom', 0)
    GFX_0('rwief431_ColdF', 0)
    Unknown4003('72776965663433315f6963657370696b65465f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65465f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeD2_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-310000)
        Unknown1066(105)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeD2_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65445f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65445f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeD2_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-310000)
        Unknown1066(105)

        def upon_STATE_END():
            GFX_0('rwief431_BreakD', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeD2_Far_Bloom', 0)
    GFX_0('rwief431_ColdD', 0)
    Unknown4003('72776965663433315f6963657370696b65445f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65445f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeE2_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-450000)
        Unknown1007(-20000)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeE2_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65455f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65455f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeE2_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-600000)
        Unknown1007(-20000)

        def upon_STATE_END():
            GFX_0('rwief431_BreakE', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeE2_Far_Bloom', 0)
    GFX_0('rwief431_ColdE', 0)
    Unknown4003('72776965663433315f6963657370696b65455f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65455f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeF2_Near():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(9)
        teleportRelativeX(-600000)
        Unknown1066(95)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeF2_Near_Bloom', 0)
    GFX_0('rwief431_IcedGround', 0)
    Unknown4003('72776965663433315f6963657370696b65465f4e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65465f4e30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@State
def rwief431_IceSpikeF2_Far():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Func')
        Unknown23015(15)
        teleportRelativeX(-450000)
        Unknown1066(95)

        def upon_STATE_END():
            GFX_0('rwief431_BreakF', 0)
    sprite('null', 1)	# 1-1
    GFX_0('rwief431_IceSpikeF2_Far_Bloom', 0)
    GFX_0('rwief431_ColdF', 0)
    Unknown4003('72776965663433315f6963657370696b65465f4630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(20)
    Unknown1067(20)
    Unknown23122(16)
    sprite('null', 1)	# 2-2
    Unknown23122(63)
    sprite('null', 1)	# 3-3
    Unknown4003('72776965663433315f6963657370696b65465f4630322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    sprite('null', 1)	# 5-5
    Unknown23122(32)
    sprite('null', 1)	# 6-6
    Unknown1059(0)
    Unknown1067(0)
    Unknown23122(16)
    sprite('null', 1)	# 7-7
    Unknown23122(8)
    sprite('null', 500)	# 8-507
    Unknown23122(6)

@Subroutine
def rwief431_IceSpike_Bloom_Func():
    Unknown4011(3)
    Unknown4061(4)
    Unknown3033()
    Unknown1066(90)
    Unknown1099(8)
    Unknown2055(77)
    Unknown4009(2)

@Subroutine
def rwief431_Ground_Bloom_Func():
    Unknown4011(3)
    Unknown3000(0)
    Unknown4061(3)
    Unknown3033()
    Unknown4013(2)
    Unknown2055(77)
    Unknown4009(2)
    Unknown3003(60)

@State
def rwief431_IceSpikeA_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
        Unknown1066(90)
        Unknown1007(-10000)
        Unknown2055(73)
    sprite('vref_rwi431_IceSpikeA_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeA_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeA_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeA_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
        Unknown1066(90)
        Unknown2055(73)
    sprite('vref_rwi431_IceSpikeA_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeA_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeA_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeB_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
        Unknown2055(75)
    sprite('vref_rwi431_IceSpikeB_N01', 4)	# 1-4
    sprite('vref_rwi431_IceSpikeB_N01', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeB_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
        Unknown2055(75)
    sprite('vref_rwi431_IceSpikeB_F01', 4)	# 1-4
    sprite('vref_rwi431_IceSpikeB_F01', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeC_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
    sprite('vref_rwi431_IceSpikeC_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeC_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeC_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeC_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
    sprite('vref_rwi431_IceSpikeC_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeC_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeC_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeD_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
    sprite('vref_rwi431_IceSpikeD_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeD_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeD_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeD_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
    sprite('vref_rwi431_IceSpikeD_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeD_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeD_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeE_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
        Unknown1066(90)
    sprite('vref_rwi431_IceSpikeE_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeE_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeE_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeE_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
        Unknown1066(90)
    sprite('vref_rwi431_IceSpikeE_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeE_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeE_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeF_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
        Unknown1098(107)
    sprite('vref_rwi431_IceSpikeF_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeF_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeF_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeF_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
        Unknown1098(107)
    sprite('vref_rwi431_IceSpikeF_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeF_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeF_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeD2_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
        Unknown1066(105)
    sprite('vref_rwi431_IceSpikeD_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeD_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeD_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeD2_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
        Unknown1066(105)
    sprite('vref_rwi431_IceSpikeD_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeD_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeD_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeE2_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
    sprite('vref_rwi431_IceSpikeE_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeE_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeE_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeE2_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
    sprite('vref_rwi431_IceSpikeE_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeE_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeE_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeF2_Near_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(10)
        Unknown1066(95)
    sprite('vref_rwi431_IceSpikeF_N01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeF_N02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeF_N02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_IceSpikeF2_Far_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_IceSpike_Bloom_Func')
        Unknown23015(14)
        Unknown1066(95)
    sprite('vref_rwi431_IceSpikeF_F01', 2)	# 1-2
    sprite('vref_rwi431_IceSpikeF_F02', 2)	# 3-4
    sprite('vref_rwi431_IceSpikeF_F02', 500)	# 5-504
    Unknown1099(0)

@State
def rwief431_BreakA():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663433315f696365627265616b5f410000000000000000000000000000000000')
    SFX_0('018_ice_break_1')

@State
def rwief431_BreakB():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663433315f696365627265616b5f420000000000000000000000000000000000')
    SFX_0('018_ice_break_1')

@State
def rwief431_BreakC():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663433315f696365627265616b5f430000000000000000000000000000000000')
    SFX_0('018_ice_break_1')

@State
def rwief431_BreakD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663433315f696365627265616b5f460000000000000000000000000000000000')

@State
def rwief431_BreakE():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663433315f696365627265616b5f460000000000000000000000000000000000')

@State
def rwief431_BreakF():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663433315f696365627265616b5f460000000000000000000000000000000000')

@Subroutine
def rwief431_Cold_Func():
    Unknown4061(1)
    Unknown3038(1)
    Unknown4011(3)
    Unknown4010(2)

@State
def rwief431_ColdA():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_Cold_Func')
    sprite('null', 1)	# 1-1
    Unknown4054(15)
    Unknown4047(32, 32, 64)
    Unknown4045('72776965663433315f627572737444000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 20)	# 2-21
    Unknown4054(15)
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f415f4c6f6f7000000000000000000000000000000000')
    gotoLabel(0)

@State
def rwief431_ColdB():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_Cold_Func')
    sprite('null', 1)	# 1-1
    Unknown4054(15)
    Unknown4047(32, 32, 64)
    Unknown4045('72776965663433315f627572737443000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 20)	# 2-21
    Unknown4054(15)
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f425f4c6f6f7000000000000000000000000000000000')
    gotoLabel(0)

@State
def rwief431_ColdC():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_Cold_Func')
    sprite('null', 1)	# 1-1
    Unknown4054(15)
    Unknown4047(32, 32, 64)
    Unknown4045('72776965663433315f627572737442000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 20)	# 2-21
    Unknown4054(15)
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f435f4c6f6f7000000000000000000000000000000000')
    gotoLabel(0)

@State
def rwief431_ColdD():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_Cold_Func')
    sprite('null', 1)	# 1-1
    Unknown4054(15)
    Unknown4047(32, 32, 64)
    Unknown4045('72776965663433315f627572737400000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 20)	# 2-21
    Unknown4054(15)
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f445f4c6f6f7000000000000000000000000000000000')
    gotoLabel(0)

@State
def rwief431_ColdE():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_Cold_Func')
    sprite('null', 1)	# 1-1
    Unknown4054(15)
    Unknown4047(32, 32, 64)
    Unknown4045('72776965663433315f627572737400000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 20)	# 2-21
    Unknown4054(15)
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f455f4c6f6f7000000000000000000000000000000000')
    gotoLabel(0)

@State
def rwief431_ColdF():

    def upon_IMMEDIATE():
        callSubroutine('rwief431_Cold_Func')
    sprite('null', 1)	# 1-1
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f46000000000000000000000000000000000000000000')
    Unknown4054(15)
    Unknown4047(32, 32, 64)
    Unknown4045('72776965663433315f627572737400000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 20)	# 2-21
    Unknown4054(15)
    Unknown4047(60, 60, 60)
    Unknown4045('72776965663433315f636f6c645f465f4c6f6f7000000000000000000000000000000000')
    gotoLabel(0)

@State
def rwief431_IcedGround():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown3032()
        Unknown23015(15)
        Unknown1066(95)
        Unknown4003('72776965665f6963656467726f756e64000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1062(1000, 1500)
        Unknown1094(800, 1500)
        Unknown3001(110)
        teleportRelativeX(100000)
    sprite('null', 120)	# 1-120
    sprite('null', 37)	# 121-157
    Unknown3004(-3)

@State
def rwief431_Charge():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3038(1)
        Unknown23022(1)
        Unknown4061(1)

        def upon_3():
            Unknown4047(48, 64, 64)
            Unknown4045('72776965663433315f636861726765000000000000000000000000000000000000000000')
    sprite('rwi431_00', 6)	# 1-6
    sprite('rwi431_01', 6)	# 7-12
    sprite('rwi431_02', 6)	# 13-18
    sprite('rwi431_03', 6)	# 19-24
    sprite('rwi431_04', 6)	# 25-30
    sprite('rwi431_05', 10)	# 31-40
    sprite('rwi431_06', 3)	# 41-43
    GFX_0('rwief431_Pillar', 100)

@State
def rwief431_Pillar():

    def upon_IMMEDIATE():
        Unknown4061(1)
        teleportRelativeX(55000)
    sprite('null', 3)	# 1-3
    Unknown4047(63, 48, 64)
    Unknown4045('72776965663433315f70696c6c6172000000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    GFX_0('rwief431_Circle', 0)
    Unknown4054(14)
    Unknown4045('72776965663433315f70696c6c6172420000000000000000000000000000000000000000')
    Unknown4047(48, 64, 64)
    Unknown4045('72776965663433315f70696c6c6172430000000000000000000000000000000000000000')

@State
def rwief431_Circle():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown1007(120000)
    sprite('null', 3)	# 1-3
    Unknown4047(48, 48, 64)
    Unknown4045('72776965663433315f636972636c65000000000000000000000000000000000000000000')

@State
def rwief355_Glyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4003('72776965663335355f676c7970682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sendToLabelUpon(32, 0)
        Unknown4009(2)
        Unknown4061(1)
    sprite('null', 2)	# 1-2
    Unknown3001(0)
    sprite('null', 5)	# 3-7
    Unknown4047(56, 56, 56)
    Unknown4045('72776965663335355f636f6c6400000000000000000000000000000000000000ffffffff')
    Unknown4003('72776965663335355f676c7970682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3001(200)
    Unknown1056(800)
    Unknown1064(300)
    Unknown1088(240)
    Unknown1059(20)
    Unknown1067(6)
    Unknown1091(6)
    sprite('null', 5)	# 8-12
    sprite('null', 3)	# 13-15
    Unknown1059(0)
    Unknown1067(0)
    Unknown1091(0)
    sprite('null', 80)	# 16-95
    GFX_0('rwief355_Sword', -1)
    sprite('null', 10)	# 96-105
    Unknown3004(-25)
    Unknown1059(-60)
    Unknown1067(-21)
    Unknown1091(-18)

@State
def rwief355_Sword():

    def upon_IMMEDIATE():
        Unknown23015(12)
        Unknown4061(1)
        Unknown23122(6)
        Unknown3032()
        Unknown4009(2)
        Unknown1096(2466)
        sendToLabelUpon(32, 0)
        GFX_0('rwief355_Sword_Bloom', -1)
    sprite('null', 10)	# 1-10
    Unknown4003('72776965663335355f73776f726430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 11-14
    Unknown4003('72776965663335355f73776f726430312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsYImpulse(2000)
    sprite('null', 8)	# 15-22
    physicsYImpulse(500)
    sprite('null', 100)	# 23-122
    physicsYImpulse(0)
    label(0)
    sprite('null', 5)	# 123-127
    Unknown4003('72776965663335355f73776f726430322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23015(10)
    teleportRelativeY(-10000)
    sprite('null', 5)	# 128-132
    Unknown4003('72776965663335355f73776f726430332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    teleportRelativeY(-30000)
    sprite('null', 5)	# 133-137
    Unknown4003('72776965663335355f73776f726430342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 138-142
    Unknown4003('72776965663335355f73776f726430352e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 143-145
    Unknown4003('72776965663335355f73776f726430362e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 146-148
    Unknown4003('72776965663335355f73776f726430372e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    teleportRelativeY(30000)
    teleportRelativeX(-100000)
    Unknown1073(30000)
    GFX_0('rwief355_slash', -1)
    sprite('null', 12)	# 149-160
    Unknown4003('72776965663335355f73776f726430382e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 24)	# 161-184
    GFX_0('rwief355_Out', -1)

@State
def rwief355_Sword_Bloom():

    def upon_IMMEDIATE():
        Unknown23015(11)
        Unknown4061(1)
        Unknown21004(80)
        Unknown3033()
        Unknown3003(50)
        Unknown4009(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown4007(2)
        Unknown1096(2466)
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    Unknown4003('72776965663335355f73776f72643030622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 110)	# 11-120
    Unknown4003('72776965663335355f73776f72643031622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 5)	# 121-125
    Unknown4003('72776965663335355f73776f72643032622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23015(1)
    sprite('null', 5)	# 126-130
    Unknown4003('72776965663335355f73776f72643033622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 131-135
    Unknown4003('72776965663335355f73776f72643034622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 136-140
    Unknown4003('72776965663335355f73776f72643035622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 141-143
    Unknown4003('72776965663335355f73776f72643036622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 144-146
    Unknown4003('72776965663335355f73776f72643037622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 147-158
    Unknown4003('72776965663335355f73776f72643038622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 24)	# 159-182

@State
def rwief355_Sword_Signal():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)	# 1-1
    Unknown21012('72776965663335355f53776f726400000000000000000000000000000000000020000000')
    Unknown21012('72776965663335355f53776f72645f426c6f6f6d00000000000000000000000020000000')

@State
def rwief355_slash():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        teleportRelativeX(550000)
        Unknown1007(285000)
        Unknown4009(2)
    sprite('null', 28)	# 1-28
    GFX_0('rwief355_slash_Model', -1)
    GFX_0('rwief355_slash_Bloom', -1)
    GFX_0('rwief355_Slash_Dust', -1)
    Unknown21012('727769656634333100000000000000000000000000000000000000000000000020000000')

@State
def rwief355_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663335355f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(3350)
        Unknown1099(16)
        Unknown23122(64)
        Unknown23015(10)
        Unknown4015()
    sprite('null', 20)	# 1-20
    sprite('null', 8)	# 21-28
    Unknown3004(-28)

@State
def rwief355_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23015(10)
        Unknown1096(2000)
        Unknown1099(10)
    sprite('vref_rwi355_00', 28)	# 1-28
    Unknown3004(-10)

@State
def rwief355_Out():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23015(10)
        Unknown3038(1)
        Unknown4006(2)
    sprite('vref_rwi355_sword_ex', 1)	# 1-1
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000000000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000001000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000002000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000003000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000004000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000005000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000006000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000007000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000008000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000009000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f757400000000000000000000000000000000000000000a000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f757400000000000000000000000000000000000000000b000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f757400000000000000000000000000000000000000000c000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f757400000000000000000000000000000000000000000d000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f757400000000000000000000000000000000000000000e000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f757400000000000000000000000000000000000000000f000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f6f7574000000000000000000000000000000000000000010000000')

@State
def rwief355_Slash_Dust():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown23015(10)
        Unknown3038(1)
        Unknown1096(2000)
        Unknown1099(10)
    sprite('vref_rwi355_00', 1)	# 1-1
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000000000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000000000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000001000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000002000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000003000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000004000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000005000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000006000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000007000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000008000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000009000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c64420000000000000000000000000000000000000a000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c64420000000000000000000000000000000000000b000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c64420000000000000000000000000000000000000c000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c64420000000000000000000000000000000000000d000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c64420000000000000000000000000000000000000e000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c64420000000000000000000000000000000000000f000000')
    Unknown4047(40, 40, 40)
    Unknown4045('72776965663335355f636f6c644200000000000000000000000000000000000010000000')
    sprite('vref_rwi355_00', 1)	# 2-2
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000001000000')
    sprite('vref_rwi355_00', 1)	# 3-3
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000002000000')
    sprite('vref_rwi355_00', 1)	# 4-4
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000003000000')
    sprite('vref_rwi355_00', 1)	# 5-5
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000004000000')
    sprite('vref_rwi355_00', 1)	# 6-6
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000005000000')
    sprite('vref_rwi355_00', 1)	# 7-7
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000006000000')
    sprite('vref_rwi355_00', 1)	# 8-8
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000007000000')
    sprite('vref_rwi355_00', 1)	# 9-9
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000008000000')
    sprite('vref_rwi355_00', 1)	# 10-10
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000009000000')
    sprite('vref_rwi355_00', 1)	# 11-11
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f64757374000000000000000000000000000a000000')
    sprite('vref_rwi355_00', 1)	# 12-12
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f64757374000000000000000000000000000b000000')
    sprite('vref_rwi355_00', 1)	# 13-13
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f64757374000000000000000000000000000c000000')
    sprite('vref_rwi355_00', 1)	# 14-14
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f64757374000000000000000000000000000d000000')
    sprite('vref_rwi355_00', 1)	# 15-15
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f64757374000000000000000000000000000e000000')
    sprite('vref_rwi355_00', 1)	# 16-16
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f64757374000000000000000000000000000f000000')
    sprite('vref_rwi355_00', 1)	# 17-17
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736c6173685f647573740000000000000000000000000010000000')

@State
def rwief355_SnowFall():

    def upon_IMMEDIATE():
        Unknown4061(1)
        teleportRelativeY(0)
        Unknown2055(35)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
        Unknown4047(48, 48, 48)
        Unknown4045('72776965663335355f736e6f7766616c6c000000000000000000000000000000ffffffff')
    label(0)
    sprite('null', 5)	# 1-5
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663335355f736e6f7766616c6c5f6c6f6f7000000000000000000000ffffffff')
    gotoLabel(0)

@State
def AstralAtkSecond():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(4)
        Damage(1000)
        AirPushbackX(2500)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(500)
        Unknown11064(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(120)
        Unknown11091(100)
        Unknown9021(1)
        Unknown11067(1)
        Unknown1086(22)
        Unknown1056(2000)
        Unknown1064(2000)
        Unknown11069('AstralAtkShotRush')
    sprite('rwi450_AstAtk', 3)	# 1-3	 **attackbox here**

@State
def AstralAtkShotRush():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(4)
        Damage(1750)
        AirPushbackX(500)
        AirPushbackY(5000)
        Unknown11064(1)
        Hitstop(6)
        Unknown11091(100)
        Unknown9021(1)
        Unknown9266(9)
        Unknown11067(1)
        Unknown1086(22)
        Unknown1007(200000)
        Unknown1056(2000)
        Unknown1064(2000)

        def upon_78():
            Unknown23029(3, 4502, 0)

        def upon_43():
            if (SLOT_48 == 4503):
                clearUponHandler(43)
                clearUponHandler(78)
                Unknown11001(300, 300, 300)
    sprite('rwi450_AstAtk', 3)	# 1-3	 **attackbox here**

@State
def AstralFirstCamera():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2053(0)
        Unknown1086(3)
        SLOT_51 = SLOT_163
        op(3, 2, 51, 0, 2)
        if SLOT_38:
            op(2, 2, 0, 0, -1)
        SLOT_83 = (SLOT_83 + SLOT_0)

        def upon_43():
            if (SLOT_48 == 4504):
                clearUponHandler(43)
                sendToLabel(1)
    label(0)
    sprite('null', 300)	# 1-300
    Unknown20000(1)
    Unknown20003(1)
    label(1)
    sprite('null', 1)	# 301-301
    Unknown20000(0)
    Unknown20003(0)

@State
def AstralLastCamera():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2053(0)

        def upon_3():
            Unknown1086(3)
            if SLOT_2:
                SLOT_51 = SLOT_163
                op(3, 2, 51, 0, 2)
                if SLOT_38:
                    op(2, 2, 0, 0, -1)
                SLOT_83 = (SLOT_83 + SLOT_0)
    sprite('null', 10)	# 1-10
    Unknown2037(1)
    Unknown20000(1)
    Unknown20003(1)
    sprite('null', 185)	# 11-195
    clearUponHandler(3)
    sprite('null', 1)	# 196-196
    Unknown23029(3, 4505, 0)
    Unknown20000(0)
    Unknown20003(0)

@State
def AstralAtkFinal():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown2034(0)
        Unknown2053(0)
        AttackLevel_(5)
        Damage(11700)
        Unknown11064(3)
        Unknown11023(1)
        Unknown11067(1)
        Hitstop(0)
        AirPushbackX(50000)
        AirPushbackY(80000)
        Unknown11091(100)
        Unknown9021(1)
        Unknown9266(9)
        Unknown1086(22)
        Unknown1056(2000)
        Unknown1064(2000)
    sprite('null', 95)	# 1-95
    GFX_0('rwief450_Flare', -1)
    sprite('null', 4)	# 96-99
    GFX_0('rwief450_Finish', -1)
    sprite('rwi450_AstAtk', 3)	# 100-102	 **attackbox here**

@State
def rwief450_1st():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4009(3)
        Unknown2054(1)
        Unknown1056(650)
        Unknown1064(1400)
        Unknown1088(1000)
        Unknown1072(-90000)
        teleportRelativeX(500000)
        Unknown23015(11)
        sendToLabelUpon(32, 0)

        def upon_41():
            Unknown26('RWBY_AHground')
    sprite('null', 30)	# 1-30
    Unknown4003('72776965665f676c7970685f73746172743330660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4045('72776965663435305f676c797068000000000000000000000000000000000000ffffffff')
    SFX_3('rwise_43')
    sprite('null', 50)	# 31-80
    Unknown4003('72776965665f676c7970685f6c6f6f70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('RWBY_AHground', -1)
    gotoLabel(9)
    label(0)
    sprite('null', 60)	# 81-140
    label(9)
    sprite('null', 6)	# 141-146
    Unknown1059(-108)
    Unknown1067(-233)
    Unknown1091(-166)

@State
def RWBY_AHground():

    def upon_IMMEDIATE():
        Unknown4003('525742595f414867726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3026(-16777216)
        Unknown1000(0)
        teleportRelativeY(-1000)
        Unknown1056(2000)
        Unknown4022(3)
        Unknown3032()
        Unknown23015(2)
        sendToLabelUpon(32, 0)
    sprite('null', 100)	# 1-100
    sprite('null', 32767)	# 101-32867
    GFX_0('RWBY_AHground_Mask', -1)
    label(0)
    sprite('null', 20)	# 32868-32887

@State
def RWBY_AHground_Mask():

    def upon_IMMEDIATE():
        Unknown4003('525742595f414867726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3026(-16777216)
        Unknown1088(500)
        Unknown1056(2000)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown23015(12)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 20)	# 32768-32787

@State
def rwief450_Glyph_Hit():

    def upon_IMMEDIATE():
        Unknown4061(1)
        teleportRelativeX(500000)
    sprite('null', 1)	# 1-1
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f676c7970685f6869740000000000000000000000000000ffffffff')

@State
def rwief450_2nd():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('vref_rwi450_dust', 4)	# 1-4
    Unknown4048(20000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000000000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000000000000')
    sprite('keep', 2)	# 5-6
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000001000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000001000000')
    GFX_0('rwief450_GlyphSmall01', -1)
    sprite('keep', 2)	# 7-8
    Unknown4048(-20000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000002000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000002000000')
    GFX_0('rwief450_GlyphSmall02', -1)
    sprite('keep', 1)	# 9-9
    Unknown4048(-70000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000003000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000003000000')
    sprite('keep', 1)	# 10-10
    Unknown4048(-110000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000004000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000004000000')
    GFX_0('rwief450_GlyphSmall03', -1)
    sprite('keep', 2)	# 11-12
    Unknown4048(-135000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000005000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000005000000')
    sprite('keep', 2)	# 13-14
    Unknown4048(-170000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000006000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000006000000')
    GFX_0('rwief450_GlyphSmall04', -1)
    sprite('keep', 2)	# 15-16
    Unknown4048(-190000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000007000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000007000000')
    GFX_0('rwief450_GlyphSmall05', -1)
    sprite('keep', 2)	# 17-18
    Unknown4048(-230000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000008000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000008000000')
    GFX_0('rwief450_GlyphSmall06', -1)
    sprite('keep', 30)	# 19-48
    Unknown4048(-260000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f647573740000000000000000000000000009000000')
    Unknown4045('72776965663435305f73776f72645f647573744200000000000000000000000009000000')
    Unknown4048(-280000)
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663435305f73776f72645f64757374000000000000000000000000000a000000')
    Unknown4045('72776965663435305f73776f72645f64757374420000000000000000000000000a000000')
    sprite('null', 10)	# 49-58
    GFX_0('rwief450_LazerSignal', -1)
    sprite('null', 110)	# 59-168
    GFX_0('rwief450_HoldGlyph', -1)
    sprite('null', 40)	# 169-208
    GFX_0('rwief450_GlyphEndSignal', -1)

@Subroutine
def rwief450_GlyphSmall_Func():
    callSubroutine('MagicImage_Func')
    Unknown4009(3)
    Unknown2054(1)
    Unknown4003('72776965663435305f676c79706830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(0)
    Unknown1059(40)
    Unknown1067(100)
    Unknown1091(200)
    Unknown1072(-20000)
    teleportRelativeX(-30000)
    Unknown1007(-40000)
    sendToLabelUpon(33, 0)
    Unknown4047(48, 48, 48)
    Unknown4048(-20000)
    Unknown4045('72776965663435305f676c797068535f7a697a6f6b7500000000000000000000ffffffff')

    def upon_32():
        GFX_0('rwief450_Lazer', -1)
        GFX_0('rwief450_GlyphBurst', -1)

@Subroutine
def rwief450_GlyphSmall_End_Func():
    Unknown1059(-40)
    Unknown1067(-100)
    Unknown1091(-200)

@State
def rwief450_GlyphEndSignal():

    def upon_IMMEDIATE():
        pass
    sprite('null', 2)	# 1-2
    Unknown21012('72776965663435305f476c797068536d616c6c3031000000000000000000000021000000')
    sprite('null', 2)	# 3-4
    Unknown21012('72776965663435305f476c797068536d616c6c3034000000000000000000000021000000')
    sprite('null', 2)	# 5-6
    Unknown21012('72776965663435305f476c797068536d616c6c3036000000000000000000000021000000')
    sprite('null', 2)	# 7-8
    Unknown21012('72776965663435305f476c797068536d616c6c3035000000000000000000000021000000')
    sprite('null', 2)	# 9-10
    Unknown21012('72776965663435305f476c797068536d616c6c3033000000000000000000000021000000')
    sprite('null', 2)	# 11-12
    Unknown21012('72776965663435305f476c797068536d616c6c3032000000000000000000000021000000')

@State
def rwief450_GlyphSmall01():

    def upon_IMMEDIATE():
        teleportRelativeX(195000)
        Unknown1007(210000)
        callSubroutine('rwief450_GlyphSmall_Func')
        Unknown23015(11)
        Unknown1101(90)
    sprite('null', 10)	# 1-10
    sprite('null', 32767)	# 11-32777
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 32778-32787
    callSubroutine('rwief450_GlyphSmall_End_Func')
    Unknown1101(90)

@State
def rwief450_GlyphSmall02():

    def upon_IMMEDIATE():
        teleportRelativeX(130000)
        Unknown1007(390000)
        callSubroutine('rwief450_GlyphSmall_Func')
        Unknown23015(11)
        Unknown1101(80)
    sprite('null', 10)	# 1-10
    sprite('null', 32767)	# 11-32777
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 32778-32787
    callSubroutine('rwief450_GlyphSmall_End_Func')
    Unknown1101(80)

@State
def rwief450_GlyphSmall03():

    def upon_IMMEDIATE():
        teleportRelativeX(-45000)
        Unknown1007(500000)
        callSubroutine('rwief450_GlyphSmall_Func')
        Unknown23015(6)
    sprite('null', 10)	# 1-10
    sprite('null', 32767)	# 11-32777
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 32778-32787
    callSubroutine('rwief450_GlyphSmall_End_Func')

@State
def rwief450_GlyphSmall04():

    def upon_IMMEDIATE():
        teleportRelativeX(-200000)
        Unknown1007(410000)
        callSubroutine('rwief450_GlyphSmall_Func')
        Unknown23015(6)
        Unknown1101(115)
    sprite('null', 10)	# 1-10
    sprite('null', 32767)	# 11-32777
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 32778-32787
    callSubroutine('rwief450_GlyphSmall_End_Func')
    Unknown1101(115)

@State
def rwief450_GlyphSmall05():

    def upon_IMMEDIATE():
        teleportRelativeX(-150000)
        Unknown1007(150000)
        callSubroutine('rwief450_GlyphSmall_Func')
        Unknown23015(6)
        Unknown1101(130)
    sprite('null', 10)	# 1-10
    sprite('null', 32767)	# 11-32777
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 32778-32787
    callSubroutine('rwief450_GlyphSmall_End_Func')
    Unknown1101(130)

@State
def rwief450_GlyphSmall06():

    def upon_IMMEDIATE():
        teleportRelativeX(80000)
        Unknown1007(50000)
        callSubroutine('rwief450_GlyphSmall_Func')
        Unknown23015(6)
        Unknown1101(110)
    sprite('null', 10)	# 1-10
    sprite('null', 32767)	# 11-32777
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 32778-32787
    callSubroutine('rwief450_GlyphSmall_End_Func')
    Unknown1101(110)

@State
def rwief450_LazerSignal():

    def upon_IMMEDIATE():
        pass
    sprite('null', 9)	# 1-9
    Unknown21012('72776965663435305f476c797068536d616c6c3031000000000000000000000020000000')
    sprite('null', 9)	# 10-18
    Unknown21012('72776965663435305f476c797068536d616c6c3033000000000000000000000020000000')
    sprite('null', 9)	# 19-27
    Unknown21012('72776965663435305f476c797068536d616c6c3036000000000000000000000020000000')
    sprite('null', 9)	# 28-36
    Unknown21012('72776965663435305f476c797068536d616c6c3034000000000000000000000020000000')
    sprite('null', 9)	# 37-45
    Unknown21012('72776965663435305f476c797068536d616c6c3032000000000000000000000020000000')
    sprite('null', 9)	# 46-54
    Unknown21012('72776965663435305f476c797068536d616c6c3035000000000000000000000020000000')
    sprite('null', 9)	# 55-63
    Unknown21012('72776965663435305f476c797068536d616c6c3031000000000000000000000020000000')
    sprite('null', 9)	# 64-72
    Unknown21012('72776965663435305f476c797068536d616c6c3035000000000000000000000020000000')
    sprite('null', 9)	# 73-81
    Unknown21012('72776965663435305f476c797068536d616c6c3036000000000000000000000020000000')
    sprite('null', 9)	# 82-90
    Unknown21012('72776965663435305f476c797068536d616c6c3033000000000000000000000020000000')
    sprite('null', 9)	# 91-99
    Unknown21012('72776965663435305f476c797068536d616c6c3032000000000000000000000020000000')
    sprite('null', 9)	# 100-108
    Unknown21012('72776965663435305f476c797068536d616c6c3034000000000000000000000020000000')

@State
def rwief450_Lazer():

    def upon_IMMEDIATE():
        physicsXImpulse(60000)
        Unknown1026(60000, -40000)

        def upon_3():
            YAccel(90)
            Unknown2071('1600000000000000000000000a00000001000000')
    sprite('null', 50)	# 1-50
    GFX_0('rwief450_Lazer01', -1)
    GFX_0('rwief450_Lazer02', -1)

@State
def rwief450_Lazer01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(1)
        Unknown21004(64)
        Unknown23048('01000000')
        Unknown23051('767265665f7277693435305f747261696c2e68697000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23050('3200000014000000')
        Unknown23049('ffffffffffffff00')
    sprite('null', 50)	# 1-50
    GFX_0('rwief450_LazerBullet', -1)

@State
def rwief450_Lazer02():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown23048('01000000')
        Unknown23051('767265665f7277693435305f747261696c2e68697000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23050('280000000a000000')
        Unknown23049('ffffffffffffff00')
    sprite('null', 50)	# 1-50

@State
def rwief450_LazerBullet():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown1096(300)
        Unknown4061(1)
        Unknown4047(63, 63, 63)
        Unknown23067('rwief450_lazer_bullet')

        def upon_3():
            YAccel(90)
            Unknown2071('0200000000000000000000006400000001000000')
    sprite('null', 50)	# 1-50
    GFX_0('rwief450_LazerBulletB', -1)

@State
def rwief450_LazerBulletB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown1096(400)
        Unknown4047(64, 64, 64)
        Unknown23067('rwief450_lazer_bulletB')
    sprite('null', 50)	# 1-50

@State
def rwief450_GlyphBurst():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
    sprite('null', 50)	# 1-50
    Unknown4047(48, 48, 48)
    Unknown23067('rwief450_glyph_burst')
    SFX_3('rwise_50')

@State
def rwief450_HoldGlyph():

    def upon_IMMEDIATE():
        Unknown4012(22)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 3)	# 1-3
    GFX_0('rwief450_HoldGlyph01', -1)
    sprite('null', 3)	# 4-6
    GFX_0('rwief450_HoldGlyph02', -1)
    sprite('null', 3)	# 7-9
    GFX_0('rwief450_HoldGlyph03', -1)
    sprite('null', 32767)	# 10-32776
    GFX_0('rwief450_HoldGlyph04', -1)

@Subroutine
def rwief450_HoldGlyph_Func():
    Unknown4003('72776965663435305f676c79706830322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    callSubroutine('MagicImage_Func')
    Unknown4007(2)
    Unknown1096(0)
    Unknown1099(333)
    Unknown1059(266)
    Unknown1091(83)
    Unknown23015(0)
    Unknown3001(180)
    Unknown21004(48)

@State
def rwief450_HoldGlyph01():

    def upon_IMMEDIATE():
        callSubroutine('rwief450_HoldGlyph_Func')
        Unknown1101(100)
        Unknown1072(-60000)
    sprite('null', 3)	# 1-3
    sprite('null', 3)	# 4-6
    Unknown1101(50)
    sprite('null', 6)	# 7-12
    Unknown1101(50)
    sprite('null', 32767)	# 13-32779
    Unknown1099(0)

@State
def rwief450_HoldGlyph02():

    def upon_IMMEDIATE():
        callSubroutine('rwief450_HoldGlyph_Func')
        Unknown1101(100)
        Unknown1072(-175000)
    sprite('null', 3)	# 1-3
    sprite('null', 3)	# 4-6
    Unknown1101(50)
    sprite('null', 6)	# 7-12
    Unknown1101(50)
    sprite('null', 32767)	# 13-32779
    Unknown1099(0)

@State
def rwief450_HoldGlyph03():

    def upon_IMMEDIATE():
        callSubroutine('rwief450_HoldGlyph_Func')
        Unknown1101(110)
        Unknown1072(-115000)
    sprite('null', 3)	# 1-3
    sprite('null', 3)	# 4-6
    Unknown1101(50)
    sprite('null', 6)	# 7-12
    Unknown1101(50)
    sprite('null', 32767)	# 13-32779
    Unknown1099(0)

@State
def rwief450_HoldGlyph04():

    def upon_IMMEDIATE():
        callSubroutine('rwief450_HoldGlyph_Func')
        Unknown1101(90)
        Unknown1072(-140000)
    sprite('null', 3)	# 1-3
    sprite('null', 3)	# 4-6
    Unknown1101(50)
    sprite('null', 6)	# 7-12
    Unknown1101(50)
    sprite('null', 32767)	# 13-32779
    Unknown1099(0)

@State
def rwief450_3rd():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    sprite('null', 60)	# 1-60
    GFX_0('rwief450_JumpGlyph', -1)
    sprite('null', 5)	# 61-65
    GFX_0('rwief450_SummonGlyph', -1)
    sprite('null', 32767)	# 66-32832
    GFX_0('rwief450_Sword', -1)
    GFX_0('rwief450_IcedGround', -1)
    label(0)
    sprite('null', 5)	# 32833-32837
    sprite('null', 30)	# 32838-32867
    GFX_0('rwief450_Snow', -1)
    sprite('null', 50)	# 32868-32917
    GFX_0('rwief450_WhiteOut', -1)

@State
def rwief450_JumpGlyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown1101(90)
        Unknown1072(-90000)
        Unknown1096(1100)
        Unknown1056(400)
        Unknown23015(11)
    sprite('null', 20)	# 1-20
    Unknown4003('72776965665f676c7970685f73746172743235662e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('rwise_43')
    sprite('null', 5)	# 21-25
    Unknown4047(48, 48, 48)
    Unknown4045('72776965663433305f676c797068000000000000000000000000000000000000ffffffff')
    sprite('null', 80)	# 26-105
    Unknown4003('72776965665f676c7970685f6c6f6f70322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief450_SummonGlyph():

    def upon_IMMEDIATE():
        callSubroutine('MagicImage_Func')
        Unknown4003('72776965663335355f676c7970682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1101(90)
        Unknown1072(140000)
        Unknown1056(1400)
        Unknown1064(1120)
        Unknown1088(280)
        teleportRelativeY(1900000)
        teleportRelativeX(-700000)
        Unknown1059(14)
        Unknown1067(11)
        Unknown1091(2)
    sprite('null', 25)	# 1-25
    sprite('null', 500)	# 26-525
    Unknown1099(0)

@State
def rwief450_Sword():

    def upon_IMMEDIATE():
        teleportRelativeY(1900000)
        teleportRelativeX(-700000)
        Unknown1072(45000)
        Unknown1096(4000)
        Unknown3032()
        Unknown2054(1)
        Unknown23015(14)
        Unknown4061(1)
        Unknown23122(10)
        Unknown2005()
    sprite('null', 70)	# 1-70
    GFX_0('rwief450_SwordUV', -1)
    GFX_0('rwief450_Sword_Bloom', -1)
    Unknown4003('72776965663435305f73776f726430312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('rwise_52')
    sprite('null', 5)	# 71-75
    Unknown4003('72776965663435305f73776f726430322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsXImpulse(-122000)
    physicsYImpulse(-110000)
    sprite('null', 7)	# 76-82
    GFX_0('rwief450_Issen', -1)
    sprite('null', 5)	# 83-87
    Unknown1019(10)
    YAccel(10)
    sprite('null', 5)	# 88-92
    Unknown1019(10)
    YAccel(10)
    sprite('null', 200)	# 93-292
    SFX_3('rwise_54')
    Unknown1019(0)
    YAccel(0)

@State
def rwief450_SwordUV():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4006(2)
        Unknown4007(2)
        Unknown3032()
        Unknown2054(1)
        Unknown23015(13)
    sprite('null', 70)	# 1-70
    Unknown4003('72776965663435305f73776f726455562e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rwief450_Sword_Bloom():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4006(2)
        Unknown4007(2)
        Unknown3033()
        Unknown2054(1)
        Unknown23015(13)
        Unknown4061(1)
        Unknown21004(80)
        Unknown3003(50)
    sprite('null', 70)	# 1-70
    Unknown4003('72776965663435305f73776f72645f626c6f6f6d30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 9)	# 71-79
    Unknown4003('72776965663435305f73776f72645f626c6f6f6d30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 210)	# 80-289

@State
def rwief450_Flare():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4012(22)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 5)	# 1-5
    sprite('null', 1)	# 6-6
    Unknown4012(22)
    Unknown4047(64, 64, 64)
    Unknown4045('72776965663435305f666c617265000000000000000000000000000000000000ffffffff')

@State
def rwief450_Issen():

    def upon_IMMEDIATE():
        Unknown1072(45000)
        Unknown1056(333)
        Unknown3001(64)
        physicsXImpulse(-125000)
        physicsYImpulse(-110000)
        Unknown2055(90)
    sprite('null', 1)	# 1-1
    Unknown4048(45000)
    Unknown4045('72776965663435305f7370656564000000000000000000000000000000000000ffffffff')
    GFX_0('rwief450_IssenA', -1)
    GFX_0('rwief450_IssenB', -1)
    sprite('null', 2)	# 2-3
    Unknown1059(333)
    sprite('null', 3)	# 4-6
    Unknown3004(0)
    Unknown1059(0)
    Unknown1056(1000)
    sprite('null', 2)	# 7-8
    Unknown1084(1)
    Unknown1059(-300)
    sprite('null', 2)	# 9-10
    Unknown1059(-100)
    sprite('null', 2)	# 11-12
    Unknown1059(-50)
    sprite('null', 2)	# 13-14
    Unknown1059(-30)
    sprite('null', 2)	# 15-16
    Unknown1059(-5)
    label(0)
    sprite('null', 1)	# 17-17
    Unknown1059(-1)
    sprite('null', 1)	# 18-18
    Unknown1059(0)
    gotoLabel(0)

@State
def rwief450_IssenA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown4061(4)
    sprite('null', 40)	# 1-40
    Unknown4047(64, 64, 64)
    Unknown23067('rwief450_flashA')
    sprite('null', 2)	# 41-42
    Unknown3001(64)
    sprite('null', 4)	# 43-46
    Unknown3001(192)
    sprite('null', 2)	# 47-48
    Unknown3001(64)
    sprite('null', 16)	# 49-64
    Unknown3001(192)
    sprite('null', 2)	# 65-66
    Unknown3001(32)
    sprite('null', 10)	# 67-76
    Unknown3001(192)
    sprite('null', 2)	# 77-78
    Unknown3001(16)
    sprite('null', 2)	# 79-80
    Unknown3001(192)
    sprite('null', 2)	# 81-82
    Unknown3001(16)
    sprite('null', 4)	# 83-86
    Unknown3001(192)

@State
def rwief450_IssenB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown4061(4)
    sprite('null', 40)	# 1-40
    GFX_2('rwief450_flashB')
    sprite('null', 2)	# 41-42
    Unknown3001(64)
    sprite('null', 4)	# 43-46
    Unknown3001(192)
    sprite('null', 2)	# 47-48
    Unknown3001(64)
    sprite('null', 16)	# 49-64
    Unknown3001(192)
    sprite('null', 2)	# 65-66
    Unknown3001(32)
    sprite('null', 10)	# 67-76
    Unknown3001(192)
    sprite('null', 2)	# 77-78
    Unknown3001(16)
    sprite('null', 2)	# 79-80
    Unknown3001(192)
    sprite('null', 2)	# 81-82
    Unknown3001(16)
    sprite('null', 4)	# 83-86
    Unknown3001(192)

@State
def rwief450_Finish():

    def upon_IMMEDIATE():
        callSubroutine('rwief430_Bake_Func')
        Unknown4007(22)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(2000)
        Unknown1064(1000)
        physicsXImpulse(70000)
        physicsYImpulse(-70000)
        Unknown1072(45000)
        Unknown1000(190000)
        teleportRelativeY(0)
    sprite('vref_rwi430_00A', 1)	# 1-1
    GFX_0('rwief450_Flash', -1)
    SFX_3('rwise_48')
    sprite('vref_rwi430_00A', 3)	# 2-4
    Unknown4007(0)
    sprite('vref_rwi430_01', 1)	# 5-5
    GFX_0('rwief430_01_Model', -1)
    GFX_0('rwief430_DashRing01', 0)
    GFX_0('rwief430_DashRing02', 1)
    GFX_0('rwief430_01_dust', -1)
    Unknown1064(1200)
    sprite('vref_rwi430_01', 1)	# 6-6
    Unknown1064(1400)
    sprite('vref_rwi430_01', 2)	# 7-8
    Unknown1064(1200)
    Unknown1067(-40)
    sprite('vref_rwi430_02', 4)	# 9-12
    physicsXImpulse(10000)
    physicsYImpulse(-10000)
    sprite('vref_rwi430_03', 4)	# 13-16
    sprite('vref_rwi430_04', 4)	# 17-20
    sprite('vref_rwi430_05', 4)	# 21-24
    sprite('vref_rwi430_06', 4)	# 25-28

@State
def rwief450_Flash():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4006(2)
        Unknown4007(2)
        Unknown1096(1500)
    sprite('null', 40)	# 1-40
    Unknown4047(48, 32, 64)
    Unknown23067('rwief450_flashC')
    GFX_0('rwief450_Speed', -1)

@State
def rwief450_Speed():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4006(2)
        Unknown4007(2)
        Unknown1096(1500)
    sprite('null', 40)	# 1-40
    Unknown4047(48, 40, 32)
    Unknown23067('rwief430_speed')

@State
def rwief450_IcedGround():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown3032()
        Unknown23015(11)
        Unknown4003('72776965665f6963656467726f756e64000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(2500)
        Unknown1088(1200)
        Unknown1000(1320000)
        teleportRelativeY(0)
        Unknown4061(1)
        Unknown3001(180)
        Unknown21004(60)
    sprite('null', 260)	# 1-260
    Unknown4047(40, 40, 40)
    Unknown4054(11)
    Unknown23067('rwief450_ground')

@State
def rwief450_Snow():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4022(3)
        Unknown1000(-300000)
        teleportRelativeY(0)
    sprite('null', 160)	# 1-160
    Unknown4047(48, 40, 32)
    Unknown23067('rwief450_snow')

@State
def rwief450_WhiteOut():

    def upon_IMMEDIATE():
        Unknown4003('72776965663435305f776869746530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown23015(1)
        Unknown3033()
        Unknown4061(1)
        Unknown21004(32)
        Unknown3001(0)
        Unknown1096(4000)
        Unknown6001(1)

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)
    sprite('null', 40)	# 1-40
    sprite('null', 20)	# 41-60
    Unknown3004(2)
    sprite('null', 10)	# 61-70
    Unknown3004(4)
    sprite('null', 10)	# 71-80
    Unknown3004(8)
    sprite('null', 10)	# 81-90
    Unknown3004(16)
    Unknown23102(2)
    Unknown23108(2)
    Unknown23114(2)
    sprite('null', 10)	# 91-100
    Unknown23102(4)
    Unknown23108(4)
    Unknown23114(4)
    sprite('null', 40)	# 101-140
    Unknown23102(8)
    Unknown23108(8)
    Unknown23114(8)
    sprite('null', 40)	# 141-180
    Unknown26('RWBY_AHground')
    Unknown26('RWBY_AHground_Mask')

@State
def rwief450_SnowFall():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767
    Unknown4047(48, 48, 48)
    Unknown23067('rwief450_snowfall')

@State
def rwief600():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
    sprite('vref_rwi600_00', 6)	# 1-6
    sprite('null', 11)	# 7-17
    GFX_0('rwief600_slash_Model', -1)
    GFX_0('rwief600_slash_Bloom', -1)
    GFX_0('rwief600_EX_Dummy', -1)

@State
def rwief600_slash_Model():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
        Unknown4003('72776965663630305f736c61736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23122(64)
        Unknown1096(3700)
        teleportRelativeX(-3000)
        Unknown1007(260000)
    sprite('null', 11)	# 1-11

@State
def rwief600_slash_Bloom():

    def upon_IMMEDIATE():
        callSubroutine('rwief_slash_func')
    sprite('vref_rwi600_01b', 7)	# 1-7
    Unknown3004(-31)

@State
def rwief600_EX_Dummy():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3038(1)
    sprite('vref_rwi600_01b', 1)	# 1-1
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31360000000000000000000000000000000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32340000000000000000000000000001000000')
    sprite('vref_rwi600_01b', 1)	# 2-2
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32300000000000000000000000000002000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000003000000')
    sprite('vref_rwi600_01b', 1)	# 3-3
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000004000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f32360000000000000000000000000006000000')
    sprite('vref_rwi600_01b', 25)	# 4-28
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f38000000000000000000000000000005000000')
    Unknown4047(24, 24, 24)
    Unknown4047(24, 24, 24)
    Unknown4045('72776965665f736c6173685f647573745f31320000000000000000000000000006000000')

@State
def rwief601():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown23022(1)
        sendToLabelUpon(32, 1)
        Unknown4061(1)
    label(0)
    sprite('rwi601_00', 24)	# 1-24
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    gotoLabel(0)
    label(1)
    sprite('rwi601_01', 6)	# 25-30
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_02', 6)	# 31-36
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_03', 4)	# 37-40
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_04', 2)	# 41-42
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_04', 3)	# 43-45
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000004000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000005000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000006000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000007000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000008000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000009000000')
    sprite('rwi601_04', 3)	# 46-48
    Unknown4047(32, 32, 32)
    Unknown4045('72776965663630310000000000000000000000000000000000000000000000000a000000')
    Unknown4047(32, 32, 32)
    Unknown4045('72776965663630310000000000000000000000000000000000000000000000000b000000')
    Unknown4047(32, 32, 32)
    Unknown4045('72776965663630310000000000000000000000000000000000000000000000000c000000')
    Unknown4047(32, 32, 32)
    Unknown4045('72776965663630310000000000000000000000000000000000000000000000000d000000')
    Unknown4047(32, 32, 32)
    Unknown4045('72776965663630310000000000000000000000000000000000000000000000000e000000')
    Unknown4047(32, 32, 32)
    Unknown4045('72776965663630310000000000000000000000000000000000000000000000000f000000')
    sprite('rwi601_05', 6)	# 49-54
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000004000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000005000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000006000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000007000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000008000000')
    sprite('rwi601_06', 6)	# 55-60
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_07', 6)	# 61-66
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_06', 6)	# 67-72
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000000000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000001000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000002000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000003000000')
    sprite('rwi601_05', 6)	# 73-78
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000006000000')
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000008000000')
    sprite('rwi601_05', 6)	# 79-84
    Unknown4047(32, 32, 32)
    Unknown4045('727769656636303100000000000000000000000000000000000000000000000005000000')