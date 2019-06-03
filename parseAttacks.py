import copy
import os
from collections import OrderedDict
import heapq


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
        self.blockstun = 0
        self.hitstop = 0
        self.additionalHitstopOpponent = 0
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

    def clear_values(self, is_new_move):
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        if is_new_move:
            self.moveName = ""
            self.disableAttackboxes = False
            self.isNewHit = True
            self.blockstun = 0
            self.hitstop = 0
            self.additionalHitstopOpponent = 0
            self.exitState = False
            self.landingRecovery = 0
            self.isSubroutine = False
            self.damage = None
            self.p1 = None
            self.p2 = None
            self.p2Once = False
            self.isInv = False
            self.invType = 0
            self.invAttr = [True, True, True, True, True]
            self.superflash_start = None
            self.superflash_duration = 0
        self.disableAttackboxesThisFrame = False

    def is_attackbox(self):
        return self.isAttackBox and not (self.disableAttackboxes or self.disableAttackboxesThisFrame)


class Damage:
    def __init__(self, damage, p1=100, p2=100, min_damage=0, p2once=False):
        self.damage = damage
        self.p1 = p1
        self.p2 = p2
        self.minDamage = min_damage
        self.p2Once = p2once

    def __eq__(self, other):
        if not isinstance(other, Damage):
            return False
        return self.damage == other.damage and self.p1 == other.p1 and self.p2 == other.p2 and \
            self.minDamage == other.minDamage and self.p2Once == other.p2Once

    def __ne__(self, other):
        if not isinstance(other, Damage):
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

class Abstract:
    def __init__(self):
        pass


class AbstractChunk(Abstract):
    def __init__(self, duration=0):
        Abstract.__init__(self)
        self.duration = duration
        self.inv_type = 0  # 0 = no inv, 1 = inv, 2 = guard
        self.inv_attr = [False, False, False, False, False]

    def __str__(self):
        return str(self.duration)

    def __eq__(self, other):
        if not isinstance(other, AbstractChunk):
            return False
        return self.duration == other.duration and self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

    def __ne__(self, other):
        if not isinstance(other, AbstractChunk):
            return False
        return not self.__eq__(other)


class AttackFrameChunk(AbstractChunk):
    def __init__(self, duration=0, blockstun=0, hitstop=0, additional_hitstop_opponent=0, is_new_hit=True,
                 damage=Damage(0)):
        AbstractChunk.__init__(self, duration)
        self.blockstun = blockstun
        self.is_new_hit = is_new_hit
        self.hitstop = hitstop
        self.additionalHitstopOpponent = additional_hitstop_opponent
        self.damage = damage

    def __str__(self):
        to_return = str(self.duration)
        to_return += " Active"
        to_return += " New Hit " + str(self.is_new_hit)
        to_return += " Blockstun " + str(self.blockstun)
        to_return += " Hitstop " + str(self.hitstop) + "/+" + str(self.additionalHitstopOpponent)
        return to_return

    def __eq__(self, other):
        if not isinstance(other, AttackFrameChunk):
            return False
        return self.duration == other.duration and self.blockstun == other.blockstun and \
            self.is_new_hit == other.is_new_hit and self.hitstop == other.hitstop and \
            self.additionalHitstopOpponent == other.additionalHitstopOpponent and \
            self.damage == other.damage and self.duration == other.duration and \
            self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

    def __ne__(self, other):
        if not isinstance(other, AttackFrameChunk):
            return False
        return not self.__eq__(other)


