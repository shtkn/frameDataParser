@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f52472e4449470000000000000000000000000000000000000065665f656d625f52475f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
    sprite('null', 10)	# 1-10
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)	# 11-20
    Unknown3025(-8342273, 10)
    sprite('null', 10)	# 21-30
    Unknown3025(-1, 10)
    sprite('null', 10)	# 31-40
    Unknown3025(-8342273, 10)
    sprite('null', 80)	# 41-120

@State
def EMB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f52472e4449470000000000000000000000000000000000000065665f656d625f52475f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
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
def EMB_RG_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('65665f656d625f52472e4449470000000000000000000000000000000000000065665f656d625f52475f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
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
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('726765665f6d632e444947000000000000000000000000000000000000000000726765665f6d635f6d6f74696f6e5f3030302e6d6d6f74000000000000000000')
        Unknown4015()
        Unknown21004(224)
        Unknown2054(1)
    sprite('null', 74)	# 1-74

@State
def DIST_RG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(5000)
        Unknown1079()
        Unknown3001(255)
        Unknown3057(1)
        Unknown3058(16000)
        Unknown3059(-40)
        Unknown1099(50)
        Unknown3004(-4)
    sprite('vrdist00', 3)	# 1-3
    Unknown1010(-10000, 10000)
    Unknown1011(-10000, 10000)
    Unknown1102(-500, 500)
    sprite('vrdist00', 3)	# 4-6
    Unknown1010(-10000, 10000)
    Unknown1011(-10000, 10000)
    Unknown1102(-500, 500)
    sprite('vrdist00', 3)	# 7-9
    Unknown1010(-10000, 10000)
    Unknown1011(-10000, 10000)
    Unknown1102(-500, 500)
    sprite('vrdist00', 3)	# 10-12
    Unknown1010(-10000, 10000)
    Unknown1011(-10000, 10000)
    Unknown1102(-500, 500)
    sprite('vrdist00', 3)	# 13-15
    Unknown1010(-10000, 10000)
    Unknown1011(-10000, 10000)
    Unknown1102(-500, 500)
    sprite('vrdist00', 3)	# 16-18
    Unknown1010(-10000, 10000)
    Unknown1011(-10000, 10000)
    Unknown1102(-500, 500)

@State
def rgef_drains():
    sprite('null', 1)	# 1-1
    Unknown3038(1)
    Unknown4047(224, 224, 224)
    Unknown4045('726765665f647261696e61000000000000000000000000000000000000000000ffffffff')

@State
def rgef_drain():
    sprite('null', 1)	# 1-1
    Unknown3038(1)
    Unknown4047(224, 224, 224)
    Unknown4045('726765665f647261696e62000000000000000000000000000000000000000000ffffffff')

@State
def ThrowMazzle():
    sprite('null', 120)	# 1-120
    GFX_1('rgef_muzzle00', -1)
    GFX_1('rgef_muzzle00', -1)

@State
def rgef431_Start():
    sprite('null', 120)	# 1-120
    Unknown4046(-16777216, -16777216, 16711680)
    Unknown4045('726765665f626c6f6f646b696e65520000000000000000000000000000000000ffffffff')
    Unknown4046(-16777216, -16777216, 16711680)
    Unknown4045('726765665f626c6f6f646b696e654c0000000000000000000000000000000000ffffffff')
    Unknown4046(-65536, -65536, 16711680)
    Unknown4045('726765665f626c6f6f646b696e65523200000000000000000000000000000000ffffffff')
    Unknown4046(-65536, -65536, 16711680)
    Unknown4045('726765665f626c6f6f646b696e654c3200000000000000000000000000000000ffffffff')
    Unknown4045('726765665f626b62757273740000000000000000000000000000000000000000ffffffff')
    Unknown4054(2)
    Unknown4046(-65536, -65536, 16711680)
    Unknown4045('726765665f626c6f6f646b696e656261636b0000000000000000000000000000ffffffff')

@State
def rgef203atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(500)
        Unknown1096(900)
        teleportRelativeX(50000)
        Unknown3001(212)
    sprite('vrrgef203atk_00', 2)	# 1-2
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('vrrgef203atk_01', 3)	# 3-5
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef203atk_02', 5)	# 6-10
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_03', 4)	# 11-14
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_04', 1)	# 15-15
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    Unknown2019(-500)
    sprite('vrrgef203atk_05', 2)	# 16-17
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_06', 3)	# 18-20
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef203atk_07', 4)	# 21-24
    Unknown3001(212)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_08', 4)	# 25-28
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_09', 3)	# 29-31
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    sprite('vrrgef203atk_10', 3)	# 32-34
    GFX_1('rgef02', 0)

@State
def rgef203atkD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1096(1100)
        Unknown3001(212)
    sprite('vrrgef203atk_00', 2)	# 1-2
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('vrrgef203atk_01', 3)	# 3-5
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef203atk_02', 5)	# 6-10
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_03', 4)	# 11-14
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_04', 1)	# 15-15
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    Unknown2019(-500)
    sprite('vrrgef203atk_05', 2)	# 16-17
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_06', 3)	# 18-20
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef203atk_07', 4)	# 21-24
    Unknown3001(212)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_08', 4)	# 25-28
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_09', 3)	# 29-31
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    sprite('vrrgef203atk_10', 3)	# 32-34
    GFX_1('rgef02', 0)

@State
def rgef213atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3001(255)
    sprite('vrrgef213atk_00', 2)	# 1-2
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    sprite('vrrgef213atk_01', 2)	# 3-4	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    sprite('vrrgef213atk_02', 3)	# 5-7
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef213atk_03', 4)	# 8-11
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    sprite('vrrgef213atk_04', 4)	# 12-15
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef213atk_05', 2)	# 16-17
    GFX_1('rgef03', 0)
    Unknown3004(-10)

@State
def rgef213atkD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1096(1200)
        Unknown3001(212)
    sprite('vrrgef213atk_00', 2)	# 1-2
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    sprite('vrrgef213atk_01', 2)	# 3-4	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    sprite('vrrgef213atk_02', 3)	# 5-7
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    sprite('vrrgef213atk_03', 4)	# 8-11
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    sprite('vrrgef213atk_04', 4)	# 12-15
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drain', 0)
    sprite('vrrgef213atk_05', 2)	# 16-17
    GFX_1('rgef03', 0)
    Unknown3004(-10)

@State
def rgef233atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown2019(-100)
        Unknown3001(212)
    sprite('vrrgef233atk_00', 3)	# 1-3
    GFX_1('rgef03', 0)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef233atk_01', 3)	# 4-6
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef233atk_02', 2)	# 7-8
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef233atk_03', 2)	# 9-10
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef233atk_04', 2)	# 11-12
    Unknown4007(0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef233atk_05', 5)	# 13-17
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_1('rgef03', 5)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_0('rgef_drains', 5)
    sprite('vrrgef233atk_06', 3)	# 18-20
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    sprite('vrrgef233atk_07', 3)	# 21-23
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef233atk_08', 3)	# 24-26
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef233atk_09', 3)	# 27-29
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown3004(-10)

@State
def rgef233atkD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown2019(-100)
        Unknown3001(212)
        Unknown1096(1200)
    sprite('vrrgef233atk_00', 3)	# 1-3
    GFX_1('rgef03', 0)
    GFX_0('rgef_drain', 0)
    Unknown1007(-100000)
    sprite('vrrgef233atk_01', 3)	# 4-6
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef233atk_02', 2)	# 7-8
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef233atk_03', 2)	# 9-10
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef233atk_04', 2)	# 11-12
    Unknown4007(0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef233atk_05', 5)	# 13-17
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_1('rgef03', 5)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_0('rgef_drain', 5)
    Unknown1007(100000)
    sprite('vrrgef233atk_06', 3)	# 18-20
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 4)
    sprite('vrrgef233atk_07', 3)	# 21-23
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef233atk_08', 3)	# 24-26
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef233atk_09', 3)	# 27-29
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown3004(-10)

@State
def rgef253atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3001(212)
    sprite('vrrgef253atk_00', 3)	# 1-3
    sprite('vrrgef253atk_01', 3)	# 4-6
    sprite('vrrgef253atk_02', 2)	# 7-8
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef253atk_03', 2)	# 9-10
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 3)
    sprite('vrrgef253atk_04', 2)	# 11-12
    Unknown3004(-10)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    sprite('vrrgef253atk_05', 2)	# 13-14
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)

