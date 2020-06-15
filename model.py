import copy
import heapq
from collections import OrderedDict

ATTACK_LEVEL = {"blockstun": [9, 11, 13, 16, 18, 20],
                "hitstun": [10, 12, 14, 17, 19, 21],
                "hitstunCH": [4, 4, 4, 5, 5, 6],
                "untech": [12, 12, 14, 17, 19, 21],
                "untechCH": [11, 11, 12, 14, 15, 16],
                "stagger": [20, 22, 24, 27, 29, 31],
                "staggerFallStart": [30, 32, 34, 37, 39, 41],
                "hitstop": [8, 9, 10, 11, 12, 13],
                "hitstopCH": [0, 0, 1, 2, 5, 8],
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
        self.attackInfo.normalHitEffects = HitEffects(ground_hit_ani=0, air_hit_ani=0)
        self.exitState = False
        self.landingRecovery = 0
        self.isSubroutine = False
        self.isInv = False
        self.invType = 0  # Inv or Guard
        self.invAttr = [True, True, True, True, True]  # Head, Body, Foot, Proj, Throw
        self.superflash_list = []  # list of tuples. Each tuple contains when superlflash starts and superflash duration
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
            self.superflash_list = []  # list of tuples. Each tuple contains when superlflash starts and duration
            self.hardcodedInvList = []

    def is_attackbox(self):
        return self.isAttackBox and (
                self.isNewHit or not self.disableAttackboxes) and not self.disableAttackboxesThisFrame

    def set_values_from_subroutine(self, subroutine):
        if subroutine is None:
            return
        self.landingRecovery = subroutine.landingRecovery
        self.attackInfo = subroutine.attackInfo


class AttackInfo:
    def __init__(self, damage=None, p1=None, p2=None, min_damage=0, p2once=None, blockstun=None,
                 hitstop=None, bonus_blockstop=None, bonus_hitstop=None, attack_level=None, attribute=None,
                 normal_hit=None, counter_hit=None, bonus_counterhitstop=None):
        self.damage = damage
        self.p1 = p1
        self.p2 = p2
        self.minDamage = min_damage
        self.p2Once = p2once
        self.blockstun = blockstun
        self.attackLevel = attack_level
        self.hitstop = hitstop
        self.bonusBlockstop = bonus_blockstop  # for additional hitstop the opponent experiences on block
        self.bonusHitstop = bonus_hitstop  # for additonoal hitstop the opponent experiences on hit
        self.bonusHitstopCH = bonus_counterhitstop  # for additonoal hitstop the opponent experiences on counter hit
        self.attribute = copy.copy(attribute)
        self.normalHitEffects = copy.copy(normal_hit) if normal_hit is not None else HitEffects()
        self.counterHitEffects = copy.copy(counter_hit) if counter_hit is not None else HitEffects()

    def copy_non_none_values(self, other):
        self.damage = other.damage if other.damage is not None else self.damage
        self.p1 = other.p1 if other.p1 is not None else self.p1
        self.p2 = other.p2 if other.p2 is not None else self.p2
        self.minDamage = other.minDamage if other.minDamage is not None else self.minDamage
        self.p2Once = other.p2Once if other.p2Once is not None else self.p2Once
        self.blockstun = other.blockstun if other.blockstun is not None else self.blockstun
        self.attackLevel = other.attackLevel if other.attackLevel is not None else self.attackLevel
        self.hitstop = other.hitstop if other.hitstop is not None else self.hitstop
        self.bonusBlockstop = other.bonusBlockstop if other.bonusBlockstop is not None else self.bonusBlockstop
        self.bonusHitstop = other.bonusHitstop if other.bonusHitstop is not None else self.bonusHitstop
        self.bonusHitstopCH = other.bonusHitstopCH if other.bonusHitstopCH is not None else self.bonusHitstopCH
        self.attribute = copy.copy(other.attribute) if other.attribute is not None else self.attribute
        self.normalHitEffects = copy.copy(
            other.normalHitEffects) if other.normalHitEffects is not None else self.normalHitEffects
        self.counterHitEffects = copy.copy(
            other.counterHitEffects) if other.counterHitEffects is not None else self.counterHitEffects

    def __str__(self):
        to_return = "damage=" + str(self.damage) + "p1=" + str(self.p1) + "p2=" + str(self.p2)
        if self.p2Once:
            to_return = to_return + "(once)"
        to_return = to_return + "minDamage=" + str(self.minDamage) + "attackLv=" + str(self.attackLevel) + \
                "attr=" + str(self.attribute) + "blockstun=" + str(self.get_blockstun()) + "hitstun=" + \
                str(self.get_hitstun()) + "untech=" + str(self.get_untech()) + "hitstop=" + str(self.get_hitstop()) + \
                "bonusBlockstop=" + str(self.bonusBlockstop) + "bonusHitstop=" + \
                str(self.bonusHitstop) + "bonusCounterHitstop=" + str(self.bonusHitstopCH)
        return to_return

    def __eq__(self, other):
        if not isinstance(other, AttackInfo):
            return False
        return self.damage == other.damage and self.p1 == other.p1 and self.p2 == other.p2 and \
               self.minDamage == other.minDamage and self.p2Once == other.p2Once and self.blockstun == other.blockstun and \
               self.attackLevel == other.attackLevel and self.hitstop == other.hitstop and \
               self.bonusBlockstop == other.bonusBlockstop and self.bonusHitstop == other.bonusHitstop and \
               self.bonusHitstopCH == other.bonusHitstopCH and self.attribute == other.attribute and \
               self.normalHitEffects == other.normalHitEffects and self.counterHitEffects == other.counterHitEffects

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
        if self.normalHitEffects.hitstun is not None:
            return self.normalHitEffects.hitstun

        if self.attackLevel is not None:
            return ATTACK_LEVEL["hitstun"][self.attackLevel]
        return None

    def get_hitstun_ch(self):
        fatal_bonus = 3 if self.counterHitEffects.fatal else 0
        if self.counterHitEffects.hitstun is not None:
            return self.counterHitEffects.hitstun + fatal_bonus

        if self.attackLevel is not None:
            return self.get_hitstun() + ATTACK_LEVEL["hitstunCH"][self.attackLevel] + fatal_bonus

        return None

    def get_hitstop(self):
        if self.hitstop is None:
            if self.attackLevel is None:
                return None
            else:
                return ATTACK_LEVEL["hitstop"][self.attackLevel]
        return self.hitstop

    def get_untech(self):
        if self.normalHitEffects.untech is not None:
            return self.normalHitEffects.untech

        if self.attackLevel is not None:
            return ATTACK_LEVEL["untech"][self.attackLevel]
        return None

    def get_untech_ch(self):
        fatal_bonus = 3 if self.counterHitEffects.fatal else 0
        if self.counterHitEffects.untech is not None:
            return self.counterHitEffects.untech + fatal_bonus

        if self.attackLevel is not None:
            return self.get_untech() + ATTACK_LEVEL["untechCH"][self.attackLevel] + fatal_bonus

        return None

    def get_stagger(self):
        if self.normalHitEffects.stagger is not None:
            return self.normalHitEffects.stagger

        if self.attackLevel is not None:
            return ATTACK_LEVEL["stagger"][self.attackLevel]
        return None

    def get_stagger_ch(self):
        if self.counterHitEffects.stagger is not None:
            return self.counterHitEffects.stagger

        if self.attackLevel is not None:
            return self.get_stagger() * 2

        return None

    def get_stagger_fall_start(self):
        if self.normalHitEffects.staggerFallStart is not None:
            return self.normalHitEffects.staggerFallStart

        if self.attackLevel is not None:
            return ATTACK_LEVEL["staggerFallStart"][self.attackLevel]
        return None

    def get_stagger_fall_start_ch(self):
        if self.counterHitEffects.staggerFallStart is not None:
            return self.counterHitEffects.staggerFallStart

        if self.get_stagger_fall_start() is not None:
            return int(self.get_stagger_fall_start() * 1.5)

        return None

    def get_corner_stick(self):
        return self.normalHitEffects.cornerStick

    def get_corner_stick_ch(self):
        fatal = 3 if self.counterHitEffects.fatal else 0
        return self.counterHitEffects.cornerStick + fatal

    def get_slide(self):
        if self.normalHitEffects.slide is not None:
            return self.normalHitEffects.slide
        return None

    def get_slide_ch(self):
        fatal_bonus = 3 if self.counterHitEffects.fatal else 0
        if self.counterHitEffects.slide is not None:
            return self.counterHitEffects.slide + fatal_bonus

        return None

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
        if other.blockstun is not None:
            self.blockstun = other.blockstun
        if other.attackLevel is not None:
            self.attackLevel = other.attackLevel
        if other.hitstop is not None:
            self.hitstop = other.hitstop
        if other.bonusBlockstop is not None:
            self.bonusBlockstop = other.bonusBlockstop
        if other.bonusHitstop is not None:
            self.bonusHitstop = other.bonusHitstop
        if other.bonusHitstopCH is not None:
            self.bonusHitstopCH = other.bonusHitstopCH
        if other.attribute is not None:
            self.attribute = other.attribute
        if other.normalHitEffects is not None:
            self.normalHitEffects.override_non_none_values(other.normalHitEffects)
        if other.counterHitEffects is not None:
            self.counterHitEffects.override_non_none_values(other.counterHitEffects)


class HitEffects:
    def __init__(self, hitstun=None, untech=None, ground_hit_ani=None, air_hit_ani=None, knockdown=None,
                 slide_time=None, hitstun_after_wall_bounce=None, stagger=None, ground_bounce=None,
                 ground_bounce_type=None, wall_bounce=None, corner_bounce_type=None,
                 corner_stick=None, stagger_fall_start=None, fatal=None):
        self.hitstun = hitstun
        self.untech = untech
        self.groundHitAni = ground_hit_ani
        self.airHitAni = air_hit_ani
        self.knockdown = knockdown
        self.slide = slide_time
        self.hitstunAfterWallBounce = hitstun_after_wall_bounce
        self.stagger = stagger
        self.staggerFallStart = stagger_fall_start
        self.groundBounce = ground_bounce
        self.groundBounceType = ground_bounce_type
        self.wallBounce = wall_bounce
        self.cornerBounceType = corner_bounce_type
        self.cornerStick = corner_stick
        self.fatal = fatal

    def override_non_none_values(self, other):
        if other.hitstun is not None:
            self.hitstun = other.hitstun
        if other.untech is not None:
            self.untech = other.untech
        if other.groundHitAni is not None:
            self.groundHitAni = other.groundHitAni
        if other.airHitAni is not None:
            self.airHitAni = other.airHitAni
        if other.knockdown is not None:
            self.knockdown = other.knockdown
        if other.slide is not None:
            self.slide = other.slide
        if other.hitstunAfterWallBounce is not None:
            self.hitstunAfterWallBounce = other.hitstunAfterWallBounce
        if other.stagger is not None:
            self.stagger = other.stagger
        if other.staggerFallStart is not None:
            self.staggerFallStart = other.staggerFallStart
        if other.groundBounceType is not None:
            self.groundBounceType = other.groundBounceType
        if other.groundBounce is not None:
            self.groundBounce = other.groundBounce
        if other.wallBounce is not None:
            self.wallBounce = other.wallBounce
        if other.cornerBounceType is not None:
            self.cornerBounceType = other.cornerBounceType
        if other.cornerStick is not None:
            self.cornerStick = other.cornerStick
        if other.fatal is not None:
            self.fatal = other.fatal

    def __eq__(self, other):
        if not isinstance(other, HitEffects):
            return False
        return self.hitstun == other.hitstun and self.untech == other.untech and self.groundHitAni == other.groundHitAni and \
               self.airHitAni == other.airHitAni and self.knockdown == other.knockdown and self.slide == other.slide and \
               self.hitstunAfterWallBounce == other.hitstunAfterWallBounce and self.stagger == other.stagger and \
               self.staggerFallStart == other.staggerFallStart and self.groundBounce == other.groundBounce and \
               self.groundBounceType == other.groundBounceType and self.wallBounce == other.wallBounce and \
               self.cornerBounceType == other.cornerBounceType and self.cornerStick == other.cornerStick and \
               self.fatal == other.fatal


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
        to_return += " Hitstop " + str(self.info.get_hitstop()) + "/+" + str(self.info.bonusBlockstop) + "/+" + str(
            self.info.bonusHitstop)
        return to_return

    def __eq__(self, other):
        if not isinstance(other, ActiveFrames):
            return False
        return self.duration == other.duration and self.is_new_hit == other.is_new_hit and self.info == other.info and \
               self.duration == other.duration and self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

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
    def __init__(self, name, same_thread=False):
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
            self.attackInfo = AttackInfo(normal_hit=HitEffects(), counter_hit=HitEffects())
            self.attackInfo.copy_non_none_values(state.attackInfo)
        else:
            self.landingRecovery = None
            self.attackInfo = AttackInfo(normal_hit=HitEffects(), counter_hit=HitEffects())

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


def simulate_effect_on_block(name, effect_list, start_frame=0):
    if name not in effect_list:
        return []
    subroutine_calls = [[]]
    first_subroutine = subroutine_calls[0]
    duration = start_frame
    override_info = AttackInfo(None)
    if duration > 0:
        first_subroutine.append(WaitFrames(duration))
    for chunk in effect_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = []
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                subroutine = effect_list[chunk.name]
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_info.copy_non_none_values(subroutine.attackInfo)
            else:
                from_children = simulate_effect_on_block(chunk.name, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, ActiveFrames) and override_info is not None:
                chunk.info.override_non_none_values(override_info)

            first_subroutine.append(chunk)
            duration += chunk.duration
            if isinstance(chunk, ActiveFrames):
                duration += chunk.info.get_hitstop() if chunk.info.get_hitstop() is not None else 0

    subroutine_calls[0] = consolidate_frame_chunks(first_subroutine)
    # delete any subroutines that don't add anything
    if start_frame > 0 and len(subroutine_calls[0]) == 1 and isinstance(subroutine_calls[0][0], WaitFrames):
        subroutine_calls.pop(0)
    return subroutine_calls


def simulate_on_block(move_list, effect_list):
    hit_simulations = OrderedDict()
    for moveName in move_list:
        move = move_list[moveName]
        hit_simulations[moveName] = combine_with_effects_on_block(move, effect_list)
    return hit_simulations


def combine_with_effects_on_block(move, effect_list):
    override_info = AttackInfo(None)
    override_landing_recovery = None
    current_frame = 0
    subroutine_calls = []
    main_subroutine = []
    subroutine_calls.append(main_subroutine)
    for idx, chunk in enumerate(move.frame_chunks):
        if isinstance(chunk, SubroutineCall):
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                subroutine = effect_list[chunk.name]
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_info.copy_non_none_values(subroutine.attackInfo)
                override_landing_recovery = subroutine.landingRecovery

            else:
                subroutine_calls.extend(simulate_effect_on_block(chunk.name, effect_list, start_frame=current_frame))
        else:
            if isinstance(chunk, ActiveFrames):
                chunk.info.override_non_none_values(override_info)

            main_subroutine.append(chunk)
            current_frame += chunk.duration
            if isinstance(chunk, ActiveFrames):
                current_frame += 0 if chunk.info.get_hitstop() is None else chunk.info.get_hitstop()
    subroutine_calls[0] = consolidate_frame_chunks(main_subroutine)
    new_move = Move()
    new_move.frame_chunks = subroutine_calls[0]
    new_move.landing_recovery = override_landing_recovery \
        if override_landing_recovery is not None else move.landing_recovery
    new_move.superflash_list = copy.copy(move.superflash_list)
    if len(subroutine_calls) > 1:
        new_move.additional_chunks = subroutine_calls[1:]
    new_move.hardcoded_inv_list = copy.copy(move.hardcoded_inv_list)
    return new_move


def calc_frames_for_subroutine(frame_chunks, superflash_list=None):
    if superflash_list is None:
        superflash_list = []
    startup = 0
    middle = ""
    recovery = 0
    duration_on_whiff = 0
    duration_on_block = 0
    last_frame_of_blockstun = 0

    frame_chunks_ignoring_inv = consolidate_frame_chunks(frame_chunks, True)
    for idx, chunk in enumerate(frame_chunks_ignoring_inv):
        if isinstance(chunk, ActiveFrames):
            if len(middle) > 0 and middle[len(middle) - 1] != ")":
                middle += ","
            middle += str(chunk.duration)
            blockstun = 0 if chunk.info.get_blockstun() is None else chunk.info.get_blockstun()
            hitstop = 0 if chunk.info.get_hitstop() is None else chunk.info.get_hitstop()
            bonus_blockstop = 0 if chunk.info.bonusBlockstop is None else chunk.info.bonusBlockstop
            last_frame_of_blockstun = duration_on_block + blockstun + hitstop + bonus_blockstop + 1
            duration_on_block += hitstop
        elif middle == "":
            startup += chunk.duration
        else:
            if idx < len(frame_chunks_ignoring_inv) - 1:
                middle += "(" + str(chunk.duration) + ")"
            else:
                recovery += chunk.duration

        duration_on_whiff += chunk.duration
        duration_on_block += chunk.duration

    if len(middle) > 0:
        startup += 1
    # determine inv
    inv_list = [[0, 0, [False, False, False, False, False]]]  # duration, type, attributes
    for chunk in frame_chunks:
        if chunk.inv_type == inv_list[-1][1] and chunk.inv_attr == inv_list[-1][2]:
            inv_list[-1][0] += chunk.duration
        else:
            inv_list.append([chunk.duration, chunk.inv_type, chunk.inv_attr])
    # clean up the inv array
    cleaned_inv_list = []
    frame_counter = 1
    for value in inv_list:
        if value[1] != 0:
            cleaned_inv_list.append([frame_counter, value[0], value[1], value[2]])
        frame_counter += value[0]

    # account for superflash
    # TODO: additional logic needed to account for multiple superflashes. For now just use the first one
    for (superflash_start, superflash_duration) in superflash_list:
        total_superfreeze_time = 0
        if superflash_start > 0:
            startup -= superflash_duration
            total_superfreeze_time += superflash_duration
            post_flash_startup = startup - superflash_start
            post_flash_startup = 0 if post_flash_startup < 0 else post_flash_startup
            startup = str(superflash_start) + "+" + str(superflash_duration) + "Flash+" + str(post_flash_startup)
            break

    if middle == "" and recovery == 0:
        recovery = startup
        startup = ""
    return str(startup), middle, str(
        recovery), duration_on_whiff, duration_on_block, last_frame_of_blockstun, cleaned_inv_list


def calc_damage_for_move(move_on_block):
    damage_at_frame = []

    all_frame_chunks = [move_on_block.frame_chunks]
    all_frame_chunks.extend(move_on_block.additional_chunks)
    for frame_chunks in all_frame_chunks:
        current_frame = 0
        for chunk in frame_chunks:
            if isinstance(chunk, ActiveFrames) and chunk.is_new_hit:
                heapq.heappush(damage_at_frame, (current_frame, chunk.info))
                current_frame += 0 if chunk.info.get_hitstop() is None else chunk.info.get_hitstop()
            current_frame += chunk.duration

    damage_list = []
    while len(damage_at_frame) > 0:
        value = heapq.heappop(damage_at_frame)
        damage_list.append(value[1])
        if isinstance(value[1], (int, long)):
            print value

    return damage_list
