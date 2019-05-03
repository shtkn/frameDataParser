sourceDir = "./output/"
entry = "scr_bes.py"


class State:
    def __init__(self):
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

    def clear_values(self, is_new_move):
        self.spriteLine = ""
        self.extraLines = ""
        self.duration = 0
        self.isAttackBox = False
        self.isNewHit = False
        if is_new_move:
            self.disableAttackboxes = False
            self.isNewHit = True
        self.disableAttackboxesThisFrame = False
        # self.blockstun = 0
        # self.hitstop = 0
        # self.additionalHitstopOpponent = 0

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


class FrameChunk(AbstractChunk):
    def __init__(self, duration=0):
        AbstractChunk.__init__(self, duration)


SPRITE_START = "sprite('"
SPRITE_MID = "', "
SPRITE_END = ")"
HAS_HITBOX = "**attackbox here**"


def get_duration(sprite_str):
    print sprite_str
    number_start = sprite_str.index(SPRITE_MID) + SPRITE_MID.__len__()
    number_end = sprite_str.index(SPRITE_END)
    return int(line[number_start:number_end])


def consolidate_frame_chunks(chunk_list):
    new_chunk_list = []

    prev_chunk = move[0]
    for i in range(1, len(chunk_list)-1):
        chunk = move[i]
        if isinstance(prev_chunk, AttackFrameChunk) and isinstance(chunk, AttackFrameChunk):
            if chunk.isNewHit:
                new_chunk_list.append(prev_chunk)
                prev_chunk = chunk
            else:
                prev_chunk.duration += chunk.duration
        elif isinstance(prev_chunk, FrameChunk) and isinstance(chunk, FrameChunk):
                prev_chunk.duration += chunk.duration
        else:
            new_chunk_list.append(prev_chunk)
            prev_chunk = chunk
    new_chunk_list.append(prev_chunk)
    #
    # for chunk in newChunkList:
    #     print chunk
    return new_chunk_list


state = State()
source = open(sourceDir + entry, "r")
target = open(entry + ".txt", "w")
contents = source.readlines()

moveList = {}
move = None
moveName = ""
for line in contents:
    if "@State" in line:     # new move, finish parsing existing move, then restart frame counters
        if move is not None and len(move) > 0:
            chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                     state.isNewHit) \
                if state.is_attackbox() else FrameChunk(state.duration)
            move.append(chunk)
            moveList[moveName] = consolidate_frame_chunks(move)
        move = []
        moveName = ""
        # print "*** NEW MOVE ***"
        # restart counters
        state.clear_values(True)

    elif SPRITE_START in line:
        if state.duration > 0:
            chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                                     state.isNewHit) \
                if state.is_attackbox() else FrameChunk(state.duration)
            move.append(chunk)
            state.clear_values(False)
        spriteLine = line
        state.duration = get_duration(spriteLine)

        if HAS_HITBOX in spriteLine:
            state.isAttackBox = HAS_HITBOX in spriteLine

    else:
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
        elif "def " in line and len(moveName) < 1:
            name_start = line.index("def ") + SPRITE_MID.__len__() +1
            name_end = line.index("()")
            moveName = line[name_start:name_end]
        elif "Unknown11001(" in line:
            name_start = line.index("(") +1
            name_end = line.index(")")
            numbers = [x.strip() for x in line[name_start:name_end].split(',')]
            state.additionalHitstopOpponent = int(numbers[0])

if state.duration > 0:
    chunk = AttackFrameChunk(state.duration, state.blockstun, state.hitstop, state.additionalHitstopOpponent,
                             state.isNewHit) \
        if state.is_attackbox() else FrameChunk(state.duration)
    move.append(chunk)
    moveList[moveName] = consolidate_frame_chunks(move)


target = open("outfile", "w")
for moveName in moveList:
    move = moveList[moveName]
    startup = 0
    middle = ""
    recovery = ""

    target.write(moveName + "\n")
    total_duration = 0
    attack_timeline = 0
    block_timeline = 0
    for idx, chunk in enumerate(move):
        total_duration += chunk.duration
        if idx == 0 and len(move) > 1:
            startup = chunk.duration +1
        else:
            if isinstance(chunk, AttackFrameChunk):
                if len(middle) > 0 and middle[len(middle)-1] != ")":
                    middle += ","
                middle += str(chunk.duration)
                attack_timeline += 1
                block_timeline = attack_timeline + chunk.blockstun + chunk.hitstop + chunk.additionalHitstopOpponent
                attack_timeline += chunk.hitstop + chunk.duration - 1
            else:
                attack_timeline += chunk.duration
                if idx < len(move) - 1:
                    middle += "(" + str(chunk.duration) + ")"
                else:
                    recovery += str(chunk.duration)

    target.write(str(startup) + " " + middle + " " + recovery + ". Total duration: " + str(total_duration) + "\n")
    target.write("\tduration: " + str(attack_timeline))
    target.write(" blockstun: " + str(block_timeline))
    target.write(" diff: " + str(block_timeline - attack_timeline))
    target.write("\n")

print "DONE"


