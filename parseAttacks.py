import copy
import os
from collections import OrderedDict


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
        self.damage = 0
        self.P1 = 100
        self.P2 = 100
        self.P2Once = False
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
            self.damage = 0
            self.P1 = 100
            self.P2 = 100
            self.P2Once = False
            self.isInv = False
            self.invType = 0
            self.invAttr = [True, True, True, True, True]
            self.superflash_start = None
            self.superflash_duration = 0
        self.disableAttackboxesThisFrame = False

    def is_attackbox(self):
        return self.isAttackBox and not (self.disableAttackboxes or self.disableAttackboxesThisFrame)


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
    def __init__(self, duration=0, blockstun=0, hitstop=0, additional_hitstop_opponent=0, is_new_hit=True):
        AbstractChunk.__init__(self, duration)
        self.blockstun = blockstun
        self.is_new_hit = is_new_hit
        self.hitstop = hitstop
        self.additionalHitstopOpponent = additional_hitstop_opponent
        self.damage = 0
        self.p1 = 100
        self.p2 = 100
        self.p2Once = False
        self.minDamage = 0

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
        self.damage = 0
        self.blockstun = 0
        self.hitstop = 0
        self.additionalHitstopOpponent = 0
        self.landingRecovery = 0

    def __eq__(self, other):
        if not isinstance(other, Subroutine):
            return False
        return self.damage == other.damage and \
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
CALL_SUBROUTINE_START = "callSubroutine('"


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


def consolidate_frame_chunks(chunk_list):
    new_chunk_list = []
    prev_chunk = copy.copy(chunk_list[0])
    for i in range(1, len(chunk_list)):
        chunk = chunk_list[i]
        if isinstance(prev_chunk, AttackFrameChunk) and isinstance(chunk, AttackFrameChunk) \
                and has_same_inv(prev_chunk, chunk):
            if chunk.is_new_hit:
                new_chunk_list.append(prev_chunk)
                prev_chunk = copy.copy(chunk)
            else:
                prev_chunk.duration += chunk.duration
        elif isinstance(prev_chunk, WaitFrameChunk) and isinstance(chunk, WaitFrameChunk) \
                and has_same_inv(prev_chunk, chunk):
            prev_chunk.duration += chunk.duration
        else:
            new_chunk_list.append(prev_chunk)
            prev_chunk = copy.copy(chunk)
    new_chunk_list.append(prev_chunk)

    return new_chunk_list


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
                effect_list[state.moveName] = subroutine

            elif frame_chunks is not None and len(frame_chunks) > 0:
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop,
                                         state.additionalHitstopOpponent, state.isNewHit) \
                    if state.is_attackbox() else WaitFrameChunk(state.duration)
                if state.isInv:
                    chunk.inv_type = 1 if state.invType == 0 else 2
                    chunk.inv_attr = state.invAttr
                if isinstance(chunk, AttackFrameChunk):
                    chunk.damage = state.damage
                    chunk.p1 = state.P1
                    chunk.p2 = state.P2
                    chunk.p2Once = state.P2Once
                    chunk.minDamage = state.minDamage
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
                    chunk.damage = state.damage
                    chunk.p1 = state.P1
                    chunk.p2 = state.P2
                    chunk.p2Once = state.P2Once
                    chunk.minDamage = state.minDamage
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
                level = line[line.index("(") + 1:line.index("(") + 2]
                # print "LEVEL: " + level
                # blockstun by level: 0: 9F, 1: 11F, 2: 13F, 3: 16F, 4: 18F, 5: 20F
                # so blockstun = 0 * Level*2. If Level 3 or higher, blockstun + 1
                state.blockstun = 9 + int(level) * 2
                if int(level) >= 3:
                    state.blockstun += 1
                # hitstop by level 0: 8F, 1: 9F, 2: 10F, 3: 11F, 4: 12F, 5: 13F
                state.hitstop = 8 + int(level)
                state.P2 = 65 + (int(level) * 5)
            elif "AttackP1(" in line:
                state.P1 = int(line[line.index("(") + 1:line.index(")")])
            elif "AttackP2(" in line:
                state.P2 = int(line[line.index("(") + 1:line.index(")")])
            elif " Damage(" in line:
                state.damage = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown11092(" in line:
                state.P2Once = line[line.index("(") + 1:line.index(")")] == "1"
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
            elif CALL_SUBROUTINE_START in line:
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
        effect_list[state.moveName] = subroutine

    elif state.duration > 0:
        chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                 state.isNewHit) \
            if state.is_attackbox() else WaitFrameChunk(state.duration)
        if state.isInv:
            chunk.inv_type = 1 if state.invType == 0 else 2
            chunk.inv_attr = state.invAttr
        if isinstance(chunk, AttackFrameChunk):
            chunk.damage = state.damage
            chunk.p1 = state.P1
            chunk.p2 = state.P2
            chunk.p2Once = state.P2Once
            chunk.minDamage = state.minDamage

        frame_chunks.append(chunk)

        move_list[state.moveName] = Move()
        move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
        if state.landingRecovery > 0:
            move_list[state.moveName].landing_recovery = state.landingRecovery
        if state.superflash_start is not None:
            move_list[state.moveName].superflash_start = state.superflash_start
            move_list[state.moveName].superflash_duration = state.superflash_duration

    return move_list


