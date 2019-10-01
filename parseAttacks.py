import copy
import os
from collections import OrderedDict
import heapq

ATTACK_LEVEL = {"blockstun": [9, 11, 13, 16, 18, 20],
                "hitstun": [10, 12, 14, 17, 19, 21],
                "untech": [12, 12, 14, 17, 19, 21],
                "hitstop": [8, 9, 10, 11, 12, 13],
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
                 air_hit_ani=None, knockdown_time=None, slide_time=None, hitstun_after_wall_bounce=None, wallstick_time=None,
                 crumple_time=None, spin_fall_time=None):
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
        self.knockdownTime = knockdown_time
        self.slideTime = slide_time
        self.hitstunAfterWallBounce = hitstun_after_wall_bounce
        self.wallStickTime = wallstick_time
        self.crumpleTime = crumple_time
        self.spinFallTime = spin_fall_time

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
               self.groundHitAni == other.groundHitAni and self.airHitAni == self.airHitAni

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
    def __init__(self, name):
        Abstract.__init__(self)
        self.name = name

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


SPRITE_START = "    sprite('"
SPRITE_MID = "', "
SPRITE_END = ")"
HAS_HITBOX = "**attackbox here**"
GFX_START = "GFX_0('"
CALL_SUBROUTINE_STARTC = "callSubroutine('"
CALL_SUBROUTINE_STARTc = "CallSubroutine('"


def get_duration(sprite_str):
    number_start = sprite_str.index(SPRITE_MID) + SPRITE_MID.__len__()
    number_end = sprite_str.index(SPRITE_END)
    return int(sprite_str[number_start:number_end])


def parse_attributes(inv_str):
    return [inv_str[1] == "1",
            inv_str[9] == "1",
            inv_str[17] == "1",
            inv_str[25] == "1",
            inv_str[33] == "1"
            ]


def has_same_inv(chunk1, chunk2):
    return chunk1.inv_type == chunk2.inv_type and chunk1.inv_attr == chunk2.inv_attr


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