@State
def rgef253atkD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3001(212)
    sprite('vrrgef253atk_00', 3)	# 1-3
    sprite('vrrgef253atk_01', 3)	# 4-6
    sprite('vrrgef253atk_02ex01', 2)	# 7-8
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 4)
    sprite('vrrgef253atk_03ex01', 2)	# 9-10
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 3)
    sprite('vrrgef253atk_04', 2)	# 11-12
    Unknown3004(-10)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    sprite('vrrgef253atk_05', 2)	# 13-14
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)

@State
def rgef400loop():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3029(1)
        Unknown3069(4)
        Unknown3070(1)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(900)
        Unknown3001(255)
        Unknown1064(1100)
        Unknown1007(-60000)
    sprite('vrrgef400atk_02', 3)	# 1-3	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    sprite('vrrgef400atk_03', 2)	# 4-5	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    label(0)
    sprite('vrrgef400atk_04', 2)	# 6-7	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown1096(1000)
    Unknown3004(-10)
    Unknown1007(-5000)
    sprite('vrrgef400atk_04', 2)	# 8-9	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown1096(1100)
    Unknown1007(5000)
    sprite('vrrgef400atk_04', 2)	# 10-11	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown1096(1200)
    Unknown1007(-10000)
    sprite('vrrgef400atk_04', 2)	# 12-13	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown1096(1100)
    Unknown1007(-5000)
    Unknown3004(10)
    sprite('vrrgef400atk_04', 2)	# 14-15	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown1096(1200)
    Unknown1007(2000)
    sprite('vrrgef400atk_04', 2)	# 16-17	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown1096(1100)
    Unknown1007(-3000)
    loopRest()
    gotoLabel(0)
    sprite('null', 20)	# 18-37

@State
def rgef400end():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3029(1)
        Unknown3069(4)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3001(255)
        Unknown1064(1100)
        Unknown1007(-70000)
        teleportRelativeX(120000)
    sprite('vrrgef400atk_05', 2)	# 1-2	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown3004(-10)
    sprite('vrrgef400atk_06', 4)	# 3-6	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    Unknown4007(0)
    sprite('vrrgef400atk_07', 4)	# 7-10	 **attackbox here**
    GFX_1('rgef00', 0)
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    sprite('vrrgef400atk_08', 4)	# 11-14	 **attackbox here**
    sprite('null', 20)	# 15-34

@State
def rgef400nokori():

    def upon_IMMEDIATE():
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3001(255)
    sprite('vrrgef400b_00', 5)	# 1-5	 **attackbox here**
    Unknown3004(-2)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    sprite('vrrgef400b_01', 2)	# 6-7	 **attackbox here**
    sprite('vrrgef400b_02', 3)	# 8-10	 **attackbox here**
    sprite('vrrgef400b_03', 3)	# 11-13	 **attackbox here**
    sprite('vrrgef400b_04', 3)	# 14-16	 **attackbox here**
    sprite('vrrgef400b_05', 3)	# 17-19	 **attackbox here**
    sprite('vrrgef400b_06', 3)	# 20-22	 **attackbox here**
    sprite('vrrgef400b_07', 3)	# 23-25	 **attackbox here**
    sprite('vrrgef400b_08', 3)	# 26-28	 **attackbox here**
    sprite('vrrgef400b_09', 3)	# 29-31	 **attackbox here**
    sprite('null', 9)	# 32-40
    Unknown3004(-6)

@State
def rgef401atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(-500)
        Unknown3032()
        Unknown3001(224)
    sprite('vrrgef401atk_00', 3)	# 1-3
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef401atk_01', 1)	# 4-4
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_0('rgef_drains', 5)
    GFX_0('rgef_drains', 6)
    sprite('vrrgef401atk_02', 1)	# 5-5
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef401atk_03', 1)	# 6-6
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 5)
    GFX_0('rgef_drains', 6)
    GFX_0('rgef_drains', 7)
    GFX_0('rgef_drains', 8)
    sprite('vrrgef401atk_04', 3)	# 7-9
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef401atk_05', 4)	# 10-13
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef401atk_06', 4)	# 14-17
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef401atk_07', 3)	# 18-20
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef401atk_08', 3)	# 21-23
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)

@State
def rgef402atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(-500)
        Unknown3001(240)
    sprite('vrrgef402atk_00', 1)	# 1-1
    sprite('vrrgef402atk_01', 1)	# 2-2
    sprite('vrrgef402atk_02', 1)	# 3-3
    sprite('vrrgef402atk_03', 3)	# 4-6
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef402atk_04', 3)	# 7-9
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef402atk_05', 3)	# 10-12
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef402atk_06', 3)	# 13-15
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef402atk_07', 3)	# 16-18
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef402atk_08', 3)	# 19-21
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)

@State
def rgef406atk():

    def upon_IMMEDIATE():
        Unknown3001(255)
        Unknown3004(-20)
    sprite('vrrgef406atk_00', 3)	# 1-3	 **attackbox here**
    GFX_1('rgef02', 1)
    sprite('vrrgef406atk_01', 3)	# 4-6	 **attackbox here**
    GFX_1('rgef02', 2)
    sprite('vrrgef406atk_02', 3)	# 7-9	 **attackbox here**
    GFX_1('rgef02', 1)
    sprite('vrrgef406atk_03', 3)	# 10-12	 **attackbox here**
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef406atk_00', 3)	# 13-15	 **attackbox here**
    GFX_1('rgef02', 1)
    sprite('vrrgef406atk_01', 3)	# 16-18	 **attackbox here**
    GFX_1('rgef02', 2)
    sprite('vrrgef406atk_02', 3)	# 19-21	 **attackbox here**
    sprite('vrrgef406atk_03', 3)	# 22-24	 **attackbox here**