class WaitFrameChunk(AbstractChunk):
    def __init__(self, duration=0):
        AbstractChunk.__init__(self, duration)

    def __eq__(self, other):
        if not isinstance(other, WaitFrameChunk):
            return False
        return self.duration == other.duration and self.inv_type == other.inv_type and self.inv_attr == other.inv_attr

    def __ne__(self, other):
        if not isinstance(other, WaitFrameChunk):
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
        self.additionalHitstopOpponent = None
        self.landingRecovery = None
        self.p1 = None
        self.p2 = None
        self.p2Once = False
        self.minDamage = None

    def __eq__(self, other):
        if not isinstance(other, Subroutine):
            return False
        return self.damage == other.damage and self.p1 == other.p1 and self.p2 == other.p2 and\
            self.p2Once == other.p2Once and self.minDamage == other.minDamage and \
            self.blockstun == other.blockstun and \
            self.hitstop == other.hitstop and \
            self.additionalHitstopOpponent == other.additionalHitstopOpponent and \
            self.landingRecovery == other.landingRecovery

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
        if isinstance(prev_chunk, AttackFrameChunk) and isinstance(chunk, AttackFrameChunk) \
                and (has_same_inv(prev_chunk, chunk) or ignore_inv):
            if chunk.is_new_hit:
                new_chunk_list.append(prev_chunk)
                prev_chunk = copy.copy(chunk)
            else:
                prev_chunk.duration += chunk.duration
        elif isinstance(prev_chunk, WaitFrameChunk) and isinstance(chunk, WaitFrameChunk) \
                and (has_same_inv(prev_chunk, chunk) or ignore_inv):
            prev_chunk.duration += chunk.duration
        else:
            new_chunk_list.append(prev_chunk)
            prev_chunk = copy.copy(chunk)
    new_chunk_list.append(prev_chunk)

    return new_chunk_list

def createDamageValuesIntoFromState(state):
    damage = 0 if state.damage is None else state.damage
    p1 = 100 if state.p1 is None else state.p1
    p2 = 100 if state.p2 is None else state.p2
    p2Once = False if state.p2Once is None else state.p2Once
    minDamage = 0 if state.minDamage is None else state.minDamage
    return Damage(damage, p1, p2, minDamage, p2Once)


