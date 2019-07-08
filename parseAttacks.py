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
        self.moveName = ""
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        self.disableAttackboxes = False
        self.disableAttackboxesThisFrame = False
        self.isNewHit = True
        self.blockstun = None
        self.hitstun = None
        self.untech = None
        self.hitstop = None
        self.bonus_blockstop = None
        self.bonus_hitstop = None
        self.exitState = False
        self.landingRecovery = 0
        self.isSubroutine = False
        self.damage = None
        self.p1 = None
        self.p2 = None
        self.p2Once = False
        self.minDamage = 0
        self.isInv = False
        self.invType = 0  # Inv or Guard
        self.invAttr = [True, True, True, True, True]  # Head, Body, Foot, Proj, Throw
        self.superflash_start = None
        self.superflash_duration = 0
        self.attackLevel = None
        self.attr = [False, False, False, False, False]

    def clear_values(self, is_new_move):
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        self.disableAttackboxesThisFrame = False
        if is_new_move:
            self.moveName = ""
            self.disableAttackboxes = False
            self.isNewHit = True
            self.blockstun = None
            self.hitstun = None
            self.untech = None
            self.hitstop = None
            self.bonus_blockstop = None
            self.bonus_hitstop = None
            self.exitState = False
            self.landingRecovery = 0
            self.isSubroutine = False
            self.damage = None
            self.p1 = None
            self.p2 = None
            self.p2Once = False
            self.minDamage = 0
            self.isInv = False
            self.invType = 0  # Inv or Guard
            self.invAttr = [True, True, True, True, True]  # Head, Body, Foot, Proj, Throw
            self.attr = [False, False, False, False, False]
            self.superflash_start = None
            self.superflash_duration = 0
            self.attackLevel = None

    def is_attackbox(self):
        return self.isAttackBox and (self.isNewHit or not (self.disableAttackboxes or self.disableAttackboxesThisFrame))


class AttackInfo:
    def __init__(self, damage, p1=None, p2=None, min_damage=None, p2once=None, hitstun=None, untech=None, blockstun=None,
                 hitstop=None, bonus_blockstop=None, bonus_hitstop=None, attackLevel=None, attribute=None):
        self.damage = damage
        self.p1 = p1
        self.p2 = p2
        self.minDamage = min_damage
        self.p2Once = p2once
        self.hitstun = hitstun
        self.untech = untech
        self.blockstun = blockstun
        self.attackLevel = attackLevel
        self.hitstop = hitstop
        self.bonus_blockstop = bonus_blockstop    # for additional hitstop the opponent experiences on block
        self.bonus_hitstop = bonus_hitstop       # for additonoal hitstop the opponent experiences on hit
        self.attribute = copy.copy(attribute)

    def __str__(self):
        toReturn = "damage=" + str(self.damage) + "p1=" + str(self.p1) + "p2=" + str(self.p2)
        if self.p2Once:
            toReturn = toReturn + "(once)"
        toReturn = toReturn + "minDamage=" + str(self.minDamage) + "attackLv=" + str(self.attackLevel) + \
                   "attr=" + str(self.attribute) + "blockstun=" + str(self.blockstun) + "hitstun=" + str(self.hitstun) + \
                   "untech=" + str(self.untech) + "hitstop=" + str(self.hitstop) + "bonusHitstop=" + str(self.bonus_blockstop)
        return toReturn

    def __eq__(self, other):
        if not isinstance(other, AttackInfo):
            return False
        return self.damage == other.damage and self.p1 == other.p1 and self.p2 == other.p2 and \
               self.minDamage == other.minDamage and self.p2Once == other.p2Once and self.blockstun == other.blockstun and \
               self.hitstun == other.hitstun and self.untech == other.untech and self.attackLevel == other.attackLevel and \
               self.hitstop == other.hitstop and self.bonus_blockstop == other.bonus_blockstop and \
               self.bonus_hitstop == other.bonus_hitstop and self.attribute == other.attribute

    def __ne__(self, other):
        if not isinstance(other, AttackInfo):
            return False
        return not self.__eq__(other)

    def override_values(self, other):
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
        to_return += " Blockstun " + str(self.info.blockstun)
        to_return += " Hitstop " + str(self.info.hitstop) + "/+" + str(self.info.bonus_blockstop) + "/+" + str(self.info.bonus_hitstop)
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
        self.superflash_start = None
        self.superflash_duration = 0

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
        return self.landing_recovery == other.landing_recovery and self.superflash_start == other.superflash_start and \
            self.superflash_duration == self.superflash_duration

    def __ne__(self, other):
        if not isinstance(other, Move):
            return False
        return not self.__eq__(other)