@State
def rgef406batk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(-500)
        Unknown1007(300000)
        teleportRelativeX(120000)
        Unknown3032()
        Unknown3001(224)
    sprite('vrrgef406batk_00', 4)	# 1-4
    GFX_1('rgef03', 0)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef406batk_01', 4)	# 5-8
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef406batk_02', 3)	# 9-11
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_1('rgef03', 5)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_0('rgef_drains', 5)
    sprite('vrrgef406batk_03', 3)	# 12-14
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef406batk_04', 3)	# 15-17
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    sprite('vrrgef406batk_05', 3)	# 18-20
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown3004(-20)

@State
def rgef406batkD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1007(300000)
        teleportRelativeX(120000)
        Unknown3032()
        Unknown3001(224)
    sprite('vrrgef406batk_00', 4)	# 1-4
    GFX_1('rgef03', 0)
    GFX_0('rgef_drain', 0)
    sprite('vrrgef406batk_01', 4)	# 5-8
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef406batk_02', 3)	# 9-11
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_0('rgef_drain', 5)
    sprite('vrrgef406batk_03', 3)	# 12-14
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    sprite('vrrgef406batk_04', 3)	# 15-17
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    sprite('vrrgef406batk_05', 3)	# 18-20
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 0)
    Unknown3004(-20)

@State
def rgef408nokori():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(-500)
        Unknown3069(2)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        teleportRelativeX(-128000)
        Unknown3001(255)
    sprite('vrrgef408b_00', 2)	# 1-2
    Unknown3004(-5)
    sprite('vrrgef408b_01', 2)	# 3-4
    sprite('vrrgef408b_02', 2)	# 5-6
    sprite('vrrgef408b_03', 2)	# 7-8
    sprite('vrrgef408b_04', 2)	# 9-10
    sprite('vrrgef408b_05', 2)	# 11-12
    sprite('vrrgef408b_06', 2)	# 13-14

@State
def rgef408Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirUntechableTime(30)
        Unknown11058('0000000000000000000000000100000000000000')
        AirHitstunAnimation(10)
        AirPushbackY(20000)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown11087(1, 1)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3032()
        teleportRelativeX(250000)
        Unknown1096(1000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 0)
    sprite('vrrgef408_shot00', 1)	# 1-1
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot01', 1)	# 2-2	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown1096(600)
    sprite('vrrgef408_shot01', 1)	# 3-3	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown1096(700)
    sprite('vrrgef408_shot01', 1)	# 4-4	 **attackbox here**
    Unknown1096(900)
    sprite('vrrgef408_shot01', 2)	# 5-6	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    RefreshMultihit()
    Unknown1096(1000)
    sprite('vrrgef408_shot01', 2)	# 7-8	 **attackbox here**
    sprite('vrrgef408_shot01', 4)	# 9-12	 **attackbox here**
    sprite('vrrgef408_shot01', 1)	# 13-13	 **attackbox here**
    sprite('vrrgef408_shot01', 1)	# 14-14	 **attackbox here**
    label(0)
    sprite('vrrgef408_shot02', 2)	# 15-16	 **attackbox here**
    clearUponHandler(54)
    DisableAttackRestOfMove()
    sprite('vrrgef408_shot02', 2)	# 17-18	 **attackbox here**
    sprite('vrrgef408_shot03', 4)	# 19-22	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    DisableAttackRestOfMove()
    sprite('vrrgef408_shot04', 3)	# 23-25
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot05', 3)	# 26-28
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot06', 3)	# 29-31
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown3004(-20)
    sprite('vrrgef408_shot07', 3)	# 32-34
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot06', 3)	# 35-37
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown3038(1)
    sprite('vrrgef408_shot07', 3)	# 38-40

@State
def rgef408ShotASS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirUntechableTime(50)
        AttackP1(70)
        Unknown11058('0000000000000000000000000100000000000000')
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(36000)
        YImpluseBeforeWallbounce(2000)
        Hitstop(14)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown11042(1)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3032()
        teleportRelativeX(250000)
        Unknown1096(1000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 0)
    sprite('vrrgef408_shot00', 1)	# 1-1
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot01', 1)	# 2-2	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown1096(600)
    sprite('vrrgef408_shot01', 1)	# 3-3	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown1096(700)
    sprite('vrrgef408_shot01', 1)	# 4-4	 **attackbox here**
    Unknown1096(900)
    sprite('vrrgef408_shot01', 2)	# 5-6	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    RefreshMultihit()
    Unknown1096(1000)
    sprite('vrrgef408_shot01', 2)	# 7-8	 **attackbox here**
    sprite('vrrgef408_shot01', 4)	# 9-12	 **attackbox here**
    sprite('vrrgef408_shot01', 1)	# 13-13	 **attackbox here**
    sprite('vrrgef408_shot01', 1)	# 14-14	 **attackbox here**
    label(0)
    sprite('vrrgef408_shot02', 2)	# 15-16	 **attackbox here**
    clearUponHandler(54)
    DisableAttackRestOfMove()
    sprite('vrrgef408_shot02', 2)	# 17-18	 **attackbox here**
    sprite('vrrgef408_shot03', 4)	# 19-22	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    DisableAttackRestOfMove()
    sprite('vrrgef408_shot04', 3)	# 23-25
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot05', 3)	# 26-28
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot06', 3)	# 29-31
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown3004(-20)
    sprite('vrrgef408_shot07', 3)	# 32-34
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot06', 3)	# 35-37
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown3038(1)
    sprite('vrrgef408_shot07', 3)	# 38-40

