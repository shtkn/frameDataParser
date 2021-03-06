import os
import struct


def isContainsAttackBox(source_file):
    jonb = source_file.read(4)     # jonbin files start with 'JONB', make sure this is true
    if jonb != "JONB":
        return False
    test = source_file.read(1)
    result = struct.unpack(">B", test)
    source_file.read(1)    # skip padding
    source_file.read(32*result[0])  # skip sprite names
    source_file.read(6)    # skip padding \x14 \x01 \x00 \x?? \x00 \x00
    source_file.read(2)    # skip number of hurtboxes
    attackbox_count = source_file.read(2)   # this is number of hitboxes
    result = struct.unpack(">H", attackbox_count)
    # print file_name + " attackbox count\n\t" + str(result[0])
    source_file.close()
    return result[0] > 0


def findActiveForFolder(source_dir):
    file_list = os.listdir(source_dir)
    contains_attackboxes = []
    for file_name in file_list:
        if file_name.lower().endswith(".jonbin") and isContainsAttackBox(open(source_dir + "/" + file_name, "r")):
            contains_attackboxes.append(file_name[:-len(".jonbin")] + "\n")

    return sorted(contains_attackboxes)


def main():
    target_name = "bbcf_all_active.txt"
    target = open(target_name, "w")
    base_folder = "/Users/shtkn/Documents/BBCF_CharData"
    folders = ["am", "ar", "az", "bl", "bn",
               "ca", "ce", "es", "ha", "hb",
               "hz", "iz", "jb", "jn", "kg",
               "kk", "lc", "ma", "mi", "mk",
               "mu", "no", "nt", "ny", "ph",
               "pt", "rc", "rg", "rl", "rm",
               "su", "tb", "tg", "tk", "tm",
               "vh"
               ]
    for folder in folders:
        active = findActiveForFolder(base_folder + os.path.sep + folder + "_scr" + os.path.sep + "char_" + folder + "_col")
        target.write(folder + " starts here\n")
        target.writelines(active)


if __name__ == "__main__":
    main()