def parse_subroutine(name, move_list, effect_list, start_frame=0):
    if name not in move_list:
        return []
    subroutine_calls = [[]]
    first_subroutine = subroutine_calls[0]
    duration = start_frame
    override_blockstun = None
    override_hitstop = None
    override_additional_hitstop = None
    if duration > 0:
        first_subroutine.append(WaitFrameChunk(duration))
    for chunk in move_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = []
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_blockstun = effect_list[chunk.name].blockstun
                override_hitstop = effect_list[chunk.name].hitstop
                override_additional_hitstop = effect_list[chunk.name].additionalHitstopOpponent
            else:
                from_children = parse_subroutine(chunk.name, effect_list, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, AttackFrameChunk) and override_blockstun is not None:
                chunk.blockstun = override_blockstun
                chunk.hitstop = override_hitstop
                chunk.additionalHitstopOpponent = override_additional_hitstop

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
    if duration > 0:
        first_subroutine.append(WaitFrameChunk(duration))
    for chunk in effect_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = []
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_blockstun = effect_list[chunk.name].blockstun
                override_hitstop = effect_list[chunk.name].hitstop
                override_additional_hitstop = effect_list[chunk.name].additionalHitstopOpponent
            else:
                from_children = parse_subroutine(chunk.name, effect_list, effect_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            if isinstance(chunk, AttackFrameChunk) and override_blockstun is not None:
                chunk.blockstun = override_blockstun
                chunk.hitstop = override_hitstop
                chunk.additionalHitstopOpponent = override_additional_hitstop

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
    recovery = ""
    duration_on_whiff = 0
    duration_on_block = 0
    last_frame_of_blockstun = 0
    inv_list = [[0, 0, [False, False, False, False, False]]]  # duration, type, attributes
    for idx, chunk in enumerate(frame_chunks):
        if idx == 0 and len(frame_chunks) > 1:
            startup = chunk.duration + 1
        else:
            if isinstance(chunk, AttackFrameChunk):
                if len(middle) > 0 and middle[len(middle) - 1] != ")":
                    middle += ","
                middle += str(chunk.duration)
                last_frame_of_blockstun = duration_on_block + chunk.blockstun + chunk.hitstop + \
                    chunk.additionalHitstopOpponent + 1
                duration_on_block += chunk.hitstop
            elif len(middle) < 1:
                startup += chunk.duration
            else:
                if idx < len(frame_chunks) - 1:
                    middle += "(" + str(chunk.duration) + ")"
                else:
                    recovery += str(chunk.duration)
        if chunk.inv_type == inv_list[-1][1] and chunk.inv_attr == inv_list[-1][2]:
            inv_list[-1][0] += chunk.duration
        else:
            inv_list.append([chunk.duration, chunk.inv_type, chunk.inv_attr])
        duration_on_whiff += chunk.duration
        duration_on_block += chunk.duration

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

    return startup, middle, recovery, duration_on_whiff, duration_on_block, last_frame_of_blockstun, cleaned_list


def calc_damage_for_subroutine(move, effect_list):
    damage_list = []
    for chunk in move.frame_chunks:
        if isinstance(chunk, AttackFrameChunk):
            if chunk.is_new_hit:
                damage_list.append([chunk.damage, chunk.p1, chunk.p2, chunk.p2Once, chunk.minDamage])
        elif isinstance(chunk, SubroutineCall):
            # calc_damage_for_subroutine(, effect_list)
            damage_list.extend(calc_damage_for_subroutine(effect_list[chunk.name], effect_list))

    return damage_list


def combine_with_effects_on_block(move, effect_list):
    override_blockstun = None
    override_hitstop = None
    override_additional_hitstop = None
    override_landing_recovery = None
    current_frame = 0
    subroutine_calls = []
    main_subroutine = []
    subroutine_calls.append(main_subroutine)
    for idx, chunk in enumerate(move.frame_chunks):
        if isinstance(chunk, SubroutineCall):
            if chunk.name in effect_list and isinstance(effect_list[chunk.name], Subroutine):
                # print "SUBROUTINE " + effect_list[chunk.name]
                override_blockstun = effect_list[chunk.name].blockstun
                override_hitstop = effect_list[chunk.name].hitstop
                override_additional_hitstop = effect_list[chunk.name].additionalHitstopOpponent
                override_landing_recovery = effect_list[chunk.name].landingRecovery
            else:
                subroutine_calls.extend(simulate_effect_on_block(chunk.name, effect_list, start_frame=current_frame))
        else:
            if isinstance(chunk, AttackFrameChunk) and override_blockstun is not None:
                chunk.blockstun = override_blockstun
                chunk.hitstop = override_hitstop
                chunk.additionalHitstopOpponent = override_additional_hitstop

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
        if startup is not "0":
            target.write(str(startup) + " " + middle + " " + recovery)
        else:
            target.write("Total: " + recovery)
        if move_on_block.landing_recovery > 0:
            target.write("+" + str(move_on_block.landing_recovery) + "L")
        # target.write(". Duration: " + duration_str)
        if move_on_block.landing_recovery > 0:
            target.write("+" + str(move_on_block.landing_recovery) + "L")
        target.write("\n\tduration on block: " + str(duration_on_block))
        if len(subroutine_block_timelines) > 0:
            for result in subroutine_block_timelines:
                last_blockstun_frame = result[5] if result[5] > last_blockstun_frame else last_blockstun_frame
                target.write("\n\tstartup: " + str(result[0]))
                target.write(" blockstun: " + str(last_blockstun_frame))
        if last_blockstun_frame != 0:
            target.write("\n\tlast blockstun: " + str(last_blockstun_frame))
            target.write(" diff: " + str(last_blockstun_frame - duration_on_block))
        for inv in inv_list:
            inv_type = " Guard" if inv[2] == 2 else ""
            inv_attr = get_inv_attr_text(inv[3])

            target.write("\n\t" + str(inv[0]) + "-" + str(inv[0] + inv[1] - 1) + inv_type + " " + inv_attr)
        target.write("\n")


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


def main():
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
    # file_list = ["testfile"]
    for file_name in file_list:
        # Parse effects
        source_dir = "./annotated"
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
        target_dir = "./parsedAttacks"
        char_target = open(target_dir + "/" + file_name + "_out.txt", "w")
        move_list = OrderedDict()
        move_list = parse_move_file(char_source, move_list, effect_list)

        hit_simulations = simulate_on_block(move_list, effect_list)

        write_file(hit_simulations, char_target)
        print "DONE"


if __name__ == "__main__":
    main()