@State
def __408_dog():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(50)
        AirPushbackY(25000)
        AirPushbackX(28000)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(800)
        Unknown1007(8000)
        teleportRelativeX(250000)
        Unknown2019(-500)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 0)
    sprite('vrrgef408_00', 3)	# 1-3
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_01', 1)	# 4-4
    physicsXImpulse(6000)
    Unknown1097(-500)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_01', 1)	# 5-5
    Unknown1097(200)
    Unknown1019(150)
    sprite('vrrgef408_01', 1)	# 6-6
    Unknown1097(200)
    Unknown1019(150)
    sprite('vrrgef408_02', 2)	# 7-8	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown1019(200)
    sprite('vrrgef408_02', 2)	# 9-10	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown1097(100)
    sprite('vrrgef408_02', 2)	# 11-12	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_02', 1)	# 13-13	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown1019(90)
    sprite('vrrgef408_02', 1)	# 14-14	 **attackbox here**
    Unknown1019(90)
    sprite('vrrgef408_02', 1)	# 15-15	 **attackbox here**
    Unknown1019(90)
    label(0)
    sprite('vrrgef408_03', 2)	# 16-17	 **attackbox here**
    clearUponHandler(54)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown1019(80)
    sprite('vrrgef408_03', 2)	# 18-19	 **attackbox here**
    Unknown1019(80)
    sprite('vrrgef408_04', 2)	# 20-21
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_04', 2)	# 22-23
    Unknown1019(50)
    sprite('vrrgef408_05', 4)	# 24-27
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown1019(50)
    sprite('vrrgef408_06', 4)	# 28-31
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    physicsXImpulse(0)
    sprite('vrrgef408_07', 4)	# 32-35
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_08', 4)	# 36-39

@State
def __408_dog_Assist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(33)
        AirPushbackY(20000)
        AirPushbackX(28000)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown11042(1)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(800)
        Unknown1007(8000)
        teleportRelativeX(250000)
        Unknown2019(-500)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 0)
    sprite('vrrgef408_00', 3)	# 1-3
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_01', 1)	# 4-4
    physicsXImpulse(6000)
    Unknown1097(-500)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_01', 1)	# 5-5
    Unknown1097(200)
    Unknown1019(150)
    sprite('vrrgef408_01', 1)	# 6-6
    Unknown1097(200)
    Unknown1019(150)
    sprite('vrrgef408_02', 2)	# 7-8	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown1019(200)
    sprite('vrrgef408_02', 2)	# 9-10	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown1097(100)
    sprite('vrrgef408_02', 2)	# 11-12	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_02', 1)	# 13-13	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    Unknown1019(90)
    sprite('vrrgef408_02', 1)	# 14-14	 **attackbox here**
    Unknown1019(90)
    sprite('vrrgef408_02', 1)	# 15-15	 **attackbox here**
    Unknown1019(90)
    label(0)
    sprite('vrrgef408_03', 2)	# 16-17	 **attackbox here**
    clearUponHandler(54)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown1019(80)
    sprite('vrrgef408_03', 2)	# 18-19	 **attackbox here**
    Unknown1019(80)
    sprite('vrrgef408_04', 2)	# 20-21
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_04', 2)	# 22-23
    Unknown1019(50)
    sprite('vrrgef408_05', 4)	# 24-27
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    Unknown1019(50)
    sprite('vrrgef408_06', 4)	# 28-31
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    physicsXImpulse(0)
    sprite('vrrgef408_07', 4)	# 32-35
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_08', 4)	# 36-39

@State
def rgef408Shotsp():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP2(90)
        AirUntechableTime(30)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(20000)
        PushbackX(18000)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11068(1)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3032()
        teleportRelativeX(240000)
        Unknown1096(1350)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
    sprite('vrrgef408_shot00', 4)	# 1-4
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot01boss', 1)	# 5-5	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_shot02', 4)	# 6-9	 **attackbox here**
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot03', 4)	# 10-13	 **attackbox here**
    DisableAttackRestOfMove()
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_shot04', 3)	# 14-16
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot05', 3)	# 17-19
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_shot06', 3)	# 20-22
    Unknown3004(-20)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    sprite('vrrgef408_shot07', 3)	# 23-25
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_shot06', 3)	# 26-28
    Unknown3038(1)
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef408_shot07', 3)	# 29-31
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)

@State
def rgef401atk2nd():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AttackP2(90)
        PushbackX(18000)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown4011(3)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9015(1)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AirUntechableTime(60)
        AirPushbackX(80000)
        Hitstop(8)
        Unknown11089(80)
        Unknown9362(1)
        Unknown9364(20)
        AirHitstunAfterWallbounce(60)
        WallbounceReboundTime(20)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11068(1)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3032()
        teleportRelativeX(-30000)
        Unknown1096(1450)
    sprite('vrrgef401atk_00', 3)	# 1-3
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef401atk_01', 3)	# 4-6
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    GFX_0('rgef_drains', 5)
    GFX_0('rgef_drains', 6)
    sprite('vrrgef401atk_02', 1)	# 7-7
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef401atk_03', 1)	# 8-8
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 5)
    GFX_0('rgef_drains', 6)
    GFX_0('rgef_drains', 7)
    GFX_0('rgef_drains', 8)
    sprite('vrrgef401atk_04ex', 3)	# 9-11	 **attackbox here**
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef401atk_05', 4)	# 12-15
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef401atk_06', 4)	# 16-19
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    sprite('vrrgef401atk_07', 3)	# 20-22
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef401atk_08', 3)	# 23-25
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)

@State
def rgef412effpos():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
    sprite('vrrgef412effpos_00', 3)	# 1-3
    GFX_1('rgef03', 0)
    GFX_1('rgef03', 1)
    GFX_1('rgef03', 2)
    GFX_1('rgef03', 3)
    GFX_1('rgef03', 4)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    GFX_0('rgef_drains', 4)
    sprite('vrrgef412effpos_00', 3)	# 4-6
    GFX_1('rgef03', 5)
    GFX_1('rgef03', 6)
    GFX_1('rgef03', 7)
    GFX_1('rgef03', 8)
    GFX_1('rgef03', 9)
    GFX_0('rgef_drains', 5)
    GFX_0('rgef_drains', 6)
    GFX_0('rgef_drains', 7)
    GFX_0('rgef_drains', 8)
    GFX_0('rgef_drains', 9)
    sprite('vrrgef412effpos_00', 3)	# 7-9
    GFX_1('rgef03', 10)
    GFX_1('rgef03', 11)
    GFX_1('rgef03', 12)
    GFX_1('rgef03', 13)
    GFX_0('rgef_drains', 10)
    GFX_0('rgef_drains', 11)
    GFX_0('rgef_drains', 12)
    GFX_0('rgef_drains', 13)
    sprite('vrrgef412effpos_00', 3)	# 10-12
    GFX_1('rgef03', 14)
    GFX_1('rgef03', 15)
    GFX_1('rgef03', 16)
    GFX_1('rgef03', 17)
    GFX_1('rgef03', 18)
    GFX_1('rgef03', 19)
    GFX_1('rgef03', 20)
    GFX_1('rgef03', 21)
    GFX_1('rgef03', 22)
    GFX_1('rgef03', 23)
    GFX_1('rgef03', 24)
    GFX_1('rgef03', 25)
    GFX_1('rgef03', 26)
    GFX_0('rgef_drains', 14)
    GFX_0('rgef_drains', 15)
    GFX_0('rgef_drains', 16)
    GFX_0('rgef_drains', 17)
    GFX_0('rgef_drains', 18)
    GFX_0('rgef_drains', 19)
    GFX_0('rgef_drains', 20)
    GFX_0('rgef_drains', 21)
    GFX_0('rgef_drains', 22)
    GFX_0('rgef_drains', 23)
    GFX_0('rgef_drains', 24)
    GFX_0('rgef_drains', 25)
    GFX_0('rgef_drains', 26)
    sprite('vrrgef412effpos_00', 3)	# 13-15
    GFX_1('rgef03', 27)
    GFX_1('rgef03', 28)
    GFX_1('rgef03', 29)
    GFX_0('rgef_drains', 27)
    GFX_0('rgef_drains', 28)
    GFX_0('rgef_drains', 29)

