from model import *


def write_file(moves_on_block, target):
    for moveName in moves_on_block:
        move_on_block = moves_on_block[moveName]

        target.write("\n" + moveName + "\n")
        startup, middle, recovery, total_duration, duration_on_block, last_blockstun_frame, inv_list = \
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
                target.write("\nAdditional Hit (projectile?)\n|startup=" + str(result[0]) + "|active=" + result[
                    1] + "|recovery=" + str(result[2]))
                target.write("last blockstun frame: " + str(last_blockstun_frame))

        inv_text = ""
        for inv in move_on_block.hardcoded_inv_list:
            inv_list.append(inv)
        for idx, inv in enumerate(inv_list):
            inv_text = create_inv_text(inv[0], inv[1], inv[2], inv[3],
                                       move_on_block.superflash_list
                                       )
            if idx != len(inv_list) - 1:
                inv_text += "<br/>"
        frame_adv = ""
        if last_blockstun_frame != 0:
            frame_adv = str(last_blockstun_frame - duration_on_block)
            # target.write("\n\tlast blockstun: " + str(last_blockstun_frame))
            # target.write("|frameAdv=" + str(last_blockstun_frame - duration_on_block))
        damage_list = calc_damage_for_move(move_on_block)
        damage = create_damage_text(damage_list)
        p1 = create_p1_text(damage_list)
        p2 = create_p2_text(damage_list)
        level = create_attack_level_text(damage_list)
        blockstop = create_blockstop_text(damage_list)
        hitstop = create_hitstop_text(damage_list)
        hitstopCH = create_hitstop_ch_text(damage_list)
        attribute = create_attribute_text(damage_list)
        blockstun = create_blockstun_text(damage_list)
        hitstun = create_hitstun_text(damage_list)
        untech = create_untech_text(damage_list)
        hitstunCH = create_hitstun_ch_text(damage_list)
        untechCH = create_untech_ch_text(damage_list)

        target.write("\n |damage=" + damage + "|p1=" + p1 + "|p2=" + p2)
        target.write("\n |level=" + level + "|attribute=" + attribute + "|guard=|invul=" + inv_text)
        target.write(
            "\n |startup=" + str(startup) + "|active=" + middle + "|recovery=" + recovery + "|frameAdv=" + frame_adv)
        target.write(
            "\n |blockstun=" + blockstun + "|blockstop=" + blockstop + "|hitstop=" + hitstop + "|hitstopCH=" + hitstopCH)
        target.write("\n |groundHit=" + hitstun + "|airHit=" + untech + "|groundCH=" + hitstunCH + "|airCH=" + untechCH)
        target.write("\n |hitbox=")
        target.write("\n}}\n")


def create_inv_text(inv_start, inv_duration, inv_type, inv_attr, superflash_list):
    inv_type = " Guard" if inv_type == 2 else ""
    inv_attr = create_inv_attr_text(inv_attr)

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


def create_inv_attr_text(attr):
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


def create_attr_value(attr):
    return_value = ""
    if attr is None:
        return return_value
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


def create_hitstun_value(attack_info):
    hit_effects = attack_info.normalHitEffects
    text = ""
    if hit_effects.groundHitAni == 0 or hit_effects.groundHitAni is None:
        text = str(attack_info.get_hitstun())
    elif hit_effects.groundHitAni == 2:
        text = "Stagger " + str(attack_info.get_stagger())
    elif hit_effects.groundHitAni == 3:  # forces crouch. so far we don't do anything with this info
        text = str(attack_info.get_hitstun())
    elif hit_effects.groundHitAni == 6:
        # spin duration = hitstun, falling duration = 16
        text = "Spin Fall " + str(attack_info.get_hitstun() + 16)
    else:
        text = "Launch"
    return text


def create_hitstun_ch_value(attack_info):
    ch_hit_effects = attack_info.counterHitEffects
    text = ""
    if ch_hit_effects.groundHitAni == 0 or ch_hit_effects.groundHitAni is None:
        text = str(attack_info.get_hitstun_ch())
    elif ch_hit_effects.groundHitAni == 2:
        text = "Stagger " + str(attack_info.get_stagger_ch())
    elif ch_hit_effects.groundHitAni == 3:  # forces crouch. so far we don't do anything with this info
        text = str(attack_info.get_hitstun_ch())
    elif ch_hit_effects.groundHitAni == 6:
        # spin duration = hitstun, falling duration = 16
        text = "Spin Fall " + str(attack_info.get_hitstun_ch() + 16)
    else:
        text = "Launch"
    return text


