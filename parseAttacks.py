import copy
from collections import OrderedDict


class State:
    def __init__(self):
        self.moveName = ""
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.totalDuration = 0
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

    def clear_values(self, is_new_move):
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        self.isNewHit = False
        if is_new_move:
            self.moveName = ""
            self.totalDuration = 0
            self.disableAttackboxes = False
            self.isNewHit = True
            self.blockstun = 0
            self.hitstop = 0
            self.additionalHitstopOpponent = 0
            self.exitState = False
            self.landingRecovery = 0
            self.isSubroutine = False
            self.damage = 0
        self.disableAttackboxesThisFrame = False

    def is_attackbox(self):
        return self.isAttackBox and not (self.disableAttackboxes or self.disableAttackboxesThisFrame)


class AbstractChunk:
    def __init__(self, duration=0):
        self.duration = duration

    def __str__(self):
        return str(self.duration)

    def __eq__(self, other):
        if not isinstance(other, AbstractChunk):
            return False
        return self.duration == other.duration


class AttackFrameChunk(AbstractChunk):
    def __init__(self, duration=0, blockstun=0, hitstop=0, additional_hitstop_opponent=0, is_new_hit=True):
        AbstractChunk.__init__(self, duration)
        self.blockstun = blockstun
        self.isNewHit = is_new_hit
        self.hitstop = hitstop
        self.additionalHitstopOpponent = additional_hitstop_opponent
        self.damage = 0

    def __str__(self):
        to_return = str(self.duration)
        to_return += " Active"
        to_return += " New Hit " + str(self.isNewHit)
        to_return += " Blockstun " + str(self.blockstun)
        to_return += " Hitstop " + str(self.hitstop) + "/+" + str(self.additionalHitstopOpponent)
        return to_return

    def __eq__(self, other):
        if not isinstance(other, AttackFrameChunk):
            return False
        return self.duration == other.duration and \
            self.blockstun == other.blockstun and \
            self.isNewHit == other.isNewHit and \
            self.hitstop == other.hitstop and \
            self.additionalHitstopOpponent == other.additionalHitstopOpponent and \
            self.damage == other.damage


class WaitFrameChunk(AbstractChunk):
    def __init__(self, duration=0):
        AbstractChunk.__init__(self, duration)

    def __eq__(self, other):
        if not isinstance(other, WaitFrameChunk):
            return False
        return self.duration == other.duration


class SubroutineCall(AbstractChunk):
    def __init__(self, name):
        AbstractChunk.__init__(self, 0)
        self.name = name

    def __str__(self):
        return self.name


class Move:
    def __init__(self):
        self.frame_chunks = []
        self.additional_chunks = []
        self.landing_recovery = 0


class Subroutine:
    def __init__(self):
        self.damage = 0
        self.blockstun = 0
        self.hitstop = 0
        self.additionalHitstopOpponent = 0
        self.landingRecovery = 0
        pass
    

SPRITE_START = "    sprite('"
SPRITE_MID = "', "
SPRITE_END = ")"
HAS_HITBOX = "**attackbox here**"
GFX_START = "    GFX_0('"
CALL_SUBROUTINE_START = "callSubroutine('"


def get_duration(sprite_str):
    number_start = sprite_str.index(SPRITE_MID) + SPRITE_MID.__len__()
    number_end = sprite_str.index(SPRITE_END)
    return int(sprite_str[number_start:number_end])


def consolidate_frame_chunks(chunk_list):
    new_chunk_list = []
    prev_chunk = copy.copy(chunk_list[0])
    for i in range(1, len(chunk_list)):
        chunk = chunk_list[i]
        if isinstance(prev_chunk, AttackFrameChunk) and isinstance(chunk, AttackFrameChunk):
            if chunk.isNewHit:
                new_chunk_list.append(prev_chunk)
                prev_chunk = copy.copy(chunk)
            else:
                prev_chunk.duration += chunk.duration
        elif isinstance(prev_chunk, WaitFrameChunk) and isinstance(chunk, WaitFrameChunk):
            prev_chunk.duration += chunk.duration
        else:
            new_chunk_list.append(prev_chunk)
            prev_chunk = copy.copy(chunk)
    new_chunk_list.append(prev_chunk)
    #
    # for chunk in new_chunk_list:
    #     print chunk
    return new_chunk_list