@State
def rgef_414():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(0)
        Unknown3032()
        Unknown13044(1)
        teleportRelativeX(-32000)
    sprite('vrrgef414_10', 3)	# 1-3
    sprite('vrrgef414_11', 3)	# 4-6
    sprite('vrrgef414_12', 3)	# 7-9

@State
def rgef_414_fall():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(0)
        Unknown3032()
        Unknown13044(1)
    label(0)
    sprite('vrrgef414_01', 5)	# 1-5
    sprite('vrrgef414_02', 5)	# 6-10
    gotoLabel(0)

@State
def rgef432lock():

    def upon_IMMEDIATE():
        Unknown2019(-100)
        Unknown3032()
        Unknown3001(224)
    sprite('vrrgef432lock_00', 4)	# 1-4
    sprite('vrrgef432lock_01', 4)	# 5-8
    sprite('vrrgef432lock_02', 4)	# 9-12
    sprite('vrrgef432lock_03', 4)	# 13-16
    sprite('vrrgef432lock_04', 4)	# 17-20
    sprite('vrrgef432lock_05', 4)	# 21-24
sprite('null', 1)	# 25-25

@State
def rgef432loop():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown4009(3)
        GFX_2('rgef432_drainhit')
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(10)
        Unknown3076(1000)
        Unknown3077(1200)
        Unknown3032()
        Unknown3001(192)
        Unknown1096(1000)
    sprite('null', 2)	# 1-2
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 3-4
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 5-6
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 7-8
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 9-10
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 11-12
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 13-14
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 15-16
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 17-18
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 19-20
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 21-22
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 23-24
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 25-26
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 27-28
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 29-30
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 31-32
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 33-34
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 35-36
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 37-38
    SFX_0('007_swing_knife_1')
    Unknown3004(-15)
    sprite('null', 2)	# 39-40
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 41-42
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 43-44
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 45-46
    SFX_0('007_swing_knife_1')

@State
def rgef432loop_SP():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown4009(3)
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(10)
        Unknown3076(1000)
        Unknown3077(1200)
        Unknown3032()
        Unknown3001(192)
        Unknown1096(1500)
    sprite('null', 2)	# 1-2
    GFX_1('rgef432loopptc', -1)
    GFX_1('rgef432_drainhit', -1)
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 3-4
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 5-6
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 7-8
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 9-10
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 11-12
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 13-14
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 15-16
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 17-18
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 19-20
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 21-22
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 23-24
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 25-26
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 27-28
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 29-30
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 31-32
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 33-34
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 35-36
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 37-38
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 39-40
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 41-42
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 43-44
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 45-46
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 47-48
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 49-50
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 51-52
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 53-54
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 55-56
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 57-58
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 59-60
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 61-62
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 63-64
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 65-66
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 67-68
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 69-70
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 71-72
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 73-74
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 75-76
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 77-78
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 79-80
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 81-82
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 83-84
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 85-86
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 87-88
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 89-90
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 91-92
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 93-94
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 95-96
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 97-98
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 99-100
    SFX_0('007_swing_knife_1')
    Unknown3004(-15)
    sprite('null', 2)	# 101-102
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 103-104
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 105-106
    SFX_0('007_swing_knife_1')
    sprite('null', 2)	# 107-108
    SFX_0('007_swing_knife_1')

@State
def rgef432fall():

    def upon_IMMEDIATE():
        Unknown6001(1)
        Unknown2055(80)
    label(0)
    sprite('null', 7)	# 1-7
    Unknown23032(50)
    Unknown23033(0)
    Unknown4047(215, 215, 209)
    Unknown4045('7267656634333266616c6c00000000000000000000000000000000000000000000000000')
    gotoLabel(0)

@State
def rgef440():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown4009(2)
        teleportRelativeX(500000)
        Unknown1097(200)
    sprite('vrrgef440_00', 6)	# 1-6
    ScreenShake(20000, 20000)
    sprite('vrrgef440_01', 5)	# 7-11
    sprite('vrrgef440_02', 4)	# 12-15
    sprite('vrrgef440_03', 3)	# 16-18
    sprite('vrrgef440_04', 3)	# 19-21
    GFX_1('rgef02', 0)
    GFX_0('rgef_drains', 0)
    GFX_1('rgef02', 1)
    GFX_0('rgef_drains', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 3)
    GFX_0('rgef_drains', 3)
    GFX_1('rgef02', 4)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 5)
    GFX_0('rgef_drains', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 6)
    GFX_1('rgef02', 7)
    GFX_0('rgef_drains', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 8)
    GFX_1('rgef02', 9)
    GFX_0('rgef_drains', 9)
    sprite('vrrgef440_05', 3)	# 22-24

@State
def rgef440Ex():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown4009(2)
        teleportRelativeX(500000)
        Unknown1097(400)
    sprite('vrrgef440_00', 6)	# 1-6
    ScreenShake(20000, 20000)
    sprite('vrrgef440_01', 5)	# 7-11
    sprite('vrrgef440_02', 4)	# 12-15
    sprite('vrrgef440_03', 3)	# 16-18
    sprite('vrrgef440_04', 3)	# 19-21
    GFX_1('rgef02', 0)
    GFX_0('rgef_drains', 0)
    GFX_1('rgef02', 1)
    GFX_0('rgef_drains', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 3)
    GFX_0('rgef_drains', 3)
    GFX_1('rgef02', 4)
    GFX_0('rgef_drains', 4)
    GFX_1('rgef02', 5)
    GFX_0('rgef_drains', 5)
    GFX_1('rgef02', 6)
    GFX_0('rgef_drains', 6)
    GFX_1('rgef02', 7)
    GFX_0('rgef_drains', 7)
    GFX_1('rgef02', 8)
    GFX_0('rgef_drains', 8)
    GFX_1('rgef02', 9)
    GFX_0('rgef_drains', 9)
    sprite('vrrgef440_05', 3)	# 22-24

@State
def rgef440StartEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown3001(245)
        Unknown1096(1450)
        Unknown1007(-25000)
        teleportRelativeX(75000)
        Unknown23015(6)
    sprite('vrrgef440_10', 6)	# 1-6
    sprite('vrrgef440_11', 5)	# 7-11
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    sprite('vrrgef440_12', 5)	# 12-16
    GFX_1('rgef02', 0)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef440_13', 5)	# 17-21
    GFX_1('rgef02', 0)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef440_14', 4)	# 22-25
    GFX_1('rgef02', 0)
    GFX_0('rgef_drains', 0)
    sprite('vrrgef440_15', 4)	# 26-29
    GFX_1('rgef02', 0)
    GFX_0('rgef_drains', 0)