def create_untech_value(attack_info):
    hit_effects = attack_info.normalHitEffects
    text = ""
    if hit_effects.airHitAni == 0 or hit_effects.airHitAni is None:
        text = str(attack_info.get_untech())

    if hit_effects.groundBounce is not None and hit_effects.groundBounce > 0:
        text = text + " + GBounce"
    if hit_effects.airHitAni == 12 or hit_effects.groundHitAni == 12 or hit_effects.wallBounce is not None:
        text = text + " + WBounce"
        if hit_effects.wallBounce > 0:
            text = text + " " + str(hit_effects.wallBounce)
    if hit_effects.cornerStick is not None:
        text = text + " + WStick"
        if hit_effects.cornerStick > 0:
            text = text + " " + str(attack_info.get_corner_stick())
    if hit_effects.slide is not None and hit_effects.slide > 0:
        text = text + " + Slide " + str(attack_info.get_slide())
    if hit_effects.knockdown is not None and hit_effects.knockdown > 0:
        text = text + " + Down " + str(hit_effects.knockdown)

    return text


def create_untech_ch_value(attack_info):
    hit_effects = attack_info.counterHitEffects
    text = ""
    if hit_effects.airHitAni == 0 or hit_effects.airHitAni is None:
        text = str(attack_info.get_untech_ch())

    if hit_effects.groundBounce is not None and hit_effects.groundBounce > 0:
        text = text + " + GBounce"
    if hit_effects.airHitAni == 12 or hit_effects.groundHitAni == 12 or hit_effects.wallBounce is not None:
        text = text + " + WBounce"
        if hit_effects.wallBounce > 0:
            text = text + " " + str(hit_effects.wallBounce)
    if hit_effects.cornerStick is not None:
        text = text + " + WStick"
        if hit_effects.cornerStick > 0:
            text = text + " " + str(attack_info.get_corner_stick_ch())
    if hit_effects.slide is not None and hit_effects.slide > 0:
        text = text + " + Slide " + str(attack_info.get_slide_ch())
    if hit_effects.knockdown is not None and hit_effects.knockdown > 0:
        text = text + " + Down " + str(hit_effects.knockdown)

    return text


def create_untech_helper(hit_effects, base_untech):
    text = ""
    if hit_effects.airHitAni == 0 or hit_effects.airHitAni is None:
        text = str(base_untech)

    if hit_effects.groundBounce is not None and hit_effects.groundBounce > 0:
        text = text + " + GBounce"
    if hit_effects.airHitAni == 12 or hit_effects.groundHitAni == 12 or hit_effects.wallBounce is not None:
        text = text + " + WBounce"
        if hit_effects.wallBounce > 0:
            text = text + " " + str(hit_effects.wallBounce)
    if hit_effects.cornerStick is not None:
        text = text + " + WStick"
        if hit_effects.cornerStick > 0:
            text = text + " " + str(hit_effects.cornerStick)
    if hit_effects.slide is not None and hit_effects.slide > 0:
        text = text + " + Slide " + str(hit_effects.slide)
    if hit_effects.knockdown is not None and hit_effects.knockdown > 0:
        text = text + " + Down " + str(hit_effects.knockdown)

    return text


def create_damage_text(damage_list):
    if len(damage_list) == 0:
        return ""

    damage_str = ""
    current_damage = str(damage_list[0].get_damage())
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_damage == str(attack_info.get_damage()):
            multiplier += 1
        else:
            damage_str = append_new_value(damage_str, current_damage, multiplier)
            current_damage = str(attack_info.get_damage())
            multiplier = 1

    damage_str = append_new_value(damage_str, current_damage, multiplier)
    return damage_str


def create_p2_value(attack_info):
    text = str(attack_info.get_p2())
    if attack_info.p2Once:
        text = text + " (Once)"
    return text