def parse_move_file(source, move_list, effect_list):
    state = State()
    frame_chunks = None
    for line in source.readlines():
        # new move, finish parsing existing move, then restart frame counters
        if "@State" in line or "@Subroutine" in line:

            if state.isSubroutine:
                subroutine = Subroutine()
                subroutine.blockstun = state.blockstun
                subroutine.hitstop = state.hitstop
                subroutine.additionalHitstopOpponent = state.additionalHitstopOpponent
                subroutine.damage = state.damage
                subroutine.p1 = state.p1
                subroutine.p2 = state.p2
                subroutine.p2Once = state.p2Once
                effect_list[state.moveName] = subroutine

            elif frame_chunks is not None and len(frame_chunks) > 0:
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop,
                                         state.additionalHitstopOpponent, state.isNewHit) \
                    if state.is_attackbox() else WaitFrameChunk(state.duration)
                if state.isInv:
                    chunk.inv_type = 1 if state.invType == 0 else 2
                    chunk.inv_attr = state.invAttr
                if isinstance(chunk, AttackFrameChunk):
                    chunk.damage = createDamageValuesIntoFromState(state)
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
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop,
                                         state.additionalHitstopOpponent, state.isNewHit) \
                    if state.is_attackbox() else WaitFrameChunk(state.duration)
                if state.isInv:
                    chunk.inv_type = 1 if state.invType == 0 else 2
                    chunk.inv_attr = state.invAttr
                frame_chunks.append(chunk)
                if isinstance(chunk, AttackFrameChunk):
                    state.isNewHit = False
                    chunk.damage = createDamageValuesIntoFromState(state)
                state.clear_values(False)
            state.duration = get_duration(line)

            if HAS_HITBOX in line:
                state.isAttackBox = HAS_HITBOX in line
        elif not state.exitState:
            if "Recovery()" in line or "Unknown23027()" in line:  # disables active frames for rest of move
                state.disableAttackboxes = True
            elif "StartMultihit()" in line:  # turns off these active frames
                state.disableAttackboxesThisFrame = True
            elif "RefreshMultihit()" in line:  # counts as a new hit, end previous frames; start a  new one
                state.isNewHit = True
            elif "AttackLevel_(" in line:  # get hitstun/blockstun values according to it's level
                level = int(line[line.index("(") + 1:line.index(")")])
                # print "LEVEL: " + level
                # blockstun by level: 0: 9F, 1: 11F, 2: 13F, 3: 16F, 4: 18F, 5: 20F
                # so blockstun = 0 * Level*2. If Level 3 or higher, blockstun + 1
                state.blockstun = 9 + level * 2
                if level >= 3:
                    state.blockstun += 1
                # hitstop by level 0: 8F, 1: 9F, 2: 10F, 3: 11F, 4: 12F, 5: 13F
                state.hitstop = 8 + level
                state.p2 = 65 + (level * 5)
                if level == 0 or level == 1 or level == 2:
                    state.damage = 1000
                elif level == 3:
                    state.damage = 1500
                elif level == 4:
                    state.damage = 1700
                elif level == 5:
                    state.damage = 2000

            elif "AttackP1(" in line:
                state.p1 = int(line[line.index("(") + 1:line.index(")")])
            elif "AttackP2(" in line:
                state.p2 = int(line[line.index("(") + 1:line.index(")")])
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
                name_start = line.index("(") + 1
                name_end = line.index(")")
                numbers = [x.strip() for x in line[name_start:name_end].split(',')]
                state.additionalHitstopOpponent = int(numbers[0])
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
                    if isinstance(chunk, AbstractChunk):
                        state.superflash_start += chunk.duration
                state.superflash_duration = int(line[flash_start:flash_end])
                # superfreeze
            elif "Unknown22019(" in line:
                # set invul to which attributes
                params = line[line.index("('") + 2: line.index("')")]
                state.invAttr = parse_attributes(params)
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
                state.blockstun = 16
                state.hitstop = 11

    if state.isSubroutine:
        subroutine = Subroutine()
        subroutine.blockstun = state.blockstun
        subroutine.hitstop = state.hitstop
        subroutine.additionalHitstopOpponent = state.additionalHitstopOpponent
        subroutine.damage = state.damage
        subroutine.p1 = state.p1
        subroutine.p2 = state.p2
        subroutine.p2Once = state.p2Once
        effect_list[state.moveName] = subroutine

    elif state.duration > 0:
        chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                 state.isNewHit) \
            if state.is_attackbox() else WaitFrameChunk(state.duration)
        if state.isInv:
            chunk.inv_type = 1 if state.invType == 0 else 2
            chunk.inv_attr = state.invAttr
        if isinstance(chunk, AttackFrameChunk):
            chunk.damage = createDamageValuesIntoFromState(state)

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
    override_blockstun = None
    override_hitstop = None
    override_additional_hitstop = None
    override_damage = None
    if duration > 0:
        first_subroutine.append(WaitFrameChunk(duration))
    for chunk in move_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = []
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                subroutine = effect_list[chunk.name]
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_blockstun = subroutine.blockstun
                override_hitstop = subroutine.hitstop
                override_additional_hitstop = subroutine.additionalHitstopOpponent
                override_damage = Damage(subroutine.damage, subroutine.p1, subroutine.p2,
                                         subroutine.minDamage, subroutine.p2Once)
            else:
                from_children = parse_subroutine(chunk.name, effect_list, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, AttackFrameChunk):
                if override_blockstun is not None:
                    chunk.blockstun = override_blockstun
                if override_additional_hitstop is not None:
                    chunk.additionalHitstopOpponent = override_additional_hitstop
                if override_hitstop is not None:
                    chunk.hitstop = override_hitstop
                if override_damage is not None:
                    chunk.damage.override_values(override_damage)

            first_subroutine.append(chunk)
            duration += chunk.duration

    subroutine_calls[0] = consolidate_frame_chunks(first_subroutine)
    # delete any subroutines that don't add anything
    if len(subroutine_calls[0]) == 1 and isinstance(subroutine_calls[0][0], WaitFrameChunk):
        subroutine_calls.pop(0)
    return subroutine_calls