@State
def rgef450():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(-500)
        Unknown3033()
        Unknown3001(255)
    sprite('vrrgef450atk_00', 2)	# 1-2
    sprite('vrrgef450atk_01', 2)	# 3-4
    sprite('vrrgef450atk_02', 3)	# 5-7
    sprite('vrrgef450atk_03', 5)	# 8-12
    sprite('vrrgef450atk_04', 5)	# 13-17
    sprite('vrrgef450atk_05', 5)	# 18-22
    sprite('vrrgef450atk_06', 5)	# 23-27
    Unknown3004(-10)

@State
def rgef451atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(3)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        teleportRelativeX(100000)
        Unknown1096(1500)
    sprite('vrrgef451atk_01', 2)	# 1-2
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef451atk_02', 2)	# 3-4
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_0('rgef_drain', 5)
    sprite('vrrgef451atk_03', 4)	# 5-8
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_0('rgef_drain', 5)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    sprite('vrrgef451atk_04', 4)	# 9-12
    Unknown1096(750)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_1('rgef02', 10)
    GFX_1('rgef02', 11)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    GFX_0('rgef_drain', 8)
    GFX_0('rgef_drain', 9)
    GFX_0('rgef_drain', 10)
    GFX_0('rgef_drain', 11)
    sprite('vrrgef451atk_05', 4)	# 13-16
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    Unknown4007(0)
    sprite('vrrgef451atk_06', 3)	# 17-19
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    sprite('vrrgef451atk_07', 3)	# 20-22
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef451atk_08', 3)	# 23-25
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    sprite('vrrgef451atk_09', 3)	# 26-28
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef451atk_10', 3)	# 29-31
    sprite('null', 12)	# 32-43

@State
def rgef451atkOD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(3)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        teleportRelativeX(100000)
        Unknown1096(1500)
    sprite('vrrgef451atk_01', 2)	# 1-2
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    sprite('vrrgef451atk_02', 2)	# 3-4
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_0('rgef_drain', 5)
    sprite('vrrgef451atk_03', 4)	# 5-8
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_0('rgef_drain', 5)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    sprite('vrrgef451atk_04', 2)	# 9-10
    Unknown1096(750)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_1('rgef02', 10)
    GFX_1('rgef02', 11)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    GFX_0('rgef_drain', 8)
    GFX_0('rgef_drain', 9)
    GFX_0('rgef_drain', 10)
    GFX_0('rgef_drain', 11)
    sprite('vrrgef451atk_04', 2)	# 11-12
    Unknown1097(150)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_1('rgef02', 10)
    GFX_1('rgef02', 11)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    GFX_0('rgef_drain', 8)
    GFX_0('rgef_drain', 9)
    GFX_0('rgef_drain', 10)
    GFX_0('rgef_drain', 11)
    sprite('vrrgef451atk_04', 2)	# 13-14
    Unknown1097(150)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_1('rgef02', 10)
    GFX_1('rgef02', 11)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    GFX_0('rgef_drain', 8)
    GFX_0('rgef_drain', 9)
    GFX_0('rgef_drain', 10)
    GFX_0('rgef_drain', 11)
    sprite('vrrgef451atk_04', 2)	# 15-16
    Unknown1097(150)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_1('rgef02', 10)
    GFX_1('rgef02', 11)
    GFX_0('rgef_drain', 6)
    GFX_0('rgef_drain', 7)
    GFX_0('rgef_drain', 8)
    GFX_0('rgef_drain', 9)
    GFX_0('rgef_drain', 10)
    GFX_0('rgef_drain', 11)
    sprite('vrrgef451atk_05', 4)	# 17-20
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    Unknown4007(0)
    sprite('vrrgef451atk_06', 3)	# 21-23
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    GFX_1('rgef02', 9)
    sprite('vrrgef451atk_07', 3)	# 24-26
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef451atk_08', 3)	# 27-29
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    sprite('vrrgef451atk_09', 3)	# 30-32
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef451atk_10', 3)	# 33-35
    sprite('null', 12)	# 36-47

@State
def rgef610wingmake():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(-100)
        Unknown3032()
        Unknown3001(255)
    sprite('rgef610_02', 3)	# 1-3
    sprite('rgef610_03', 3)	# 4-6
    sprite('rgef610_04', 3)	# 7-9
    sprite('rgef610_05', 3)	# 10-12
    sprite('rgef610_06', 3)	# 13-15
    sprite('rgef610_06ex01', 3)	# 16-18

@State
def rgef610wingbreak():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2019(-100)
        Unknown3029(1)
        Unknown3070(1)
        Unknown3071(4)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3032()
        Unknown3001(255)
    sprite('rgef610_07', 2)	# 1-2
    Unknown3004(-5)
    Unknown1067(5)
    Unknown1059(10)
    sprite('rgef610_08', 2)	# 3-4
    sprite('rgef610_09', 2)	# 5-6
    GFX_1('rgef610', 4)
    GFX_1('rgef610', 5)
    GFX_1('rgef610', 6)
    GFX_1('rgef610', 7)
    sprite('rgef610_10', 2)	# 7-8
    GFX_1('rgef610', 0)
    GFX_1('rgef610', 1)
    GFX_1('rgef610', 2)
    GFX_1('rgef610', 3)
    sprite('rgef610_11', 2)	# 9-10
    GFX_1('rgef610', 0)
    GFX_1('rgef610', 1)
    GFX_1('rgef610', 2)
    GFX_1('rgef610', 3)
    GFX_1('rgef610', 4)
    GFX_1('rgef610', 5)
    GFX_1('rgef610', 6)
    GFX_1('rgef610', 7)
    sprite('rgef610_12', 2)	# 11-12
    GFX_1('rgef610', 0)
    GFX_1('rgef610', 1)
    GFX_1('rgef610', 2)
    GFX_1('rgef610', 3)
    GFX_1('rgef610', 4)
    GFX_1('rgef610', 5)
    GFX_1('rgef610', 6)
    GFX_1('rgef610', 7)
    sprite('rgef610_13', 3)	# 13-15
    GFX_1('rgef610', 0)
    GFX_1('rgef610', 1)
    GFX_1('rgef610', 2)
    GFX_1('rgef610', 3)
    sprite('rgef610_14', 3)	# 16-18
    GFX_1('rgef610', 4)
    GFX_1('rgef610', 5)
    GFX_1('rgef610', 6)
    GFX_1('rgef610', 7)
    sprite('rgef610_15', 4)	# 19-22
    GFX_1('rgef610', 1)
    GFX_1('rgef610', 2)
    GFX_1('rgef610', 3)
    GFX_1('rgef610', 4)
    sprite('rgef610_16', 4)	# 23-26
    sprite('null', 30)	# 27-56