def parse_move_file(source, move_list, effect_list):
    state = State()
    frame_chunks = None
    for line in source.readlines():
        # new move, finish parsing existing move, then restart frame counters
        if "@State" in line or "@Subroutine" in line:
            if frame_chunks is not None and len(frame_chunks) > 0:
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop,
                                         state.additionalHitstopOpponent, state.isNewHit) \
                    if state.is_attackbox() else WaitFrameChunk(state.duration)
                frame_chunks.append(chunk)

                if state.isSubroutine:
                    subroutine = Subroutine()
                    subroutine.blockstun = state.blockstun
                    subroutine.hitstop = state.hitstop
                    subroutine.additionalHitstopOpponent = state.additionalHitstopOpponent
                    effect_list[state.moveName] = subroutine

                else:
                    move_list[state.moveName] = Move()
                    move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
                    if state.landingRecovery > 0:
                        move_list[state.moveName].landing_recovery = state.landingRecovery
            frame_chunks = []
            # print "*** NEW MOVE ***"
            # restart counters
            state.clear_values(True)
            if "@Subroutine" in line:
                state.isSubroutine = True
        elif SPRITE_START in line:
            if state.duration > 0:
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop,
                                         state.additionalHitstopOpponent, state.isNewHit) \
                    if state.is_attackbox() else WaitFrameChunk(state.duration)
                frame_chunks.append(chunk)
                state.clear_values(False)
            state.duration = get_duration(line)

            if HAS_HITBOX in line:
                state.isAttackBox = HAS_HITBOX in line

        elif not state.exitState:
            if "Recovery()" in line or "Unknown23027()" in line:  # disables active frames for rest of move
                state.disableAttackboxes = True
            elif "StartMultihit()" in line:  # turns off these active frames
                state.disableAttackboxesThisFrame = True
            elif "RefreshMultiHit()" in line:  # counts as a new hit, end previous frames; start a  new one
                state.isNewHit = True
            elif "AttackLevel_(" in line:  # get hitstun/blockstun values according to it's level
                level = line[line.index("(")+1:line.index("(")+2]
                # print "LEVEL: " + level
                # blockstun by level: 0: 9F, 1: 11F, 2: 13F, 3: 16F, 4: 18F, 5: 20F
                # so blockstun = 0 * Level*2. If Level 3 or higher, blockstun + 1
                state.blockstun = 9 + int(level)*2
                if int(level) >= 3:
                    state.blockstun += 1
                # hitstop by level 0: 8F, 1: 9F, 2: 10F, 3: 11F, 4: 12F, 5: 13F
                state.hitstop = 8 + int(level)
            elif "Unknown11028(" in line:
                state.blockstun = line[line.index("(")+1:line.index(")")]
                # print "Hardcoded blockstun: " + state.blockstun
            elif "Hitstop(" in line:
                state.hitstop = int(line[line.index("(")+1:line.index(")")])
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
            elif line.startswith(GFX_START):    # only care about gfx calls in teh main body, not sub functions
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
                pass  # superfreeze
            elif "ExitState()" in line:
                # we assume all the lines above this are for the move on block/whiff. Anything after is on hit
                state.exitState = True

    if state.duration > 0:
        chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                 state.isNewHit) \
            if state.is_attackbox() else WaitFrameChunk(state.duration)
        frame_chunks.append(chunk)

        if state.isSubroutine:
            subroutine = Subroutine()
            subroutine.blockstun = state.blockstun
            subroutine.hitstop = state.hitstop
            subroutine.additionalHitstopOpponent = state.additionalHitstopOpponent
            effect_list[state.moveName] = subroutine

        else:
            move_list[state.moveName] = Move()
            move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
            if state.landingRecovery > 0:
                move_list[state.moveName].landing_recovery = state.landingRecovery

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
    hit_simulations = {}
    for moveName in move_list:
        move = move_list[moveName]
        hit_simulations[moveName] = combine_with_effects_on_block(move, effect_list)
    return hit_simulations


def calc_frame_adv_for_subroutine(frame_chunks):
    startup = 0
    middle = ""
    recovery = ""
    duration_on_whiff = 0
    duration_on_block = 0
    last_frame_of_blockstun = 0
    for idx, chunk in enumerate(frame_chunks):
        if idx == 0 and len(frame_chunks) > 1:
            startup = chunk.duration + 1
        else:
            if isinstance(chunk, AttackFrameChunk):
                if len(middle) > 0 and middle[len(middle) - 1] != ")":
                    middle += ","
                middle += str(chunk.duration)
                last_frame_of_blockstun = duration_on_block + chunk.blockstun + chunk.hitstop + chunk.additionalHitstopOpponent + 1
                duration_on_block += chunk.hitstop
            else:
                if idx < len(frame_chunks) - 1:
                    middle += "(" + str(chunk.duration) + ")"
                else:
                    recovery += str(chunk.duration)
        duration_on_whiff += chunk.duration
        duration_on_block += chunk.duration

    return startup, middle, recovery, duration_on_whiff, duration_on_block, last_frame_of_blockstun


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
    if len(subroutine_calls) > 1:
        new_move.additional_chunks = subroutine_calls[1:]
    return new_move


def write_file(move_list, target):
    for moveName in move_list:
        move = move_list[moveName]

        target.write(moveName + "\n")
        startup, middle, recovery, total_duration, duration_on_block, last_blockstun_frame = \
            calc_frame_adv_for_subroutine(move.frame_chunks)
        subroutine_block_timelines = []
        for subroutine in move.additional_chunks:
            result = calc_frame_adv_for_subroutine(subroutine)
            subroutine_block_timelines.append(result[5])
        if startup > 0:
            target.write(str(startup) + " " + middle + " " + recovery)
        else:
            target.write(recovery)
        if move.landing_recovery > 0:
            target.write("+" + str(move.landing_recovery) + "L")
        target.write(". Duration: " + str(total_duration))
        if move.landing_recovery > 0:
            target.write("+" + str(move.landing_recovery) + "L")
        target.write("\n")
        target.write("\tduration on block: " + str(duration_on_block))
        if len(subroutine_block_timelines) > 0:
            for num in subroutine_block_timelines:
                last_blockstun_frame = num if num > last_blockstun_frame else last_blockstun_frame
        if last_blockstun_frame != 0:
            target.write(" blockstun: " + str(last_blockstun_frame))
            target.write(" diff: " + str(last_blockstun_frame - duration_on_block))
        target.write("\n")
    print "DONE"


def main():
    # Parse effects
    source_dir = "./"
    entry = "testfileea"
    effect_source = open(source_dir + entry, "r")
    effect_list = OrderedDict()
    effect_list = parse_move_file(effect_source, effect_list, effect_list)
    # Parse moves
    source_dir = "./"
    entry = "testfile"
    char_source = open(source_dir + entry, "r")
    char_target = open(entry + "_out.txt", "w")
    move_list = OrderedDict()
    move_list = parse_move_file(char_source, move_list, effect_list)

    hit_simulations = simulate_on_block(move_list, effect_list)

    write_file(hit_simulations, char_target)
    print "DONE"


if __name__ == "__main__":
    main()