class Subroutine:
    def __init__(self):
        self.damage = None
        self.blockstun = None
        self.hitstop = None
        self.bonus_blockstop = None
        self.bonus_hitstop = None
        self.landingRecovery = None
        self.p1 = None
        self.p2 = None
        self.p2Once = None
        self.minDamage = None
        self.attackLevel = None
        self.hitstun = None
        self.untech = None

    def __eq__(self, other):
        if not isinstance(other, Subroutine):
            return False
        return self.damage == other.damage and self.p1 == other.p1 and self.p2 == other.p2 and \
               self.p2Once == other.p2Once and self.minDamage == other.minDamage and \
               self.blockstun == other.blockstun and \
               self.hitstop == other.hitstop and \
               self.bonus_blockstop == other.bonus_blockstop and \
               self.bonus_hitstop == other.bonus_hitstop and \
               self.landingRecovery == other.landingRecovery and \
               self.attackLevel == other.attackLevel and \
               self.hitstun == other.hitstun and \
               self.untech == other.untech

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


def create_damage_info_from_state(state):
    damage = 0 if state.damage is None else state.damage
    p1 = 100 if state.p1 is None else state.p1
    p2 = 100 if state.p2 is None else state.p2
    p2Once = False if state.p2Once is None else state.p2Once
    minDamage = 0 if state.minDamage is None else state.minDamage
    hitstun = 0 if state.hitstun is None else state.hitstun
    untech = 0 if state.untech is None else state.untech
    blockstun = 0 if state.blockstun is None else state.blockstun
    hitstop = 0 if state.hitstop is None else state.hitstop
    bonus_blockstop = 0 if state.bonus_blockstop is None else state.bonus_blockstop
    bonus_hitstop = 0 if state.bonus_hitstop is None else state.bonus_hitstop
    attackLevel = 0 if state.attackLevel is None else state.attackLevel

    return AttackInfo(damage, p1, p2, minDamage, p2Once, hitstun, untech, blockstun, hitstop, bonus_blockstop=bonus_blockstop,
                      bonus_hitstop=bonus_hitstop, attribute=state.attr, attackLevel=attackLevel)