def create_blockstop_value(attack_info):
    text = ""
    if attack_info.get_hitstop() is not None:
        text = str(attack_info.get_hitstop())
    if attack_info.bonusBlockstop is not None and attack_info.bonusBlockstop != 0:
        sign = "+" if attack_info.bonusBlockstop > 0 else ""
        text = text + "/" + sign + str(attack_info.bonusBlockstop)
    return text


def create_bonus_hitstop_value(attack_info):
    if attack_info.attackLevel is None and attack_info.bonusHitstop is None:
        return ""
    value = attack_info.bonusHitstop if attack_info.bonusHitstop is not None else 0
    sign = "+" if value >= 0 else ""
    return sign + str(value)


def create_bonus_hitstop_ch_value(attack_info):
    if attack_info.attackLevel is None and attack_info.bonusHitstopCH is None:
        return ""
    value = attack_info.bonusHitstopCH \
        if attack_info.bonusHitstopCH is not None \
        else ATTACK_LEVEL["hitstopCH"][attack_info.attackLevel]
    sign = "+" if value >= 0 else ""
    return sign + str(value)


def create_p1_text(damage_list):
    p1_list = []
    for attack_info in damage_list:
        p1_list.append(attack_info.get_p1())
    return create_basic_text(p1_list)


def create_p2_text(damage_list):
    p2_list = []
    for attack_info in damage_list:
        p2_list.append(create_p2_value(attack_info))
    return create_basic_text(p2_list)


def create_attack_level_text(damage_list):
    attack_level_list = []
    for attack_info in damage_list:
        attack_level_list.append(attack_info.attackLevel)
    return create_basic_text(attack_level_list)


def create_attribute_text(damage_list):
    attribute_list = []
    for attack_info in damage_list:
        attribute_list.append(create_attr_value(attack_info.attribute))
    return create_basic_text(attribute_list)


def create_blockstun_text(damage_list):
    blockstun_list = []
    for attack_info in damage_list:
        blockstun_list.append(attack_info.get_blockstun())
    return create_basic_text(blockstun_list)


def create_blockstop_text(damage_list):
    blockstop_list = []
    for attack_info in damage_list:
        blockstop_list.append(create_blockstop_value(attack_info))
    return create_basic_text(blockstop_list)


def create_hitstop_text(damage_list):
    hitstop_list = []
    for attack_info in damage_list:
        hitstop_list.append(create_bonus_hitstop_value(attack_info))
    return create_basic_text(hitstop_list)


def create_hitstop_ch_text(damage_list):
    hitstop_ch_list = []
    for attack_info in damage_list:
        hitstop_ch_list.append(create_bonus_hitstop_ch_value(attack_info))
    return create_basic_text(hitstop_ch_list)


def create_hitstun_text(damage_list):
    hitstun_list = []
    for attack_info in damage_list:
        hitstun_list.append(create_hitstun_value(attack_info))
    return create_basic_text(hitstun_list)


def create_untech_text(damage_list):
    untech_list = []
    for attack_info in damage_list:
        untech_list.append(create_untech_value(attack_info))
    return create_basic_text(untech_list)


def create_hitstun_ch_text(damage_list):
    hitstun_ch_list = []
    for attack_info in damage_list:
        hitstun_ch_list.append(create_hitstun_ch_value(attack_info))
    return create_basic_text(hitstun_ch_list)


def create_untech_ch_text(damage_list):
    untech_ch_list = []
    for attack_info in damage_list:
        untech_ch_list.append(create_untech_ch_value(attack_info))
    return create_basic_text(untech_ch_list)


def create_basic_text(value_list):
    if len(value_list) == 0:
        return ""

    value_str = ""
    current_value = str(value_list[0])
    multiplier = 1
    for value in value_list[1:]:
        if current_value == str(value):
            multiplier += 1
        else:
            value_str = append_new_value(value_str, current_value, multiplier)
            current_value = str(value)
            multiplier = 1

    if len(value_str) == 0:
        value_str = current_value
    else:
        value_str = append_new_value(value_str, current_value, multiplier)
    return value_str


def append_new_value(base_str, new_value, new_multiplier):
    if len(base_str) != 0:
        base_str = base_str + ", "
    base_str = base_str + str(new_value)
    if new_multiplier > 1:
        base_str = base_str + "*" + str(new_multiplier)
    return base_str
