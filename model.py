import copy

ATTACK_LEVEL = {"blockstun": [9, 11, 13, 16, 18, 20],
                "hitstun": [10, 12, 14, 17, 19, 21],
                "untech": [12, 12, 14, 17, 19, 21],
                "hitstop": [8, 9, 10, 11, 12, 13],
                "hitstopCH": [0, 0, 0, 2, 5, 8],
                "p1": [100, 100, 100, 100, 100, 100],
                "p2": [65, 70, 75, 80, 85, 90],
                "damage": [1000, 1000, 1000, 1500, 1700, 2000]}


class State:
    def __init__(self):
        self.inUponImmediate = False
        self.uponImmediateIndent = ""
        self.moveName = ""
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        self.disableAttackboxes = False
        self.disableAttackboxesThisFrame = False
        self.isNewHit = True
        self.attackInfo = AttackInfo()
        self.attackInfo.groundHitAni = 0
        self.attackInfo.airHitAni = 0
        self.exitState = False
        self.landingRecovery = 0
        self.isSubroutine = False
        self.isInv = False
        self.invType = 0  # Inv or Guard
        self.invAttr = [True, True, True, True, True]  # Head, Body, Foot, Proj, Throw
        self.superflash_list = []    # list of tuples. Each tuple contains when superlflash starts and superflash duration
        self.attackLevel = None
        self.attr = None
        self.hardcodedInvList = []  # list of tuples. Each tuple contains when hardcoded inv starts, duration, inv type, and inv attr

    def clear_values(self, is_new_move):
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        self.disableAttackboxesThisFrame = False
        self.inUponImmediate = False
        self.uponImmediateIndent = ""
        if is_new_move:
            self.moveName = ""
            self.disableAttackboxes = False
            self.isNewHit = True
            self.exitState = False
            self.landingRecovery = None
            self.isSubroutine = False
            self.attackInfo = AttackInfo()
            self.attackInfo.groundHitAni = 0
            self.attackInfo.airHitAni = 0
            self.isInv = False
            self.invType = 0  # Inv or Guard
            self.invAttr = [True, True, True, True, True]  # Head, Body, Foot, Proj, Throw
            self.attr = None
            self.superflash_list = []    # list of tuples. Each tuple contains when superlflash starts and superflash duration
            self.hardcodedInvList = []

    def is_attackbox(self):
        return self.isAttackBox and (self.isNewHit or not self.disableAttackboxes) and not self.disableAttackboxesThisFrame

    def set_values_from_subroutine(self, subroutine):
        if subroutine is None:
            return
        self.landingRecovery = subroutine.landingRecovery
        self.attackInfo = subroutine.attackInfo


