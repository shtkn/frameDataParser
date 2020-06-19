import os
from writeAttacks import *

SPRITE_START = "    sprite('"
SPRITE_MID = "', "
SPRITE_END = ")"
HAS_HITBOX = "**attackbox here**"
GFX_START = "GFX_0('"
CALL_SUBROUTINE_STARTC = "CallSubroutine('"
CALL_SUBROUTINE_STARTc = "callSubroutine('"


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
        self.isWallBounce = False
        self.isCornerBounce = False
        self.isWallBounceCH = False
        self.isCornerBounceCH = False
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
            self.isWallBounce = False
            self.isCornerBounce = False
            self.isWallBounceCH = False
            self.isCornerBounceCH = False

    def is_attackbox(self):
        return self.isAttackBox and (
                self.isNewHit or not self.disableAttackboxes) and not self.disableAttackboxesThisFrame

    def set_values_from_subroutine(self, subroutine):
        if subroutine is None:
            return
        self.landingRecovery = subroutine.landingRecovery
        self.attackInfo = subroutine.attackInfo

    def create_frame_chunk(self):
        if self.is_attackbox():
            chunk = ActiveFrames(self.duration, self.isNewHit, copy.copy(self.attackInfo))
            if not self.isWallBounce:
                chunk.info.normalHitEffects.wallBounce = None
            if not self.isWallBounceCH:
                chunk.info.counterHitEffects.wallBounce = None
            if not self.isCornerBounce:
                chunk.info.normalHitEffects.cornerBounceType = None
            if not self.isCornerBounceCH:
                chunk.info.counterHitEffects.cornerBounceType = None
        else:
            chunk = WaitFrames(self.duration)
        if self.isInv:
            chunk.inv_type = 1 if self.invType == 0 else 2
            chunk.inv_attr = self.invAttr
        return chunk

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