def parse_move_file(source, move_list, effect_list):
    state = State()
    frame_chunks = []
    for line in source.readlines():
        if state.inUponImmediate and line != '\n' and not line.startswith(state.uponImmediateIndent):
            state.inUponImmediate = False

        # new move, finish parsing existing move, then restart frame counters
        if "@State" in line or "@Subroutine" in line:

            if state.isSubroutine:
                subroutine = Subroutine()
                subroutine.attackInfo.copy_non_none_values(state.attackInfo)
                subroutine.landingRecovery = state.landingRecovery
                effect_list[state.moveName] = subroutine

            elif len(frame_chunks) > 0:
                chunk = ActiveFrames(state.duration, state.isNewHit, copy.copy(state.attackInfo)) \
                    if state.is_attackbox() else WaitFrames(state.duration)
                if state.isInv:
                    chunk.inv_type = 1 if state.invType == 0 else 2
                    chunk.inv_attr = state.invAttr
                frame_chunks.append(chunk)
                move_list[state.moveName] = handle_end_of_move(state, frame_chunks)
            frame_chunks = []
            # print "*** NEW MOVE ***"
            # restart counters
            state.clear_values(True)
            if "@Subroutine" in line:
                state.isSubroutine = True
        elif state.inUponImmediate and line.startswith(state.uponImmediateIndent + "    "):
            pass    # skip anything not under UPON_IMMEDIATE
        elif not state.exitState and SPRITE_START in line:
            if state.duration > 0:
                chunk = ActiveFrames(state.duration, state.isNewHit, copy.copy(state.attackInfo)) \
                    if state.is_attackbox() else WaitFrames(state.duration)
                if state.isInv:
                    chunk.inv_type = 1 if state.invType == 0 else 2
                    chunk.inv_attr = state.invAttr
                frame_chunks.append(chunk)
                if isinstance(chunk, ActiveFrames):
                    state.isNewHit = False
                state.clear_values(False)
            state.duration = get_duration(line)

            if HAS_HITBOX in line:
                state.isAttackBox = HAS_HITBOX in line
        elif not state.exitState:
            if "Recovery()" in line or "Unknown23027()" in line or  "DisableAttackRestOfMove()" in line:  # disables active frames until a refreshMultihit
                state.disableAttackboxes = True
                state.isNewHit = False
            elif "StartMultihit()" in line:  # turns off these active frames
                state.disableAttackboxesThisFrame = True
            elif "RefreshMultihit()" in line:  # counts as a new hit, end previous frames; start a  new one
                state.isNewHit = True
                state.disableAttackboxes = False
            elif "AttackLevel_(" in line:  # get hitstun/blockstun values according to it's level
                level = int(line[line.index("(") + 1:line.index(")")])
                # print "LEVEL: " + level
                state.attackInfo.attackLevel = level
            elif "AttackP1(" in line:
                state.attackInfo.p1 = int(line[line.index("(") + 1:line.index(")")])
            elif "AttackP2(" in line:
                state.attackInfo.p2 = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown9154(" in line or "hitstun(" in line:
                state.attackInfo.hitstun = int(line[line.index("(") + 1:line.index(")")])
            elif "AirUntechableTime(" in line:
                state.attackInfo.untech = int(line[line.index("(") + 1:line.index(")")])
            elif " Damage(" in line or "\tDamage(" in line:
                state.attackInfo.damage = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown11092(" in line:
                state.attackInfo.p2Once = line[line.index("(") + 1:line.index(")")] == "1"
            elif "Unknown11028(" in line or "blockstun(" in line:
                state.attackInfo.blockstun = int(line[line.index("(") + 1:line.index(")")])
                # print "Hardcoded blockstun: " + state.blockstun
            elif "Hitstop(" in line:
                state.attackInfo.hitstop = int(line[line.index("(") + 1:line.index(")")])
                # print "Hardcoded hitstop: " + state.hitstop
            elif "def " in line and len(state.moveName) < 1:
                name_start = line.index("def ") + len(SPRITE_MID) + 1
                name_end = line.index("()")
                state.moveName = line[name_start:name_end]
            elif "Unknown11001(" in line:
                numbers_start = line.index("(") + 1
                numbers_end = line.index(")")
                numbers = [x.strip() for x in line[numbers_start:numbers_end].split(',')]
                state.attackInfo.bonus_blockstop = int(numbers[0])
                state.attackInfo.bonus_hitstop = int(numbers[1])
            elif "Unknown22004(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(",")
                # print "Landing" + line[number_start: number_end]
                state.landingRecovery = int(line[number_start: number_end]) - 1
            elif GFX_START in line:
                name_start = line.index("('") + 2
                name_end = line.index("',")
                # print "GFX " + line[name_start:name_end]
                frame_chunks.append(SubroutineCall(line[name_start:name_end]))
                # run the command on line[name_start:name_end] starting at current_frame-1
            elif CALL_SUBROUTINE_STARTC in line or CALL_SUBROUTINE_STARTc in line:
                name_start = line.index("('") + 2
                name_end = line.index("')")
                # run the command on line[name_start:name_end] starting at current_frame-1
                # print "SUBROUTINE" + line[name_start:name_end]
                if state.inUponImmediate:
                    if line[name_start:name_end] in effect_list:
                        subroutine = effect_list[line[name_start:name_end]]
                        state.attackInfo.copy_non_none_values(subroutine.attackInfo)
                        state.landingRecovery = subroutine.landingRecovery
                else:
                    frame_chunks.append(SubroutineCall(line[name_start:name_end]))
            elif "AirHitstunAnimation(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.airHitAni = int(line[number_start:number_end])
            elif "GroundedHitstunAnimation(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.groundHitAni = int(line[number_start:number_end])
            elif "Unknown2036(" in line:
                flash_start = line.index("(") + 1
                flash_end = line.index(",")
                superflash_start = 1
                for chunk in frame_chunks:
                    if isinstance(chunk, AbstractFrames):
                        superflash_start += chunk.duration
                superflash_duration = int(line[flash_start:flash_end])
                state.superflash_list.append((superflash_start, superflash_duration))
                # superfreeze
            elif "Unknown22019(" in line:
                # set invul to which attributes
                params = line[line.index("('") + 2: line.index("')")]
                state.invAttr = parse_attributes(params)
            elif "Unknown11058(" in line:
                params = line[line.index("('") + 2: line.index("')")]
                state.attackInfo.attribute = parse_attributes(params)
            elif "setInvincible(" in line:
                # active/deactivate invul
                idx = line.index("(") + 1
                state.isInv = line[idx: idx + 1] == "1"
            elif "Unknown22008(" in line:
                inv_start = line.index("(") + 1
                inv_end = line.index(")")
                hardcoded_inv_start = 1
                for chunk in frame_chunks:
                    if isinstance(chunk, AbstractFrames):
                        hardcoded_inv_start += chunk.duration
                hardcoded_inv_duration = int(line[inv_start:inv_end])
                state.hardcodedInvList.append((hardcoded_inv_start, hardcoded_inv_duration, state.invType, state.invAttr))
            elif "GuardPoint_(" in line:
                idx = line.index("(") + 1
                state.invType = int(line[idx: idx + 1])
            elif "ExitState()" in line:
                # we assume all the lines above this are for the move on block/whiff. Anything after is on hit
                state.exitState = True
            elif "Unknown17025(" in line or "Unknown17024(" in line:  # i think this is attackDefaultsReversalAction()
                state.invType = 0
                state.isInv = True
            elif "Unknown30072(" in line:  # i think this is attackDefaults5C()? Basically Attack Level 3
                state.attackInfo.attackLevel = 3
                state.attackInfo.bonus_hitstop = 0
                state.attackInfo.bonus_blockstop = 0
            elif "AttackDefaults_StandingNormal(" in line:
                state.attackInfo.attribute = [False, True, False, False, False]
            elif "AttackDefaults_StandingSpecial(" in line:
                state.attackInfo.p1 = 80
                state.attackInfo.attribute = [False, True, False, False, False]
            elif "AttackDefaults_CrouchingNormal(" in line:
                state.attackInfo.attribute = [False, False, True, False, False]
            elif "AttackDefaults_AirNormal(" in line:
                state.attackInfo.p1 = 80
                state.attackInfo.attribute = [True, False, False, False, False]
            elif "Unknown17003(" in line: # attack defaults air special?
                state.attackInfo.p1 = 80
                state.attackInfo.attribute = [True, False, False, False, False]
            elif "Unknown17024(" in line: # attack defaults reversal action
                state.attackInfo.p1 = 80
                state.attackInfo.p2 = 60
                state.attackInfo.attribute = [True, False, False, False, False]
            elif "def upon_IMMEDIATE():" in line:
                state.inUponImmediate = True
                state.uponImmediateIndent = line[0:line.index("def")] + "    "
    if state.isSubroutine:
        subroutine = Subroutine()
        subroutine.attackInfo.copy_non_none_values(state.attackInfo)
        subroutine.landingRecovery = state.landingRecovery
        effect_list[state.moveName] = subroutine

    elif state.duration > 0:
        attack_info = copy.copy(state.attackInfo)
        attack_info.blockstun = 0 if attack_info.blockstun is None else attack_info.blockstun
        attack_info.hitstop = 0 if attack_info.hitstop is None else attack_info.hitstop
        attack_info.bonus_blockstop = 0 if attack_info.bonus_blockstop is None else attack_info.bonus_blockstop
        attack_info.bonus_hitstop = 0 if attack_info.bonus_hitstop is None else attack_info.bonus_hitstop
        chunk = ActiveFrames(state.duration,
                             state.isNewHit,
                             attack_info) \
            if state.is_attackbox() else WaitFrames(state.duration)
        if state.isInv:
            chunk.inv_type = 1 if state.invType == 0 else 2
            chunk.inv_attr = state.invAttr

        frame_chunks.append(chunk)

        move_list[state.moveName] = handle_end_of_move(state, frame_chunks)

    return move_list


def handle_end_of_move(state, frame_chunks):
    new_move = Move()
    new_move.frame_chunks = consolidate_frame_chunks(frame_chunks)
    if state.landingRecovery > 0:
        new_move.landing_recovery = state.landingRecovery
    if len(state.superflash_list) > 0:
        new_move.superflash_list = copy.copy(state.superflash_list)
    new_move.hardcoded_inv_list = copy.copy(state.hardcodedInvList)
    return new_move


def find_registered_moves(source):
    registered_moves = []
    for line in source.readlines():
        if "Move_Register(" in line:
            name_start = line.index("('") + 2
            name_end = line.index("',")
            name = line[name_start:name_end]
            registered_moves.append(name)

    return registered_moves


def parse_subroutine(name, move_list, effect_list, start_frame=0):
    if name not in move_list:
        return []
    subroutine_calls = [[]]
    first_subroutine = subroutine_calls[0]
    duration = start_frame
    override_info = AttackInfo()
    if duration > 0:
        first_subroutine.append(WaitFrames(duration))
    for chunk in move_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = []
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                subroutine = effect_list[chunk.name]
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_info = subroutine.attackInfo
            else:
                from_children = parse_subroutine(chunk.name, effect_list, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, ActiveFrames):
                chunk.info.override_non_none_values(override_info)

            first_subroutine.append(chunk)
            duration += chunk.duration

    subroutine_calls[0] = consolidate_frame_chunks(first_subroutine)
    # delete any subroutines that don't add anything
    if len(subroutine_calls[0]) == 1 and isinstance(subroutine_calls[0][0], WaitFrames):
        subroutine_calls.pop(0)
    return subroutine_calls


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


def calc_frames_for_subroutine(frame_chunks, superflash_list=[]):
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
            bonus_blockstop = 0 if chunk.info.bonus_blockstop is None else chunk.info.bonus_blockstop
            last_frame_of_blockstun = duration_on_block + blockstun + hitstop + \
                                      bonus_blockstop + 1
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
    return str(startup), middle, str(recovery), duration_on_whiff, duration_on_block, last_frame_of_blockstun, cleaned_inv_list


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


def write_file(moves_on_block, target):
    for moveName in moves_on_block:
        move_on_block = moves_on_block[moveName]

        target.write("\n" + moveName + "\n")
        startup, middle, recovery, total_duration, duration_on_block, last_blockstun_frame, inv_list  = \
            calc_frames_for_subroutine(move_on_block.frame_chunks,
                                       move_on_block.superflash_list)
        subroutine_block_timelines = []
        for subroutine in move_on_block.additional_chunks:
            result = calc_frames_for_subroutine(subroutine,
                                                move_on_block.superflash_list)
            subroutine_block_timelines.append(result)
        if startup is "":
            recovery = "Total: " + str(recovery)
        else:
            recovery = str(recovery)

        if move_on_block.landing_recovery > 0:
            recovery += "+" + str(move_on_block.landing_recovery) + "L"
        # target.write("\n\tduration on block: " + str(duration_on_block))
        if len(subroutine_block_timelines) > 0:
            for result in subroutine_block_timelines:
                last_blockstun_frame = result[5] if result[5] > last_blockstun_frame else last_blockstun_frame
                # target.write("\n\tstartup: " + str(result[0]))
                target.write("\nAdditional Hit (projectile?)\n|startup=" + str(result[0]) + "|active=" + result[1] + "|recovery=" + str(result[2]))
                target.write("last blockstun frame: " + str(last_blockstun_frame))

        inv_text = ""
        for inv in move_on_block.hardcoded_inv_list:
            inv_list.append(inv)
        for idx, inv in enumerate(inv_list):
            inv_text = get_inv_text(inv[0], inv[1], inv[2], inv[3],
                                    move_on_block.superflash_list
                                    )
            if idx != len(inv_list) - 1:
                inv_text += "<br/>"
        frame_adv = ""
        if last_blockstun_frame != 0:
            frame_adv = str(last_blockstun_frame-duration_on_block)
            # target.write("\n\tlast blockstun: " + str(last_blockstun_frame))
            # target.write("|frameAdv=" + str(last_blockstun_frame - duration_on_block))
        damage_list = calc_damage_for_move(move_on_block)
        damage, p1, p2, hitstun, untech, level, attribute, hitstop, blockstun = create_damage_text(damage_list)

        target.write("\n |damage=" + damage + "|cancel=" + "|p1=" + p1 + "|p2=" + p2)
        target.write("\n |level=" + level + "|attribute=" + attribute + "|guard=")
        target.write("\n |startup=" + str(startup) + "|active=" + middle + "|recovery=" + recovery + "|frameAdv=" + frame_adv)
        target.write("\n |blockstun=" + blockstun + "|groundHit=" + hitstun + "|airHit=" + untech + "|hitstop=" + hitstop)
        target.write("\n |invul=" + inv_text + "|hitbox=")
        target.write("\n}}\n")


def get_inv_text(inv_start, inv_duration, inv_type, inv_attr, superflash_list):
    inv_type = " Guard" if inv_type == 2 else ""
    inv_attr = get_inv_attr_text(inv_attr)

    inv_end = inv_start + inv_duration - 1
    # TODO: any additional logic needed to account for multiple superflashes in one move?
    for (superflash_start, superflash_duration) in superflash_list:
        if superflash_start is not None:
            if inv_start > superflash_start:
                inv_start -= superflash_duration

            if inv_end > superflash_start:
                inv_end -= superflash_duration
            if inv_end < inv_start:
                inv_end = superflash_start
    return str(inv_start) + "-" + str(inv_end) + " " + inv_attr + inv_type


def get_inv_attr_text(attr):
    return_value = ""
    if attr is None:
        return return_value
    if attr[0] and attr[1] and attr[2] and attr[3] and attr[4]:
        return_value = "All"
    else:
        if attr[0]:
            return_value += "H"
        if attr[1]:
            return_value += "B"
        if attr[2]:
            return_value += "F"
        if attr[3]:
            return_value += "P"
        if attr[4]:
            return_value += "T"
    return return_value


def create_damage_text(damage_list):
    # damage, p1, p2, hitstun, untech, level, attribute, blockstun. Hitstop is calculated separately
    value_str = ["" for i in range(8)]
    value_multiplier = [1 for i in range(8)]
    value = [None for i in range(8)]
    p2Once = None

    if len(damage_list) == 0:
        value_str.append("")
        return value_str

    for item in damage_list:
        fill_str(item.get_damage(), 0, value, value_str, value_multiplier)
        fill_str(item.get_p1(), 1, value, value_str, value_multiplier)
        fill_str(item.get_p2(), 2, value, value_str, value_multiplier)
        fill_str(item.get_hitstun(), 3, value, value_str, value_multiplier)
        fill_str(item.get_untech(), 4, value, value_str, value_multiplier)
        fill_str(item.attackLevel, 5, value, value_str, value_multiplier)
        fill_str(get_inv_attr_text(item.attribute), 6, value, value_str, value_multiplier)
        fill_str(item.get_blockstun(), 7, value, value_str, value_multiplier)
        p2Once = item.p2Once

    for i in range(len(value_str)):
        if value[i] is not None:
            value_str[i] = value_str[i] + str(value[i])
            if value_multiplier[i] > 1:
                value_str[i] = value_str[i] + "*" + str(value_multiplier[i])

    if p2Once:
        value_str[2] = value_str[2] + " (Once)"

    hitstop_str = fill_hitstop(damage_list)

    return value_str[0], value_str[1], value_str[2], value_str[3], value_str[4], value_str[5], value_str[6], \
           hitstop_str, value_str[7]


def fill_str(new_value, index, current_value, value_str, multiplier):
    if current_value[index] == new_value:
        multiplier[index] = multiplier[index] + 1
    elif current_value[index] is not None:
        value_str[index] = value_str[index] + str(current_value[index])
        if multiplier[index] > 1:
            value_str[index] = value_str[index] + "*" + str(multiplier[index])
            multiplier[index] = 1  # reset multiplier
        value_str[index] = value_str[index] + ", "
    current_value[index] = new_value


def fill_hitstop(info_list):
    to_return = ""
    current_hitstop = None
    current_bonus_blockstop = None
    current_bonus_hitstop = None
    multiplier = 0
    for i, info in enumerate(info_list):
        if i == 0:
            current_hitstop = info.hitstop
            current_bonus_blockstop = info.bonus_blockstop
            current_bonus_hitstop = info.bonus_hitstop
            multiplier = 1
        elif current_hitstop == info.hitstop and current_bonus_blockstop == info.bonus_blockstop and \
                current_bonus_hitstop == info.bonus_hitstop:
            multiplier = multiplier + 1
        else:
            if len(to_return) > 0:
                to_return = to_return + ", "
            to_return = to_return + str(current_hitstop)
            if current_bonus_blockstop is not None and (current_bonus_hitstop != 0 or current_bonus_blockstop != 0):
                to_return = to_return + "/"
                if current_bonus_blockstop > -1:
                    to_return = to_return + "+"
                to_return = to_return + str(current_bonus_blockstop)
            if current_bonus_hitstop is not None and current_bonus_hitstop != 0:
                to_return = to_return + "/"
                if current_bonus_hitstop > -1:
                    to_return = to_return + "+"
                to_return = to_return + str(current_bonus_hitstop)
            current_hitstop = info.hitstop
            current_bonus_blockstop = info.bonus_blockstop
            current_bonus_hitstop = info.bonus_hitstop
            multiplier = 1

    if len(to_return) > 0:
        to_return = to_return + ", "
    to_return = to_return + str(current_hitstop)
    if current_bonus_blockstop is not None and (current_bonus_hitstop != 0 or current_bonus_blockstop != 0):
        to_return = to_return + "/"
        if current_bonus_blockstop > -1:
            to_return = to_return + "+"
        to_return = to_return + str(current_bonus_blockstop)
    if current_bonus_hitstop is not None and current_bonus_hitstop != 0:
        to_return = to_return + "/"
        if current_bonus_hitstop > -1:
            to_return = to_return + "+"
        to_return = to_return + str(current_bonus_hitstop)

    return to_return


def main():
    source_dir = "./annotated"
    target_dir = "./parsedAttacks"
    file_list = [
        # Arcana Heart
        "scr_ahe",
        # BlazBlue
        "scr_baz", "scr_bes", "scr_bha", "scr_bhz", "scr_biz", "scr_bjb", "scr_bjn", "scr_bma", "scr_bmk",
        "scr_bno", "scr_bnt", "scr_bny", "scr_bph", "scr_bpt", "scr_brc", "scr_brg", "scr_btg",
        # Persona
        "scr_pag", "scr_pak", "scr_pbc", "scr_pce", "scr_pka", "scr_pku", "scr_pla", "scr_pmi", "scr_pna",
        "scr_pyo", "scr_pyu",
        # RWBY
        "scr_rbl", "scr_rrb", "scr_rwi", "scr_ryn",
        # Under Night
        "scr_uca", "scr_ugo", "scr_uhy", "scr_uli", "scr_ume", "scr_umi", "scr_uor", "scr_use", "scr_uva",
        "scr_uwa", "scr_uyu"
    ]

    # source_dir = "."
    # target_dir = "."
    # file_list = ["testfile"]
    for file_name in file_list:
        # Parse effects
        if not os.path.isfile(source_dir + "/" + file_name + "ea.py") or \
                not os.path.isfile(source_dir + "/" + file_name + ".py"):
            print "file" + source_dir + "/" + file_name + "ea.py or " + \
                  file_name + ".py does not exist"
            continue
        effect_source = open(source_dir + "/" + file_name + "ea.py", "r")
        effect_list = OrderedDict()
        effect_list = parse_move_file(effect_source, effect_list, effect_list)
        # Parse moves
        char_source = open(source_dir + "/" + file_name + ".py", "r")
        char_target = open(target_dir + "/" + file_name + "_out.txt", "w")
        move_list = OrderedDict()
        move_list = parse_move_file(char_source, move_list, effect_list)

        # get list of registered moves
        char_source.seek(0, 0)
        registered_moves = find_registered_moves(char_source)
        # remove all non-registered moves, like all the Act* and Event* stuff
        for move_name in move_list.keys():
            if move_name not in registered_moves and "Exe" not in move_name and \
                    "ChangePartner" not in move_name and \
                    "CmnActChangePartner" not in move_name:
                del move_list[move_name]

        hit_simulations = simulate_on_block(move_list, effect_list)

        write_file(hit_simulations, char_target)
        print "DONE with " + file_name


if __name__ == "__main__":
    main()