def simulate_effect_on_block(name, effect_list, start_frame=0):
    if name not in effect_list:
        return []
    subroutine_calls = [[]]
    first_subroutine = subroutine_calls[0]
    duration = start_frame
    override_blockstun = None
    override_hitstop = None
    override_additional_hitstop = None
    override_damage = None
    if duration > 0:
        first_subroutine.append(WaitFrameChunk(duration))
    for chunk in effect_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = []
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                subroutine = effect_list[chunk.name]
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_blockstun = subroutine.blockstun
                override_hitstop = subroutine.hitstop
                override_additional_hitstop = subroutine.additionalHitstopOpponent
                override_damage = Damage(subroutine.damage, subroutine.p1, subroutine.p2,
                                         subroutine.minDamage, subroutine.p2Once)
            else:
                from_children = parse_subroutine(chunk.name, effect_list, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, AttackFrameChunk):
                if override_blockstun is not None:
                    chunk.blockstun = override_blockstun
                if override_additional_hitstop is not None:
                    chunk.additionalHitstopOpponent = override_additional_hitstop
                if override_hitstop is not None:
                    chunk.hitstop = override_hitstop
                if override_damage is not None:
                    chunk.damage.override_values(override_damage)

            first_subroutine.append(chunk)
            duration += chunk.duration
            if isinstance(chunk, AttackFrameChunk):
                duration += chunk.hitstop

    subroutine_calls[0] = consolidate_frame_chunks(first_subroutine)
    # delete any subroutines that don't add anything
    if start_frame > 0 and len(subroutine_calls[0]) == 1 and isinstance(subroutine_calls[0][0], WaitFrameChunk):
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

    combine_inv_frame_chunks = consolidate_frame_chunks(frame_chunks, True)
    for idx, chunk in enumerate(combine_inv_frame_chunks):
        if isinstance(chunk, AttackFrameChunk):
            if len(middle) > 0 and middle[len(middle) - 1] != ")":
                middle += ","
            middle += str(chunk.duration)
            last_frame_of_blockstun = duration_on_block + chunk.blockstun + chunk.hitstop + \
                chunk.additionalHitstopOpponent + 1
            duration_on_block += chunk.hitstop
        elif middle == "":
            startup += chunk.duration
        else:
            if idx < len(combine_inv_frame_chunks) - 1:
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
        pass
    return startup, middle, str(recovery), duration_on_whiff, duration_on_block, last_frame_of_blockstun, cleaned_list


def calc_damage_for_move(move_on_block):
    damage_at_frame = []

    all_frame_chunks = [move_on_block.frame_chunks]
    all_frame_chunks.extend(move_on_block.additional_chunks)
    for frame_chunks in all_frame_chunks:
        current_frame = 0
        for chunk in frame_chunks:
            if isinstance(chunk, AttackFrameChunk) and chunk.is_new_hit:
                heapq.heappush(damage_at_frame, (current_frame, chunk.damage))
                current_frame += chunk.hitstop
            current_frame += chunk.duration

    damage_list = []
    while len(damage_at_frame) > 0:
        value = heapq.heappop(damage_at_frame)
        damage_list.append(value[1])
        if isinstance(value[1], (int, long)):
            print value

    return damage_list