def parse_move_file(source, move_list, effect_list):
    state = State()
    frame_chunks = None
    for line in source.readlines():
        # new move, finish parsing existing move, then restart frame counters
        if "@State" in line or "@Subroutine" in line:

            if state.isSubroutine:
                subroutine = Subroutine()
                subroutine.attackLevel = state.attackLevel
                if state.attackLevel is not None:
                    subroutine.blockstun = ATTACK_LEVEL["blockstun"][state.attackLevel]
                    subroutine.hitstop = ATTACK_LEVEL["hitstop"][state.attackLevel]
                    subroutine.p1 = ATTACK_LEVEL["p1"][state.attackLevel]
                    subroutine.p2 = ATTACK_LEVEL["p2"][state.attackLevel]
                    subroutine.damage = ATTACK_LEVEL["damage"][state.attackLevel]
                    subroutine.hitstun = ATTACK_LEVEL["hitstun"][state.attackLevel]
                    subroutine.untech = ATTACK_LEVEL["untech"][state.attackLevel]

                subroutine.blockstun = state.blockstun if state.blockstun is not None else subroutine.blockstun
                subroutine.hitstop = state.hitstop if state.hitstop is not None else subroutine.hitstop
                subroutine.bonus_blockstop = state.bonus_blockstop if state.bonus_blockstop is not None else subroutine.bonus_blockstop
                subroutine.damage = state.damage if state.damage is not None else subroutine.damage
                subroutine.p1 = state.p1 if state.p1 is not None else subroutine.p1
                subroutine.p2 = state.p2 if state.p2 is not None else subroutine.p2
                subroutine.p2Once = state.p2Once if state.p2Once is not None else subroutine.p2Once
                effect_list[state.moveName] = subroutine

            elif frame_chunks is not None and len(frame_chunks) > 0:
                blockstun = 0 if state.blockstun is None else state.blockstun
                hitstop = 0 if state.hitstop is None else state.hitstop
                bonus_blockstop = 0 if state.bonus_blockstop is None else state.bonus_blockstop
                chunk = ActiveFrames(state.duration, state.isNewHit, create_damage_info_from_state(state)) \
                    if state.is_attackbox() else WaitFrames(state.duration)
                if state.isInv:
                    chunk.inv_type = 1 if state.invType == 0 else 2
                    chunk.inv_attr = state.invAttr
                frame_chunks.append(chunk)

                move_list[state.moveName] = Move()
                move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
                if state.landingRecovery > 0:
                    move_list[state.moveName].landing_recovery = state.landingRecovery
                if state.superflash_start is not None:
                    move_list[state.moveName].superflash_start = state.superflash_start
                    move_list[state.moveName].superflash_duration = state.superflash_duration
            frame_chunks = []
            # print "*** NEW MOVE ***"
            # restart counters
            state.clear_values(True)
            if "@Subroutine" in line:
                state.isSubroutine = True
        elif line.startswith("            "):
            pass    # skip anything not under UPON_IMMEDIATE
        elif not state.exitState and SPRITE_START in line:
            if state.duration > 0:
                blockstun = 0 if state.blockstun is None else state.blockstun
                hitstop = 0 if state.hitstop is None else state.hitstop
                bonus_blockstop = 0 if state.bonus_blockstop is None else state.bonus_blockstop

                chunk = ActiveFrames(state.duration, state.isNewHit, create_damage_info_from_state(state)) \
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
            if "Recovery()" in line or "Unknown23027()" in line:  # disables active frames until a refreshMultihit
                state.disableAttackboxes = True
            elif "StartMultihit()" in line:  # turns off these active frames
                state.disableAttackboxesThisFrame = True
            elif "RefreshMultihit()" in line:  # counts as a new hit, end previous frames; start a  new one
                state.isNewHit = True
            elif "AttackLevel_(" in line:  # get hitstun/blockstun values according to it's level
                level = int(line[line.index("(") + 1:line.index(")")])
                # print "LEVEL: " + level
                state.blockstun = ATTACK_LEVEL["blockstun"][level]
                state.hitstop = ATTACK_LEVEL["hitstop"][level]
                state.p1 = ATTACK_LEVEL["p1"][level]
                state.p2 = ATTACK_LEVEL["p2"][level]
                state.damage = ATTACK_LEVEL["damage"][level]
                state.hitstun = ATTACK_LEVEL["hitstun"][level]
                state.untech = ATTACK_LEVEL["untech"][level]
                state.attackLevel = level
            elif "AttackP1(" in line:
                state.p1 = int(line[line.index("(") + 1:line.index(")")])
            elif "AttackP2(" in line:
                state.p2 = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown9154(" in line:
                state.hitstun = int(line[line.index("(") + 1:line.index(")")])
            elif "AirUntechableTime(" in line:
                state.untech = int(line[line.index("(") + 1:line.index(")")])
            elif " Damage(" in line or "\tDamage(" in line:
                state.damage = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown11092(" in line:
                state.p2Once = line[line.index("(") + 1:line.index(")")] == "1"
            elif "Unknown11028(" in line:
                state.blockstun = int(line[line.index("(") + 1:line.index(")")])
                # print "Hardcoded blockstun: " + state.blockstun
            elif "Hitstop(" in line:
                state.hitstop = int(line[line.index("(") + 1:line.index(")")])
                # print "Hardcoded hitstop: " + state.hitstop
            elif "def " in line and len(state.moveName) < 1:
                name_start = line.index("def ") + len(SPRITE_MID) + 1
                name_end = line.index("()")
                state.moveName = line[name_start:name_end]
            elif "Unknown11001(" in line:
                numbers_start = line.index("(") + 1
                numbers_end = line.index(")")
                numbers = [x.strip() for x in line[numbers_start:numbers_end].split(',')]
                state.bonus_blockstop = int(numbers[0])
                state.bonus_hitstop = int(numbers[1])
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
                frame_chunks.append(SubroutineCall(line[name_start:name_end]))
            elif "Unknown2036(" in line:
                flash_start = line.index("(") + 1
                flash_end = line.index(",")
                state.superflash_start = 1
                for chunk in frame_chunks:
                    if isinstance(chunk, AbstractFrames):
                        state.superflash_start += chunk.duration
                state.superflash_duration = int(line[flash_start:flash_end])
                # superfreeze
            elif "Unknown22019(" in line:
                # set invul to which attributes
                params = line[line.index("('") + 2: line.index("')")]
                state.invAttr = parse_attributes(params)
            elif "Unknown11058(" in line:
                params = line[line.index("('") + 2: line.index("')")]
                state.attr = parse_attributes(params)
            elif "setInvincible(" in line:
                # active/deactivate invul
                idx = line.index("(") + 1
                state.isInv = line[idx: idx + 1] == "1"
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
                state.attackLevel = 3
                state.blockstun = 16
                state.hitstop = 11
            elif "AttackDefaults_StandingNormal(" in line or "AttackDefaults_StandingSpecial(" in line:
                state.attr = [False, True, False, False, False]
            elif "AttackDefaults_CrouchingNormal(" in line:
                state.attr = [False, False, True, False, False]
            elif "AttackDefaults_AirNormal(" in line:
                state.attr = [True, False, False, False, False]
            elif "Unknown17003(" in line: # attack defaults air special?
                state.attr = [True, False, False, False, False]
    if state.isSubroutine:
        subroutine = Subroutine()
        subroutine.blockstun = state.blockstun
        subroutine.hitstop = state.hitstop
        subroutine.bonus_blockstop = state.bonus_blockstop
        subroutine.bonus_hitstop = state.bonus_hitstop
        subroutine.damage = state.damage
        subroutine.p1 = state.p1
        subroutine.p2 = state.p2
        subroutine.p2Once = state.p2Once
        subroutine.attackLevel = state.attackLevel
        effect_list[state.moveName] = subroutine

    elif state.duration > 0:
        blockstun = 0 if state.blockstun is None else state.blockstun
        hitstop = 0 if state.hitstop is None else state.hitstop
        bonus_hitstop = 0 if state.bonus_blockstop is None else state.bonus_blockstop
        bonus_blockstop = 0 if state.bonus_hitstop is None else state.bonus_hitstop
        chunk = ActiveFrames(state.duration,
                             state.isNewHit,
                             create_damage_info_from_state(state)) \
            if state.is_attackbox() else WaitFrames(state.duration)
        if state.isInv:
            chunk.inv_type = 1 if state.invType == 0 else 2
            chunk.inv_attr = state.invAttr

        frame_chunks.append(chunk)

        move_list[state.moveName] = Move()
        move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
        if state.landingRecovery > 0:
            move_list[state.moveName].landing_recovery = state.landingRecovery
        if state.superflash_start is not None:
            move_list[state.moveName].superflash_start = state.superflash_start
            move_list[state.moveName].superflash_duration = state.superflash_duration

    return move_list


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
                override_info.damage = subroutine.damage
                override_info.p1 = subroutine.p1
                override_info.p2 = subroutine.p2
                override_info.minDamage = subroutine.minDamage
                override_info.p2Once = subroutine.p2Once
                override_info.hitstun = subroutine.hitstun
                override_info.untech = subroutine.untech
                override_info.blockstun = subroutine.blockstun
                override_info.hitstop = subroutine.hitstop
                override_info.bonus_blockstop = subroutine.bonus_blockstop
                override_info.bonus_hitstop = subroutine.bonus_hitstop
                override_info.attackLevel = subroutine.attackLevel
            else:
                from_children = parse_subroutine(chunk.name, effect_list, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, ActiveFrames):
                chunk.info.override_values(override_info)

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
                override_info.damage = subroutine.damage
                override_info.p1 = subroutine.p1
                override_info.p2 = subroutine.p2
                override_info.minDamage = subroutine.minDamage
                override_info.p2Once = subroutine.p2Once
                override_info.hitstun = subroutine.hitstun
                override_info.untech = subroutine.untech
                override_info.blockstun = subroutine.blockstun
                override_info.hitstop = subroutine.hitstop
                override_info.bonus_blockstop = subroutine.bonus_blockstop
                override_info.bonus_hitstop = subroutine.bonus_hitstop
                override_info.attackLevel = subroutine.attackLevel
            else:
                from_children = simulate_effect_on_block(chunk.name, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, ActiveFrames) and override_info is not None:
                chunk.info.override_values(override_info)

            first_subroutine.append(chunk)
            duration += chunk.duration
            if isinstance(chunk, ActiveFrames):
                duration += chunk.info.hitstop if chunk.info.hitstop is not None else 0

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


def calc_frames_for_subroutine(frame_chunks, superflash_start=None, superflash_duration=0):
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
            blockstun = 0 if chunk.info.blockstun is None else chunk.info.blockstun
            hitstop = 0 if chunk.info.hitstop is None else chunk.info.hitstop
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
    cleaned_list = []
    frame_counter = 1
    for value in inv_list:
        if value[1] != 0:
            cleaned_list.append([frame_counter, value[0], value[1], value[2]])
        frame_counter += value[0]

    # account for superflash
    if superflash_start > 0:
        startup -= superflash_duration
        post_flash_startup = startup - superflash_start
        post_flash_startup = 0 if post_flash_startup < 0 else post_flash_startup
        startup = str(superflash_start) + "+" + str(superflash_duration) + "Flash+" + str(post_flash_startup)
    else:
        startup = str(startup)

    if middle == "" and recovery == 0:
        recovery = startup
        startup = ""
    return startup, middle, str(recovery), duration_on_whiff, duration_on_block, last_frame_of_blockstun, cleaned_list


def calc_damage_for_move(move_on_block):
    damage_at_frame = []

    all_frame_chunks = [move_on_block.frame_chunks]
    all_frame_chunks.extend(move_on_block.additional_chunks)
    for frame_chunks in all_frame_chunks:
        current_frame = 0
        for chunk in frame_chunks:
            if isinstance(chunk, ActiveFrames) and chunk.is_new_hit:
                heapq.heappush(damage_at_frame, (current_frame, chunk.info))
                current_frame += chunk.info.hitstop
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
                override_info.damage = subroutine.damage
                override_info.p1 = subroutine.p1
                override_info.p2 = subroutine.p2
                override_info.minDamage = subroutine.minDamage
                override_info.p2Once = subroutine.p2Once
                override_info.hitstun = subroutine.hitstun
                override_info.untech = subroutine.untech
                override_info.blockstun = subroutine.blockstun
                override_info.hitstop = subroutine.hitstop
                override_info.bonus_blockstop = subroutine.bonus_blockstop
                override_info.bonus_hitstop = subroutine.bonus_hitstop
                override_info.attackLevel = subroutine.attackLevel

            else:
                subroutine_calls.extend(simulate_effect_on_block(chunk.name, effect_list, start_frame=current_frame))
        else:
            if isinstance(chunk, ActiveFrames):
                chunk.info.override_values(override_info)

            main_subroutine.append(chunk)
            current_frame += chunk.duration
            if isinstance(chunk, ActiveFrames):
                current_frame += chunk.info.hitstop
    subroutine_calls[0] = consolidate_frame_chunks(main_subroutine)
    new_move = Move()
    new_move.frame_chunks = subroutine_calls[0]
    new_move.landing_recovery = override_landing_recovery \
        if override_landing_recovery is not None else move.landing_recovery
    new_move.superflash_start = move.superflash_start
    new_move.superflash_duration = move.superflash_duration
    if len(subroutine_calls) > 1:
        new_move.additional_chunks = subroutine_calls[1:]
    return new_move


def write_file(moves_on_block, target):
    for moveName in moves_on_block:
        move_on_block = moves_on_block[moveName]

        target.write("\n" + moveName + "\n")
        startup, middle, recovery, total_duration, duration_on_block, last_blockstun_frame, inv_list  = \
            calc_frames_for_subroutine(move_on_block.frame_chunks,
                                       move_on_block.superflash_start,
                                       move_on_block.superflash_duration)
        subroutine_block_timelines = []
        for subroutine in move_on_block.additional_chunks:
            result = calc_frames_for_subroutine(subroutine,
                                                move_on_block.superflash_start,
                                                move_on_block.superflash_duration)
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
        for idx, inv in enumerate(inv_list):
            inv_text = get_inv_text(inv[0], inv[1], inv[2], inv[3],
                                    move_on_block.superflash_start,
                                    move_on_block.superflash_duration
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

        target.write("|startup=" + str(startup) + "|active=" + middle + "|recovery=" + recovery + "|frameAdv=" + frame_adv)
        target.write("\n|damage=" + damage + "|p1=" + p1 + "|p2=" + p2)
        target.write("\n|level=" + level + "|attribute=" + attribute + "|guard=")
        target.write("\n|blockstun=" + blockstun + "|groundHit=" + hitstun + "|airHit=" + untech + "|hitstop=" + hitstop)
        target.write("\n|inv=" + inv_text + "|hitbox=")
        target.write("\n}}\n")


def get_inv_text(inv_start, inv_duration, inv_type, inv_attr, superflash_start, superflash_duration):
    inv_type = " Guard" if inv_type == 2 else ""
    inv_attr = get_inv_attr_text(inv_attr)

    inv_end = inv_start + inv_duration - 1
    if superflash_start is not None:
        if inv_start > superflash_start:
            inv_start -= superflash_duration

        if inv_end > superflash_start:
            inv_end -= superflash_duration
    return str(inv_start) + "-" + str(inv_end) + inv_type + " " + inv_attr + inv_type


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
        fill_str(item.damage, 0, value, value_str, value_multiplier)
        fill_str(item.p1, 1, value, value_str, value_multiplier)
        fill_str(item.p2, 2, value, value_str, value_multiplier)
        fill_str(item.hitstun, 3, value, value_str, value_multiplier)
        fill_str(item.untech, 4, value, value_str, value_multiplier)
        fill_str(item.attackLevel, 5, value, value_str, value_multiplier)
        fill_str(get_inv_attr_text(item.attribute), 6, value, value_str, value_multiplier)
        fill_str(item.blockstun, 7, value, value_str, value_multiplier)
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
    toReturn = ""
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
            if len(toReturn) > 0:
                toReturn = toReturn + ","
            toReturn = toReturn + " " + str(current_hitstop)
            if current_bonus_blockstop is not None and (current_bonus_hitstop != 0 or current_bonus_blockstop != 0):
                toReturn = toReturn + "/+" + str(current_bonus_blockstop)
            if current_bonus_hitstop is not None and current_bonus_hitstop != 0:
                toReturn = toReturn + "/+" + str(current_bonus_hitstop)
            current_hitstop = info.hitstop
            current_bonus_blockstop = info.bonus_blockstop
            current_bonus_hitstop = info.bonus_hitstop
            multiplier = 1

    if len(toReturn) > 0:
        toReturn = toReturn + ","
    toReturn = toReturn + " " + str(current_hitstop)
    if current_bonus_blockstop is not None and (current_bonus_hitstop != 0 or current_bonus_blockstop != 0):
        toReturn = toReturn + "/+" + str(current_bonus_blockstop)
    if current_bonus_hitstop is not None and current_bonus_hitstop != 0:
        toReturn = toReturn + "/+" + str(current_bonus_hitstop)

    return toReturn


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

    source_dir = "."
    target_dir = "."
    file_list = ["testfile"]
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
        print "DONE"


if __name__ == "__main__":
    main()