@State
def AstralMoveSword():

    def upon_IMMEDIATE():
        Unknown1056(-1000)
    sprite('rg460_swd00', 4)	# 1-4
    physicsYImpulse(-34000)
    sprite('rg460_swd01', 4)	# 5-8
    sprite('rg460_swd02', 4)	# 9-12
    physicsYImpulse(2000)

@State
def ChangeToDeathscythe():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown4007(3)
        Unknown4009(3)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3070(1)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1050)
        Unknown3032()
        Unknown3001(255)
        Unknown1056(-1000)
    sprite('rg460_kama00', 1)	# 1-1
    SFX_3('rgse_05')
    sprite('rg460_kama00ex01', 2)	# 2-3
    sprite('rg460_kama00ex02', 2)	# 4-5
    sprite('rg460_kama00ex03', 2)	# 6-7
    sprite('rg460_kama00ex04', 2)	# 8-9
    sprite('rg460_kama00ex05', 2)	# 10-11
    SFX_0('105_guard_slash_2')
    SFX_3('rgse_21')
    sprite('rg460_kama01', 14)	# 12-25	 **attackbox here**
    sprite('rg460_kama02', 2)	# 26-27	 **attackbox here**
    sprite('rg460_kama03', 2)	# 28-29	 **attackbox here**
    sprite('rg460_kama04', 2)	# 30-31	 **attackbox here**
    sprite('rg460_kama05', 2)	# 32-33	 **attackbox here**
    sprite('rg460_kama06', 2)	# 34-35	 **attackbox here**
    sprite('rg460_kama07', 2)	# 36-37	 **attackbox here**
    SFX_3('rgse_25')
    SFX_3('rgse_25')
    sprite('rg460_kama07ex01', 2)	# 38-39	 **attackbox here**
    sprite('rg460_kama07ex02', 2)	# 40-41	 **attackbox here**
    sprite('rg460_kama07', 2)	# 42-43	 **attackbox here**
    sprite('rg460_kama07ex01', 2)	# 44-45	 **attackbox here**
    sprite('rg460_kama07ex02', 2)	# 46-47	 **attackbox here**
    loopRest()

@State
def nyPhantom():

    def upon_IMMEDIATE():
        Unknown2010()
        Hitstop(6)
        AttackLevel_(4)
        AttackP1(80)
        Damage(700)
        PushbackX(18000)
        blockstun(25)
        hitstun(25)
        AirUntechableTime(27)
        Unknown4061(2)
        Unknown2019(-500)
        Unknown2005()
        Unknown3001(0)
        Unknown3032()
        teleportRelativeX(-600000)
        Unknown1007(10000)
        Unknown1096(1000)
    sprite('ny600_11', 6)	# 1-6
    Unknown3004(10)
    sprite('ny600_12', 6)	# 7-12
    sprite('ny600_13', 6)	# 13-18
    Unknown3001(128)
    Unknown3004(0)
    sprite('ny600_14', 6)	# 19-24
    sprite('ny600_11', 6)	# 25-30
    sprite('ny600_12', 6)	# 31-36
    sprite('ny600_13', 6)	# 37-42
    sprite('ny600_14', 6)	# 43-48
    sprite('ny600_11', 6)	# 49-54
    sprite('ny600_12', 6)	# 55-60
    sprite('ny600_13', 6)	# 61-66
    sprite('ny600_14', 6)	# 67-72
    sprite('ny600_11', 6)	# 73-78
    sprite('ny600_12', 6)	# 79-84
    sprite('ny600_13', 6)	# 85-90
    sprite('ny600_14', 6)	# 91-96
    sprite('ny600_11', 6)	# 97-102
    sprite('ny600_12', 6)	# 103-108
    sprite('ny600_13', 6)	# 109-114
    sprite('ny600_14', 6)	# 115-120
    sprite('ny600_11', 6)	# 121-126
    sprite('ny600_12', 6)	# 127-132
    sprite('ny600_13', 6)	# 133-138
    sprite('ny600_14', 6)	# 139-144
    sprite('ny600_11', 6)	# 145-150
    sprite('ny600_12', 6)	# 151-156
    sprite('ny600_13', 6)	# 157-162
    sprite('ny600_14', 6)	# 163-168
    sprite('ny600_11', 6)	# 169-174
    Unknown3004(-2)
    physicsXImpulse(1000)
    sprite('ny600_12', 6)	# 175-180
    physicsXImpulse(400)
    sprite('ny600_13', 6)	# 181-186
    sprite('ny600_14', 6)	# 187-192
    sprite('ny600_11', 6)	# 193-198
    sprite('ny600_12', 6)	# 199-204
    sprite('ny600_13', 6)	# 205-210
    sprite('ny600_14', 6)	# 211-216
    sprite('ny600_11', 6)	# 217-222
    sprite('ny600_12', 6)	# 223-228
    sprite('ny600_13', 6)	# 229-234
    sprite('ny600_14', 6)	# 235-240

@State
def rgef203atkD3rd():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(85)
        AttackP2(82)
        Unknown11058('0000000001000000000000000000000000000000')
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9130(60)
        Unknown9142(42)
        PushbackX(12000)
        AirPushbackY(-60000)
        AirPushbackX(12000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(90)
        Unknown9310(1)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown4011(3)
        Unknown4007(3)
        Unknown11060(800)
        Unknown11087(1, 1)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1096(1500)
        Unknown3001(212)
        teleportRelativeX(-150000)
    sprite('vrrgef203atk_00', 4)	# 1-4
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('vrrgef203atk_01', 4)	# 5-8
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef203atk_02', 4)	# 9-12
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_03', 4)	# 13-16
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_04ex', 4)	# 17-20	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_05ex', 4)	# 21-24	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_06ex', 4)	# 25-28	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef203atk_07', 4)	# 29-32
    Unknown3001(212)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_08', 3)	# 33-35
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_09', 4)	# 36-39
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    sprite('vrrgef203atk_10', 4)	# 40-43
    GFX_1('rgef02', 0)

@State
def EventEffectRGVsTB_Hakumen():
    sprite('ha041_03', 32767)	# 1-32767
    Unknown4061(7)
    Unknown2006()
    Unknown2005()
    teleportRelativeX(-520000)
    loopRest()

@State
def NOISE():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('65665f6576656e746e6f6973652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(4)
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 60)	# 1-60
    loopRest()

@State
def rgef414atk():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1096(1000)
        Unknown3001(212)
        teleportRelativeX(-50000)
    sprite('vrrgef203atk_00', 2)	# 1-2
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('vrrgef203atk_01', 2)	# 3-4
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef203atk_02', 2)	# 5-6
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_03', 2)	# 7-8
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_04ex', 2)	# 9-10	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_05ex', 2)	# 11-12	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_06ex', 2)	# 13-14	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef203atk_07', 4)	# 15-18
    Unknown3001(212)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_08', 3)	# 19-21
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_09', 4)	# 22-25
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    sprite('vrrgef203atk_10', 4)	# 26-29
    GFX_1('rgef02', 0)