def combine_with_effects_on_block(move, effect_list):
    override_blockstun = None
    override_hitstop = None
    override_additional_hitstop = None
    override_landing_recovery = None
    override_damage = None
    current_frame = 0
    subroutine_calls = []
    main_subroutine = []
    subroutine_calls.append(main_subroutine)
    for idx, chunk in enumerate(move.frame_chunks):
        if isinstance(chunk, SubroutineCall):
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                subroutine = effect_list[chunk.name]
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_blockstun = subroutine.blockstun
                override_hitstop = subroutine.hitstop
                override_additional_hitstop = subroutine.additionalHitstopOpponent
                override_damage = Damage(subroutine.damage, subroutine.p1, subroutine.p2,
                                         subroutine.minDamage, subroutine.p2Once)

            else:
                subroutine_calls.extend(simulate_effect_on_block(chunk.name, effect_list, start_frame=current_frame))
        else:
            if isinstance(chunk, AttackFrameChunk):
                if override_blockstun is not None:
                    chunk.blockstun = override_blockstun
                if override_additional_hitstop is not None:
                    chunk.additionalHitstopOpponent = override_additional_hitstop
                if override_hitstop is not None:
                    chunk.hitstop = override_hitstop
                if override_damage is not None:
                    chunk.damage.override_values(override_damage)

            main_subroutine.append(chunk)
            current_frame += chunk.duration
            if isinstance(chunk, AttackFrameChunk):
                current_frame += chunk.hitstop
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

        target.write(moveName + "\n")
        startup, middle, recovery, total_duration, duration_on_block, last_blockstun_frame, inv_list = \
            calc_frames_for_subroutine(move_on_block.frame_chunks,
                                       move_on_block.superflash_start,
                                       move_on_block.superflash_duration)
        subroutine_block_timelines = []
        for subroutine in move_on_block.additional_chunks:
            result = calc_frames_for_subroutine(subroutine,
                                                move_on_block.superflash_start,
                                                move_on_block.superflash_duration)
            subroutine_block_timelines.append(result)
        if startup is not "":
            target.write("\t" + str(startup) + " " + middle + " " + str(recovery))
        else:
            target.write("Total: " + str(recovery))
        if move_on_block.landing_recovery > 0:
            target.write("+" + str(move_on_block.landing_recovery) + "L")
        target.write("\n\tduration on block: " + str(duration_on_block))
        if len(subroutine_block_timelines) > 0:
            for result in subroutine_block_timelines:
                last_blockstun_frame = result[5] if result[5] > last_blockstun_frame else last_blockstun_frame
                # target.write("\n\tstartup: " + str(result[0]))
                target.write("\n\t" + str(result[0]) + " " + result[1] + " " + str(result[2]))
                target.write(" blockstun: " + str(last_blockstun_frame))
        if last_blockstun_frame != 0:
            target.write("\n\tlast blockstun: " + str(last_blockstun_frame))
            target.write(" diff: " + str(last_blockstun_frame - duration_on_block))
        for inv in inv_list:
            inv_text = get_inv_text(inv[0], inv[1], inv[2], inv[3],
                                    move_on_block.superflash_start,
                                    move_on_block.superflash_duration
                                    )
            target.write("\n\t" + inv_text)

        damage_list = calc_damage_for_move(move_on_block)
        damage_str = create_damage_text(damage_list)
        target.write(damage_str)
        target.write("\n")


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
    if len(damage_list) == 0:
        return ""

    damage_str = ""
    damage = None
    damage_multiplier = 1
    p1_str = ""
    p1 = None
    p1_multiplier = 1
    p2 = None
    p2_multiplier = 1
    p2Once = None
    p2_str = ""
    for item in damage_list:
        if damage == item.damage:
            damage_multiplier += 1
        elif damage is not None:
            damage_str += str(damage)
            if damage_multiplier > 1:
                damage_str += "*" + str(damage_multiplier)
                damage_multiplier = 1   # reset multiplier
            damage_str += ", "
        damage = item.damage
        if p1 == item.p1:
            p1_multiplier += 1
        elif p1 is not None:
            p1_str += str(p1)
            if p1_multiplier > 1:
                p1_str += "*" + str(p1_multiplier)
                p1_multiplier = 1   # reset multiplier
            p1_str += ", "
        p1 = item.p1
        if p2 == item.p2:
            p2_multiplier += 1
        elif p2 is not None:
            p2_str += str(p2)
            if p2_multiplier > 1:
                p2_str += "*" + str(p2_multiplier)
                p2_multiplier = 1   # reset multiplier
            p2_str += ", "
        p2 = item.p2
        p2Once = item.p2Once

    if damage is not None:
        damage_str += str(damage)
        if damage_multiplier > 1:
            damage_str += "*" + str(damage_multiplier)
    if p1 is not None:
        p1_str += str(p1)
        if p1_multiplier > 1 and p1_str != (str(p1)):
            p1_str += "*" + str(p1_multiplier)
    if p2 is not None:
        p2_str += str(p2)
        if p2_multiplier > 1 and p1_str != (str(p1)):
            p2_str += "*" + str(p2_multiplier)
        if p2Once:
            p2_str += " (Once)"

    return "\n\tdamage: " + damage_str + "\tP1: " + p1_str + "\tP2: " + p2_str


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
        #
        for move_name in move_list.keys():
            if move_name not in registered_moves and "Exe" not in move_name and "ChangePartnerDD" not in move_name:
                del move_list[move_name]

        hit_simulations = simulate_on_block(move_list, effect_list)

        write_file(hit_simulations, char_target)
        print "DONE"


if __name__ == "__main__":
    main()