class AttackInfo:
    def __init__(self, damage=None, p1=None, p2=None, min_damage=0, p2once=None, hitstun=None, untech=None, blockstun=None,
                 hitstop=None, bonus_blockstop=None, bonus_hitstop=None, attack_level=None, attribute=None, ground_hit_ani=None,
                 air_hit_ani=None, knockdown=None, slide_time=None, hitstun_after_wall_bounce=None, wallstick=None,
                 stagger=None, spin_fall=None, ground_bounce=None, wall_bounce=None):
        self.damage = damage
        self.p1 = p1
        self.p2 = p2
        self.minDamage = min_damage
        self.p2Once = p2once
        self.hitstun = hitstun
        self.untech = untech
        self.blockstun = blockstun
        self.attackLevel = attack_level
        self.hitstop = hitstop
        self.bonus_blockstop = bonus_blockstop    # for additional hitstop the opponent experiences on block
        self.bonus_hitstop = bonus_hitstop       # for additonoal hitstop the opponent experiences on hit
        self.attribute = copy.copy(attribute)
        self.groundHitAni = ground_hit_ani
        self.airHitAni = air_hit_ani
        self.knockdown = knockdown
        self.slide = slide_time
        self.hitstunAfterWallBounce = hitstun_after_wall_bounce
        self.wallStick = wallstick
        self.stagger = stagger
        self.spinFall = spin_fall
        self.groundBounce = ground_bounce
        self.wallBounce = wall_bounce

    def copy_non_none_values(self, other):
        self.damage = other.damage if other.damage is not None else self.damage
        self.p1 = other.p1 if other.p1 is not None else self.p1
        self.p2 = other.p2 if other.p2 is not None else self.p2
        self.minDamage = other.minDamage if other.minDamage is not None else self.minDamage
        self.p2Once = other.p2Once if other.p2Once is not None else self.p2Once
        self.hitstun = other.hitstun if other.hitstun is not None else self.hitstun
        self.untech = other.untech if other.untech is not None else self.untech
        self.blockstun = other.blockstun if other.blockstun is not None else self.blockstun
        self.attackLevel = other.attackLevel if other.attackLevel is not None else self.attackLevel
        self.hitstop = other.hitstop if other.hitstop is not None else self.hitstop
        self.bonus_blockstop = other.bonus_blockstop if other.bonus_blockstop is not None else self.bonus_blockstop
        self.bonus_hitstop = other.bonus_hitstop if other.bonus_hitstop is not None else self.bonus_hitstop
        self.attribute = copy.copy(other.attribute) if other.attribute is not None else self.attribute
        self.groundHitAni = other.groundHitAni if other.groundHitAni is not None else self.groundHitAni
        self.airHitAni = other.airHitAni if other.airHitAni is not None else self.airHitAni
        self.knockdown = other.knockdown if other.knockdown is not None else self.knockdown
        self.slide = other.slide if other.slide is not None else self.slide
        self.hitstunAfterWallBounce = other.hitstunAfterWallBounce if other.hitstunAfterWallBounce is not None else self.hitstunAfterWallBounce
        self.wallStick = other.wallStick if other.wallStick is not None else self.wallStick
        self.stagger = other.stagger if other.stagger is not None else self.stagger
        self.spinFall = other.spinFall if other.spinFall is not None else self.spinFall
        self.groundBounce = other.groundBounce if other.groundBounce is not None else self.groundBounce
        self.wallBounce = other.wallBounce if other.wallBounce is not None else self.wallBounce

    def __str__(self):
        toReturn = "damage=" + str(self.damage) + "p1=" + str(self.p1) + "p2=" + str(self.p2)
        if self.p2Once:
            toReturn = toReturn + "(once)"
        toReturn = toReturn + "minDamage=" + str(self.minDamage) + "attackLv=" + str(self.attackLevel) + \
                   "attr=" + str(self.attribute) + "blockstun=" + str(self.get_blockstun()) + "hitstun=" + str(self.get_hitstun()) + \
                   "untech=" + str(self.get_untech()) + "hitstop=" + str(self.get_hitstop()) + "bonusBlockstop=" + str(self.bonus_blockstop) + \
                   "bonusHitstop=" + str(self.bonus_hitstop)
        return toReturn

    def __eq__(self, other):
        if not isinstance(other, AttackInfo):
            return False
        return self.damage == other.damage and self.p1 == other.p1 and self.p2 == other.p2 and \
               self.minDamage == other.minDamage and self.p2Once == other.p2Once and self.blockstun == other.blockstun and \
               self.hitstun == other.hitstun and self.untech == other.untech and self.attackLevel == other.attackLevel and \
               self.hitstop == other.hitstop and self.bonus_blockstop == other.bonus_blockstop and \
               self.bonus_hitstop == other.bonus_hitstop and self.attribute == other.attribute and \
               self.groundHitAni == other.groundHitAni and self.airHitAni == other.airHitAni and \
               self.groundBounce == other.groundBounce and self.wallBounce == other.wallBounce

    def __ne__(self, other):
        if not isinstance(other, AttackInfo):
            return False
        return not self.__eq__(other)

    def get_blockstun(self):
        if self.blockstun is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["blockstun"][self.attackLevel]
        return self.blockstun

    def get_hitstun(self):
        if self.hitstun is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["hitstun"][self.attackLevel]
        return self.hitstun

    def get_hitstop(self):
        if self.hitstop is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["hitstop"][self.attackLevel]
        return self.hitstop

    def get_untech(self):
        if self.untech is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["untech"][self.attackLevel]
        return self.untech

    def get_p1(self):
        if self.p1 is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["p1"][self.attackLevel]
        return self.p1

    def get_p2(self):
        if self.p2 is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["p2"][self.attackLevel]
        return self.p2

    def get_damage(self):
        if self.damage is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["damage"][self.attackLevel]
        return self.damage

    def override_non_none_values(self, other):
        if other.damage is not None:
            self.damage = other.damage
        if other.p1 is not None:
            self.p1 = other.p1
        if other.p2 is not None:
            self.p2 = other.p2
        if other.p2Once is not None:
            self.p2Once = other.p2Once
        if other.minDamage is not None:
            self.minDamage = other.minDamage
        if other.hitstun is not None:
            self.hitstun = other.hitstun
        if other.untech is not None:
            self.untech = other.untech
        if other.blockstun is not None:
            self.blockstun = other.blockstun
        if other.attackLevel is not None:
            self.attackLevel = other.attackLevel
        if other.hitstop is not None:
            self.hitstop = other.hitstop
        if other.bonus_blockstop is not None:
            self.bonus_blockstop = other.bonus_blockstop
        if other.bonus_hitstop is not None:
            self.bonus_hitstop = other.bonus_hitstop
        if other.attribute is not None:
            self.attribute = other.attribute
        if other.groundHitAni is not None:
            self.groundHitAni = other.groundHitAni
        if other.airHitAni is not None:
            self.airHitAni = other.airHitAni
        if other.groundBounce is not None:
            self.groundBounce = other.groundBounce


class Abstract:
    def __init__(self):
        pass


