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
        hitstunCH = ""  #create_hitstun_ch_text(damage_list)
        untechCH = ""   #create_untech_ch_text(damage_list)

        target.write("\n |damage=" + damage + "|p1=" + p1 + "|p2=" + p2)
        target.write("\n |level=" + level + "|attribute=" + attribute + "|guard=|invul=" + inv_text)
        target.write(
            "\n |startup=" + str(startup) + "|active=" + middle + "|recovery=" + recovery + "|frameAdv=" + frame_adv)
        target.write("\n |blockstun=" + blockstun + "|blockstop=" + blockstop + "|hitstop=" + hitstop + "|hitstopCH=" + hitstopCH)
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


def create_attr_text(attr):
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


def create_hitstun_text(damage_list):
    if len(damage_list) == 0:
        return ""
    hitstun_str = ""
    multiplier = 1
    current_hitstun = get_hitstun_text(damage_list[0])

    for attack_info in damage_list[1:]:
        if current_hitstun == get_hitstun_text(attack_info):
            multiplier += 1
        else:
            hitstun_str = append_new_value(hitstun_str, current_hitstun, multiplier)
            current_hitstun = get_hitstun_text(attack_info)
            multiplier = 1

    if len(hitstun_str) == 0:
        hitstun_str = current_hitstun
    else:
        hitstun_str = append_new_value(hitstun_str, current_hitstun, multiplier)
    return hitstun_str


def get_hitstun_text(attack_info):
    text = ""
    hit_effects = attack_info.normalHitEffects
    if hit_effects.groundHitAni == 0 or hit_effects.groundHitAni is None:
        if hit_effects.stagger is not None and hit_effects.stagger > 0:
            text = "Stagger " + str(hit_effects.stagger)
        else:
            text = str(attack_info.get_hitstun())
    elif hit_effects.groundHitAni == 2:
        text = "Stagger " + str(attack_info.get_untech())
    elif hit_effects.groundHitAni == 3:  # forces crouch. so far we don't do anything with this info
        text = str(attack_info.get_hitstun())
    elif hit_effects.groundHitAni == 6:
        text = "Spin Fall " + str(hit_effects.spinFall)
    else:
        text = "Launch"
    return text


def create_untech_text(damage_list):
    if len(damage_list) == 0:
        return ""
    untech_str = ""
    multiplier = 1
    current_untech = get_untech_text(damage_list[0])

    for attack_info in damage_list[1:]:
        if current_untech == get_untech_text(attack_info):
            multiplier += 1
        else:
            untech_str = append_new_value(untech_str, current_untech, multiplier)
            current_untech = get_untech_text(attack_info)
            multiplier = 1

    if len(untech_str) == 0:
        untech_str = current_untech
    else:
        untech_str = append_new_value(untech_str, current_untech, multiplier)
    return untech_str


def get_untech_text(attack_info):
    text = ""
    hit_effects = attack_info.normalHitEffects
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
            text = text + " " + str(hit_effects.cornerStick)
    if hit_effects.slide is not None and hit_effects.slide > 0:
        text = text + " + Slide " + str(hit_effects.slide)
    if hit_effects.knockdown is not None and hit_effects.knockdown > 0:
        text = text + " + Down " + str(hit_effects.knockdown)

    return text


def fill_hitstop(info_list):
    to_return = ""
    current_hitstop = None
    current_bonus_blockstop = None
    current_bonus_hitstop = None
    multiplier = 0
    for i, info in enumerate(info_list):
        if i == 0:
            current_hitstop = info.get_hitstop()
            current_bonus_blockstop = info.bonusBlockstop
            current_bonus_hitstop = info.bonusHitstop
            multiplier = 1
        elif current_hitstop == info.get_hitstop() and current_bonus_blockstop == info.bonusBlockstop and \
                current_bonus_hitstop == info.bonusHitstop:
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
            current_hitstop = info.get_hitstop()
            current_bonus_blockstop = info.bonusBlockstop
            current_bonus_hitstop = info.bonusHitstop
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


