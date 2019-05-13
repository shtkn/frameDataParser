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
        self.disableAttackboxesThisFrame = False

    def is_attackbox(self):
        return self.isAttackBox and not (self.disableAttackboxes or self.disableAttackboxesThisFrame)


class AbstractChunk:
    def __init__(self, duration=0):
        self.duration = duration

    def __str__(self):
        return str(self.duration)


class AttackFrameChunk(AbstractChunk):
    def __init__(self, duration=0, blockstun=0, hitstop=0, additionalHitstopOpponent=0, is_new_hit=False):
        AbstractChunk.__init__(self, duration)
        self.blockstun = blockstun
        self.isNewHit = is_new_hit
        self.hitstop = hitstop
        self.additionalHitstopOpponent = additionalHitstopOpponent

    def __str__(self):
        to_return = str(self.duration)
        to_return += " Active"
        to_return += " New Hit " + str(self.isNewHit)
        to_return += " Blockstun " + str(self.blockstun)
        to_return += " Hitstop " + str(self.hitstop) + "/+" + str(self.additionalHitstopOpponent)
        return to_return


# Combination startup/and recovery frames, basically anything that's not an active frame
class WaitFrameChunk(AbstractChunk):
    def __init__(self, duration=0):
        AbstractChunk.__init__(self, duration)


class LandingFrameChunk(AbstractChunk):
    def __init__(self, duration=0):
        AbstractChunk.__init__(self, duration)


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


SPRITE_START = "    sprite('"
SPRITE_MID = "', "
SPRITE_END = ")"
HAS_HITBOX = "**attackbox here**"
GFX_START = "    GFX_0('"
CALLSUBROUTINE_START = "callSubroutine('"


def get_duration(sprite_str):
    # print sprite_str
    number_start = sprite_str.index(SPRITE_MID) + SPRITE_MID.__len__()
    number_end = sprite_str.index(SPRITE_END)
    return int(sprite_str[number_start:number_end])


def consolidate_frame_chunks(chunk_list):
    new_chunk_list = []
    prev_chunk = chunk_list[0]
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


def parse_move_file(source, move_list):
    state = State()
    frame_chunks = None
    for line in source.readlines():
        if "@State" in line or "@Subrouteine" in line:     # new move, finish parsing existing move, then restart frame counters
            if frame_chunks is not None and len(frame_chunks) > 0:
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                         state.isNewHit) \
                    if state.is_attackbox() else WaitFrameChunk(state.duration)
                frame_chunks.append(chunk)

                move_list[state.moveName] = Move()
                move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
                if state.landingRecovery > 0:
                    move_list[state.moveName].landing_recovery = state.landingRecovery
            frame_chunks = []
            # print "*** NEW MOVE ***"
            # restart counters
            state.clear_values(True)
        elif line.startswith(SPRITE_START):
            if state.duration > 0:
                chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                         state.isNewHit) \
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
            elif CALLSUBROUTINE_START in line:
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

        move_list[state.moveName] = Move()
        move_list[state.moveName].frame_chunks = consolidate_frame_chunks(frame_chunks)
        if state.landingRecovery > 0:
            move_list[state.moveName].landing_recovery = state.landingRecovery

    return move_list


def parse_subroutine(name, move_list, startFrame=0):
    if name not in move_list:
        return []
    subroutine_calls = [ ]
    subroutine_calls.append([])
    first_subroutine = subroutine_calls[0]
    duration = startFrame
    if duration > 0:
        first_subroutine.append(WaitFrameChunk(duration))
    for chunk in move_list[name].frame_chunks:
        if isinstance(chunk, SubroutineCall):
            from_children = parse_subroutine(chunk.name, move_list, duration)
            for one_subroutine in from_children:
                subroutine_calls.append(one_subroutine)
        else:
            first_subroutine.append(chunk)
            duration += chunk.duration

    subroutine_calls[0] = consolidate_frame_chunks(first_subroutine)
    if startFrame > 0 and len(subroutine_calls[0]) == 1 and isinstance(subroutine_calls[0][0], WaitFrameChunk):
        subroutine_calls.pop(0)
    return subroutine_calls


def write_file(move_list, target):
    for moveName in move_list:
        move = move_list[moveName]
        startup = 0
        middle = ""
        recovery = ""

        target.write(moveName + "\n")
        total_duration = 0
        attack_timeline = 0
        block_timeline = 0
        for idx, chunk in enumerate(move.frame_chunks):
            total_duration += chunk.duration
            if idx == 0 and len(move.frame_chunks) > 1:
                startup = chunk.duration + 1
            else:
                if isinstance(chunk, AttackFrameChunk):
                    if len(middle) > 0 and middle[len(middle) - 1] != ")":
                        middle += ","
                    middle += str(chunk.duration)
                    attack_timeline += 1
                    block_timeline = attack_timeline + chunk.blockstun + chunk.hitstop + chunk.additionalHitstopOpponent
                    attack_timeline += chunk.hitstop + chunk.duration - 1
                elif isinstance(chunk, SubroutineCall):

                    pass
                else:
                    attack_timeline += chunk.duration
                    if idx < len(move.frame_chunks) - 1:
                        middle += "(" + str(chunk.duration) + ")"
                    else:
                        recovery += str(chunk.duration)

        target.write(str(startup) + " " + middle + " " + recovery)
        if move.landing_recovery > 0:
            target.write("+" + str(move.landing_recovery) + "L")
        target.write(". Total duration: " + str(total_duration))
        if move.landing_recovery > 0:
            target.write("+" + str(move.landing_recovery) + "L")
        target.write("\n")
        target.write("\tattack duration: " + str(attack_timeline))
        if block_timeline != 0:
            target.write(" blockstun: " + str(block_timeline))
            target.write(" diff: " + str(block_timeline - attack_timeline))
        target.write("\n")
    print "DONE"


# Parse effects
sourceDir = "./"
entry = "testfileea"
effect_source = open(sourceDir + entry, "r")
effect_target = open(entry + "_out.txt", "w")
move_list = OrderedDict()
effect_list = parse_move_file(effect_source, move_list)
# Parse moves
sourceDir = "./"
entry = "testfile"
char_source = open(sourceDir + entry, "r")
char_target = open(entry + "_out.txt", "w")
move_list = parse_move_file(char_source, move_list)

# Add in subroutines
for name in move_list:
    print name
    subroutine_calls = parse_subroutine(name, move_list)
    for subroutine in subroutine_calls:
        for chunk in subroutine:
            print chunk
        print "//"
# write both files
write_file(move_list, char_target)
write_file(effect_list, effect_target)
print "DONE"