@State
def NmlAtk5AAAA_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1096(1300)
        Unknown3001(212)
        teleportRelativeX(-30000)
        Unknown2003(1)
    sprite('vrrgef203atk_00', 2)	# 1-2
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('vrrgef203atk_01', 2)	# 3-4
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef203atk_02', 2)	# 5-6
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_03', 2)	# 7-8
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_04ex', 1)	# 9-9	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_05ex', 1)	# 10-10	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_06ex', 3)	# 11-13	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef203atk_07', 3)	# 14-16
    Unknown3001(212)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_08', 3)	# 17-19
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_09', 3)	# 20-22
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    sprite('vrrgef203atk_10', 3)	# 23-25
    GFX_1('rgef02', 0)

@State
def DS_Niku_Head():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Niku_Body():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Niku_Leg():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Niku_Approach():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Niku_Throw():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Shot_Head():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Shot_Body():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Shot_Leg():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Shot_Approach():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def DS_Shot_Throw():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(10000)
        Unknown11064(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown4061(1)
        Unknown1086(22)
    sprite('vrrgef408_shot03', 60)	# 1-60	 **attackbox here**

@State
def Eventrgef_drains():
    sprite('null', 200)	# 1-200
    Unknown4047(224, 224, 224)
    Unknown23067('rgef_draina')
    Unknown1096(2000)
    Unknown3038(1)

@State
def Eventrgef_drains2():
    sprite('null', 6)	# 1-6
    Unknown1007(200000)
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')

@State
def Eventrgef_drains3():

    def upon_IMMEDIATE():
        pass
    sprite('null', 100)	# 1-100
    Unknown1007(200000)
    Unknown4049(3000)
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000000000000')
    Unknown4047(215, 215, 209)
    Unknown4045('72676566343332627265616b000000000000000000000000000000000000000000000000')

@State
def HAKUMEN_NOUNAI():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown6001(1)
        Unknown1000(-640000)
        teleportRelativeY(0)
        Unknown1096(20000)
        sendToLabelUpon(32, 0)
    sprite('vr_screen_black', 30)	# 1-30
    Unknown3001(0)
    Unknown3004(4)
    sprite('vr_screen_black', 32767)	# 31-32797
    Unknown3004(0)
    Unknown3001(120)
    label(0)
    sprite('vr_screen_black', 30)	# 32798-32827
    Unknown3004(-4)
    sprite('vr_screen_black', 10)	# 32828-32837
    Unknown3001(0)
    Unknown3004(0)

@State
def Eventrgef414atk():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1100)
        Unknown1096(1000)
        Unknown3001(212)
        teleportRelativeX(-50000)
    sprite('vrrgef203atk_00', 4)	# 1-4
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('vrrgef203atk_01', 4)	# 5-8
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    sprite('vrrgef203atk_02', 4)	# 9-12
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_03', 4)	# 13-16
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_04ex', 3)	# 17-19	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_05ex', 2)	# 20-21	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    StartMultihit()
    sprite('vrrgef203atk_06ex', 2)	# 22-23	 **attackbox here**
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_0('rgef_drain', 4)
    GFX_1('rgef02', 6)
    GFX_1('rgef02', 7)
    GFX_1('rgef02', 8)
    sprite('vrrgef203atk_07', 4)	# 24-27
    Unknown3001(212)
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_0('rgef_drain', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    GFX_1('rgef02', 6)
    sprite('vrrgef203atk_08', 3)	# 28-30
    GFX_0('rgef_drain', 0)
    GFX_0('rgef_drain', 1)
    GFX_0('rgef_drain', 2)
    GFX_1('rgef02', 3)
    GFX_1('rgef02', 4)
    GFX_1('rgef02', 5)
    sprite('vrrgef203atk_09', 4)	# 31-34
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_1('rgef02', 1)
    GFX_1('rgef02', 2)
    GFX_1('rgef02', 3)
    sprite('vrrgef203atk_10', 4)	# 35-38
    GFX_1('rgef02', 0)

@State
def Eventoffset():

    def upon_IMMEDIATE():
        Unknown1001(0)
        teleportRelativeY(1000000)
        Unknown1010(-100000, 100000)
    sprite('null', 4)	# 1-4
    GFX_1('ef_offset', 0)
    SFX_0('108_attack_offset')
    ScreenShake(30000, 30000)

@State
def EventRC():

    def upon_IMMEDIATE():
        Unknown30012('00000000')
        sendToLabelUpon(32, 10)
        Unknown1000(-340000)
        Unknown2019(501)
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('rc033_00', 2)	# 64-65
    physicsXImpulse(-30000)
    physicsYImpulse(20800)
    setGravity(850)
    Unknown8001(3, 100)
    sprite('rc033_01', 2)	# 66-67
    sprite('rc033_02', 3)	# 68-70
    sprite('rc033_03', 3)	# 71-73
    sprite('rc033_04', 3)	# 74-76
    sprite('rc033_05', 3)	# 77-79
    sprite('rc033_02', 3)	# 80-82
    sprite('rc033_03', 3)	# 83-85
    sprite('rc033_04', 3)	# 86-88
    sprite('rc033_05', 3)	# 89-91

@State
def EventWhiteOut():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(20000)
    sprite('vr_white', 20)	# 1-20
    Unknown3004(15)
    sprite('vr_white', 45)	# 21-65
    sprite('vr_white', 20)	# 66-85
    Unknown3001(200)
    Unknown3004(-10)

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)	# 1-10
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Noise():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('65665f6576656e746e6f6973652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 30)	# 1-30
    SFX_0('014_electric_ml')
    loopRest()

@State
def Noise_Long():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('65665f6576656e746e6f6973652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23032(50)
        Unknown23033(50)
        Unknown2037(5)
        SLOT_58 = 10

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown2038(-1)
                if (SLOT_2 <= 0):
                    SLOT_58 = (SLOT_58 + (-1))
                    Unknown61(0, 30, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0)
                    SLOT_2 = SLOT_0
                    SFX_0('014_electric_l')
            if (SLOT_58 <= 0):
                clearUponHandler(3)

        def upon_32():
            clearUponHandler(3)
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 1)	# 32768-32768

@State
def __3d_test():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('65665f746573742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(5000)
        Unknown1007(192000)
        teleportRelativeX(192000)
    sprite('null', 60)	# 1-60

@State
def Fade1():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    sprite('null', 5)	# 1-5
    GFX_0('LifeLinkEff', 0)

@State
def LifeLinkEff():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 1)	# 1-1
    Unknown4045('6e7465665f73746f72795f6c6966656c696e6b6566665f6c696e653200000000ffffffff')