def parse_scr_file(source, move_list, effect_list):
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
            # restart counters

            # state.clear_values(True)
            state = State()
            if "@Subroutine" in line:
                state.isSubroutine = True
        elif state.inUponImmediate and line.startswith(state.uponImmediateIndent + "    "):
            pass    # skip anything not under UPON_IMMEDIATE
        elif not state.exitState and SPRITE_START in line:
            if state.duration > 0:
                chunk = state.create_frame_chunk()
                frame_chunks.append(chunk)
                if isinstance(chunk, ActiveFrames):
                    state.isNewHit = False
                state.clear_values(False)
            state.duration = get_duration(line)

            if HAS_HITBOX in line:
                state.isAttackBox = HAS_HITBOX in line
        elif not state.exitState:
            if "Recovery()" in line or "Unknown23027()" in line or "DisableAttackRestOfMove()" in line:  # disables active frames until a refreshMultihit
                state.disableAttackboxes = True
                state.isNewHit = False
            elif "StartMultihit()" in line or "DisableAttackThisSprite()" in line:  # turns off these active frames
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
                state.attackInfo.normalHitEffects.hitstun = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown9178(" in line:
                is_wall_bounce = int(line[line.index("(") + 1:line.index(")")])
                state.isWallBounce = is_wall_bounce == 1
            elif "Unknown9180(" in line:
                is_wall_bounce_ch = int(line[line.index("(") + 1:line.index(")")])
                state.isWallBounceCH = is_wall_bounce_ch == 1
            elif "Unknown9156(" in line:
                state.attackInfo.counterHitEffects.hitstun = int(line[line.index("(") + 1:line.index(")")])
            elif "AirUntechableTime(" in line:  # 9166
                state.attackInfo.normalHitEffects.untech = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown9168(" in line:
                state.attackInfo.counterHitEffects.untech = int(line[line.index("(") + 1:line.index(")")])
            elif " Damage(" in line or "\tDamage(" in line:
                state.attackInfo.damage = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown11012(" in line or "MinimumDamagePct(" in line:
                state.attackInfo.minDamage = int(line[line.index("(") + 1:line.index(")")])
            elif "Unknown11092(" in line or "P2OnceOnly(" in line:
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
            elif "Unknown11001(" in line or "AdditionalHitstopOpponent(" in line:
                numbers_start = line.index("(") + 1
                numbers_end = line.index(")")
                numbers = [x.strip() for x in line[numbers_start:numbers_end].split(',')]
                state.attackInfo.bonusBlockstop = int(numbers[0])
                state.attackInfo.bonusHitstop = int(numbers[1])
                state.attackInfo.bonusHitstopCH = int(numbers[2])
            elif "Unknown22004(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(",")
                # print "Landing" + line[number_start: number_end]
                state.landingRecovery = int(line[number_start: number_end]) - 1
            elif GFX_START in line:
                name_start = line.index("('") + 2
                name_end = line.index("',")
                number_start = line.index(", ") + 2
                number_end = line.index(")")
                # if gfx_subroutine = -1, then this gfx is on the same "thread" as this one
                gfx_thread = int(line[number_start:number_end])
                # print "GFX " + line[name_start:name_end]
                frame_chunks.append(SubroutineCall(line[name_start:name_end], gfx_thread == -1))
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
            elif "AirHitstunAnimation(" in line:    # 9334
                number_start = line.index("(") + 1
                number_end = line.index(")")
                animation_type = int(line[number_start:number_end])
                state.attackInfo.normalHitEffects.airHitAni = animation_type
                if animation_type == 12:
                    state.isWallBounce = True
            elif "Unknown9336(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                animation_type = int(line[number_start:number_end])
                state.attackInfo.counterHitEffects.airHitAni = animation_type
                if animation_type == 12:
                    state.isWallBounceCH = True
            elif "GroundedHitstunAnimation(" in line:   # 9322
                number_start = line.index("(") + 1
                number_end = line.index(")")
                animation_type = int(line[number_start:number_end])
                state.attackInfo.normalHitEffects.groundHitAni = animation_type
                if animation_type == 12:
                    state.isWallBounce = True
            elif "Unknown9324(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                animation_type = int(line[number_start:number_end])
                state.attackInfo.counterHitEffects.groundHitAni = animation_type
                if animation_type == 12:
                    state.isWallBounceCH = True
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
            elif "Unknown9118(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.normalHitEffects.groundBounce = int(line[number_start:number_end])
            elif "Unknown9120(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.groundBounce = int(line[number_start:number_end])
            elif "ExitState()" in line:
                # we assume all the lines above this are for the move on block/whiff. Anything after is on hit
                state.exitState = True
            elif "Unknown9190(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.normalHitEffects.groundBounce = int(line[number_start:number_end])
            elif "Unknown9192(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.groundBounce = int(line[number_start:number_end])
            elif "Unknown9130(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                amt = int(line[number_start:number_end])
                amt = 24 if amt == 1 else amt + 14
                state.attackInfo.normalHitEffects.staggerFallStart = amt
            elif "Unknown9132(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                amt = int(line[number_start:number_end])
                amt = 24 if amt == 1 else amt + 14
                state.attackInfo.counterHitEffects.staggerFallStart = amt
            elif "Unknown9142(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.normalHitEffects.stagger = int(line[number_start:number_end])
            elif "Unknown9144(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.stagger = int(line[number_start:number_end])
            elif "Unknown9202(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.normalHitEffects.slide = int(line[number_start:number_end]) + 19
            elif "Unknown9204(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.slide = int(line[number_start:number_end]) + 19
            elif "Unknown9310(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                amt = int(line[number_start:number_end])
                amt = 24 if amt == 1 else amt + 14
                state.attackInfo.normalHitEffects.knockdown = amt
            elif "Unknown9312(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                amt = int(line[number_start:number_end])
                amt = 24 if amt == 1 else amt + 14
                state.attackInfo.counterHitEffects.knockdown = amt
            elif "Unknown9346(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.isCornerBounce = int(line[number_start:number_end]) == 1
            elif "Unknown9348(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.isCornerBounceCH = int(line[number_start:number_end]) == 1
            elif "Unknown9362(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.normalHitEffects.cornerBounceType = int(line[number_start:number_end])
            elif "Unknown9363(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.cornerBounceType = int(line[number_start:number_end])
            elif "Unknown9364(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.normalHitEffects.cornerStick = int(line[number_start:number_end])
            elif "Unknown9365(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.cornerStick = int(line[number_start:number_end])
            elif "FatalCounter(" in line:
                number_start = line.index("(") + 1
                number_end = line.index(")")
                state.attackInfo.counterHitEffects.fatal = line[number_start:number_end] == "1"
            elif "Unknown30072(" in line:  # i think this is attackDefaultsCrushAttack()? Basically Attack Level 3
                state.attackInfo.attackLevel = 3
                state.attackInfo.bonusHitstop = 0
                state.attackInfo.bonusBlockstop = 0
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
            elif "Unknown17003(" in line:   # attack defaults air special?
                state.attackInfo.p1 = 80
                state.attackInfo.attribute = [True, False, False, False, False]
            elif "Unknown17010(" in line:   # attack defaults Counter Assault
                state.attackInfo.attackLevel = 4
                state.invType = 0
                state.isInv = True
                state.attackInfo.p1 = 50
                state.attackInfo.damage = 0
                state.attackInfo.normalHitEffects.groundHitAni = 9
                state.attackInfo.normalHitEffects.airHitAni = 9
                state.attackInfo.attribute = [False, True, False, False, False]
            elif "Unknown17021(" in line:  # attack defaults Exceel Accel?
                state.attackInfo.attackLevel = 5    # i have no idea, just put something so it doensn't crash
            elif "Unknown17024(" in line:   # attack defaults reversal action
                state.invType = 0
                state.isInv = True
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
        attack_info.bonusBlockstop = 0 if attack_info.bonusBlockstop is None else attack_info.bonusBlockstop
        attack_info.bonusHitstop = 0 if attack_info.bonusHitstop is None else attack_info.bonusHitstop
        chunk = state.create_frame_chunk()
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


def parse_files(source_dir, target_dir, file_list):

    for file_name in file_list:
        # Parse effects
        if not os.path.isfile(source_dir + "/" + file_name + "ea.py") or \
                not os.path.isfile(source_dir + "/" + file_name + ".py"):
            print "file" + source_dir + "/" + file_name + "ea.py or " + \
                  file_name + ".py does not exist"
            continue
        effect_source = open(source_dir + "/" + file_name + "ea.py", "r")
        effect_list = OrderedDict()
        effect_list = parse_scr_file(effect_source, effect_list, effect_list)
        # Parse moves
        char_source = open(source_dir + "/" + file_name + ".py", "r")
        char_target = open(target_dir + "/" + file_name + "_out.txt", "w")
        move_list = OrderedDict()
        move_list = parse_scr_file(char_source, move_list, effect_list)

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
    bbtag_source_dir = "./annotated2_0"
    bbtag_target_dir = "./parsedAttacks"
    bbtag_file_list = [
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
    bbcf_source_dir = "./annotated_bbcf_2_0"
    bbcf_target_dir = "./parsedAttacks_bbcf_2_0"
    bbcf_file_list = [
        "scr_am", "scr_ar", "scr_az", "scr_bl", "scr_bn", "scr_ca", "scr_ce", "scr_es", "scr_ha", "scr_hb",
        "scr_hz", "scr_iz", "scr_jb", "scr_jn", "scr_kg", "scr_kk", "scr_lc", "scr_ma", "scr_mi", "scr_mk",
        "scr_mu", "scr_no", "scr_nt", "scr_ny", "scr_ph", "scr_pt", "scr_rc", "scr_rg", "scr_rl", "scr_rm",
        "scr_su", "scr_tb", "scr_tg", "scr_tk", "scr_tm", "scr_vh"
    ]
    test_source_dir = "."
    test_target_dir = "."
    test_file_list = ["testfile"]

    source_dir = test_source_dir
    target_dir = test_target_dir
    file_list = test_file_list
    parse_files(source_dir, target_dir, file_list)