def create_p1_text(damage_list):
    if len(damage_list) == 0:
        return ""

    p1_str = ""
    current_p1 = str(damage_list[0].get_p1())
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_p1 == str(attack_info.get_p1()):
            multiplier += 1
        else:
            p1_str = append_new_value(p1_str, current_p1, multiplier)
            current_p1 = str(attack_info.get_p1())
            multiplier = 1

    if len(p1_str) == 0:
        p1_str = current_p1
    else:
        p1_str = append_new_value(p1_str, current_p1, multiplier)
    return p1_str


def append_new_value(base_str, new_value, new_multiplier):
    if len(base_str) != 0:
        base_str = base_str + ", "
    base_str = base_str + str(new_value)
    if new_multiplier > 1:
        base_str = base_str + "*" + str(new_multiplier)
    return base_str


def create_p2_text(damage_list):
    if len(damage_list) == 0:
        return ""

    p2_str = ""
    p2_once = damage_list[0].p2Once
    current_p2 = str(damage_list[0].get_p2())
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_p2 == str(attack_info.get_p2()) and p2_once == attack_info.p2Once:
            multiplier += 1
        else:
            p2_str = append_new_p2(p2_str, current_p2, p2_once, multiplier)
            if attack_info.p2Once:
                p2_str = p2_str + " (Once)"
            current_p2 = str(attack_info.get_p2())
            p2_once = attack_info.p2Once
            multiplier = 1

    if len(p2_str) == 0:
        p2_str = current_p2
        if p2_once:
            p2_str = p2_str + " (Once)"
    else:
        p2_str = append_new_p2(p2_str, current_p2, p2_once, multiplier)

    return p2_str


def append_new_p2(base_p2, new_p2, new_p2_once, new_multiplier):
    if len(base_p2) != 0:
        base_p2 = base_p2 + ", "
    base_p2 = base_p2 + new_p2
    if new_p2_once:
        base_p2 = base_p2 + " (Once)"
    if new_multiplier > 1:
        base_p2 = base_p2 + "*" + str(new_multiplier)
    return base_p2


def create_blockstop_text(damage_list):
    if len(damage_list) == 0:
        return ""

    blockstop_str = ""
    current_blockstop = str(damage_list[0].get_hitstop())
    current_bonus_blockstop = damage_list[0].bonusBlockstop
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_blockstop == str(attack_info.get_hitstop()) and \
                current_bonus_blockstop == attack_info.bonusBlockstop:
            multiplier += 1
        else:
            blockstop_str = append_new_blockstop(blockstop_str, current_blockstop, current_bonus_blockstop, multiplier)
            current_blockstop = str(attack_info.get_hitstop())
            current_bonus_blockstop = attack_info.bonusBlockstop
            multiplier = 1

    if len(blockstop_str) == 0:
        blockstop_str = current_blockstop
        if current_bonus_blockstop is not None and current_bonus_blockstop > 0:
            sign = "+" if current_bonus_blockstop > 0 else ""
            blockstop_str = blockstop_str + "/" + sign + str(current_bonus_blockstop)
    else:
        blockstop_str = append_new_blockstop(blockstop_str, current_blockstop, current_bonus_blockstop, multiplier)
    return blockstop_str


def append_new_blockstop(base_blockstop, new_blockstop, new_bonus_blockstop, new_multiplier):
    if len(base_blockstop) != 0:
        base_blockstop = base_blockstop + ", "
    base_blockstop = base_blockstop + new_blockstop
    if new_bonus_blockstop is not None and new_bonus_blockstop > 0:
        sign = "+" if new_bonus_blockstop > 0 else ""
        base_blockstop = base_blockstop + "/" + sign + str(new_bonus_blockstop)
    if new_multiplier > 1:
        base_blockstop = base_blockstop + "*" + str(new_multiplier)
    return base_blockstop