class AbstractFrames(Abstract):
    def __init__(self, duration=0):
        Abstract.__init__(self)
        self.duration = duration
        self.inv_type = 0  # 0 = no inv, 1 = inv, 2 = guard
        self.inv_attr = [False, False, False, False, False]

    def __str__(self):
        return str(self.duration)

    def __eq__(self, other):
        if not isinstance(other, AbstractFrames):
            return False
        return self.duration == other.duration and self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

    def __ne__(self, other):
        if not isinstance(other, AbstractFrames):
            return False
        return not self.__eq__(other)


class ActiveFrames(AbstractFrames):
    def __init__(self, duration=0, is_new_hit=True, info=AttackInfo(0)):
        AbstractFrames.__init__(self, duration)
        self.is_new_hit = is_new_hit
        self.info = copy.copy(info)

    def __str__(self):
        to_return = str(self.duration)
        to_return += " Active"
        to_return += " New Hit " + str(self.is_new_hit)
        to_return += " Blockstun " + str(self.info.get_blockstun())
        to_return += " Hitstop " + str(self.info.get_hitstop()) + "/+" + str(self.info.bonus_blockstop) + "/+" + str(self.info.bonus_hitstop)
        return to_return

    def __eq__(self, other):
        if not isinstance(other, ActiveFrames):
            return False
        return self.duration == other.duration and self.is_new_hit == other.is_new_hit and \
            self.info == other.info and self.duration == other.duration and \
            self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

    def __ne__(self, other):
        if not isinstance(other, ActiveFrames):
            return False
        return not self.__eq__(other)


class WaitFrames(AbstractFrames):
    def __init__(self, duration=0):
        AbstractFrames.__init__(self, duration)

    def __eq__(self, other):
        if not isinstance(other, WaitFrames):
            return False
        return self.duration == other.duration and self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

    def __ne__(self, other):
        if not isinstance(other, WaitFrames):
            return False
        return not self.__eq__(other)


class SubroutineCall(Abstract):
    def __init__(self, name, same_thread = False):
        Abstract.__init__(self)
        self.name = name
        self.sameThread = same_thread

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, SubroutineCall):
            return False
        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, SubroutineCall):
            return False
        return not self.__eq__(other)


class Move:
    def __init__(self):
        self.frame_chunks = []
        self.additional_chunks = []
        self.landing_recovery = 0
        self.superflash_list = []
        self.hardcoded_inv_list = []

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False

        if len(self.frame_chunks) != len(other.frame_chunks):
            return False
        for i in range(len(self.frame_chunks)):
            if self.frame_chunks[i] != other.frame_chunks[i]:
                return False

        if len(self.additional_chunks) != len(other.additional_chunks):
            return False
        for i in range(len(self.additional_chunks)):
            if len(self.additional_chunks[i]) != len(other.additional_chunks[i]):
                return False
            for j in range(len(self.additional_chunks[i])):
                if self.additional_chunks[i][j] != other.additional_chunks[i][j]:
                    return False
        return self.landing_recovery == other.landing_recovery and self.superflash_list == other.superflash_list and \
               self.hardcoded_inv_list == other.hardcoded_inv_list

    def __ne__(self, other):
        if not isinstance(other, Move):
            return False
        return not self.__eq__(other)


class Subroutine:
    def __init__(self, state=None):
        if state is not None:
            self.landingRecovery = state.landingRecovery
            self.attackInfo = AttackInfo()
            self.attackInfo.copy_non_none_values(state.attackInfo)
        else:
            self.landingRecovery = None
            self.attackInfo = AttackInfo()

    def __eq__(self, other):
        if not isinstance(other, Subroutine):
            return False
        return self.attackInfo == other.attackInfo and self.landingRecovery == other.landingRecovery

    def __ne__(self, other):
        if not isinstance(other, Subroutine):
            return False
        return not self.__eq__(other)


def consolidate_frame_chunks(chunk_list, ignore_inv=False):
    new_chunk_list = []
    prev_chunk = copy.copy(chunk_list[0])
    for i in range(1, len(chunk_list)):
        chunk = chunk_list[i]
        if isinstance(prev_chunk, ActiveFrames) and isinstance(chunk, ActiveFrames) \
                and (has_same_inv(prev_chunk, chunk) or ignore_inv):
            if chunk.is_new_hit:
                new_chunk_list.append(prev_chunk)
                prev_chunk = copy.copy(chunk)
            else:
                prev_chunk.duration += chunk.duration
        elif isinstance(prev_chunk, WaitFrames) and isinstance(chunk, WaitFrames) \
                and (has_same_inv(prev_chunk, chunk) or ignore_inv):
            prev_chunk.duration += chunk.duration
        else:
            new_chunk_list.append(prev_chunk)
            prev_chunk = copy.copy(chunk)
    new_chunk_list.append(prev_chunk)

    return new_chunk_list


def has_same_inv(chunk1, chunk2):
    return chunk1.inv_type == chunk2.inv_type and chunk1.inv_attr == chunk2.inv_attr