def create_hitstop_text(damage_list):
    if len(damage_list) == 0:
        return ""

    hitstop_str = ""
    current_hitstop = damage_list[0].bonusHitstop
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_hitstop == attack_info.bonusHitstop:
            multiplier += 1
        else:
            hitstop_str = append_new_hitstop(hitstop_str, current_hitstop, multiplier)
            current_hitstop = attack_info.bonusHitstop
            multiplier = 1

    if len(hitstop_str) == 0:
        if current_hitstop is not None:
            sign = "+" if current_hitstop >= 0 else ""
            hitstop_str = sign + str(current_hitstop)
    else:
        hitstop_str = append_new_hitstop(hitstop_str, current_hitstop, multiplier)
    return hitstop_str


def create_hitstop_ch_text(damage_list):
    if len(damage_list) == 0:
        return ""

    hitstop_str = ""
    current_hitstop = damage_list[0].bonusHitstopCH
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_hitstop == attack_info.bonusHitstopCH:
            multiplier += 1
        else:
            hitstop_str = append_new_hitstop(hitstop_str, current_hitstop, multiplier)
            current_hitstop = attack_info.bonusHitstopCH
            multiplier = 1

    if len(hitstop_str) == 0:
        if current_hitstop is not None:
            sign = "+" if current_hitstop >= 0 else ""
            hitstop_str = sign + str(current_hitstop)
    else:
        hitstop_str = append_new_hitstop(hitstop_str, current_hitstop, multiplier)
    return hitstop_str


def create_attack_level_text(damage_list):
    if len(damage_list) == 0:
        return ""

    attack_level_str = ""
    current_attack_level = str(damage_list[0].attackLevel)
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_attack_level == str(attack_info.attackLevel):
            multiplier += 1
        else:
            attack_level_str = append_new_value(attack_level_str, current_attack_level, multiplier)
            current_attack_level = str(attack_info.attackLevel)
            multiplier = 1

    if len(attack_level_str) == 0:
        attack_level_str = current_attack_level
    else:
        attack_level_str = append_new_value(attack_level_str, current_attack_level, multiplier)
    return attack_level_str


def append_new_hitstop(base_hitstop, new_hitstop, new_multiplier):
    if len(base_hitstop) > 0:
        base_hitstop = base_hitstop + ", "
    if new_hitstop is not None:
        sign = "+" if new_hitstop >= 0 else ""
        base_hitstop = base_hitstop + sign + str(new_hitstop)
    if new_multiplier > 1:
        base_hitstop = base_hitstop + "*" + str(new_multiplier)
    return base_hitstop


def create_attribute_text(damage_list):
    if len(damage_list) == 0:
        return ""

    attribute_str = ""
    current_attribute = damage_list[0].attribute
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_attribute == attack_info.attribute:
            multiplier += 1
        else:
            attribute_str = append_new_value(attribute_str, create_attr_text(current_attribute), multiplier)
            current_attribute = attack_info.attribute
            multiplier = 1

    if len(attribute_str) == 0:
        attribute_str = create_attr_text(current_attribute)
    else:
        attribute_str = append_new_value(attribute_str, create_attr_text(current_attribute), multiplier)
    return attribute_str


def create_blockstun_text(damage_list):
    if len(damage_list) == 0:
        return ""

    blockstun_str = ""
    current_blockstun = str(damage_list[0].get_blockstun())
    multiplier = 1
    for attack_info in damage_list[1:]:
        if current_blockstun == str(attack_info.get_blockstun()):
            multiplier += 1
        else:
            blockstun_str = append_new_value(blockstun_str, current_blockstun, multiplier)
            current_blockstun = str(attack_info.get_blockstun())
            multiplier = 1

    if len(blockstun_str) == 0:
        blockstun_str = current_blockstun
    else:
        blockstun_str = append_new_value(blockstun_str, current_blockstun, multiplier)
    return blockstun_str
