import os

SPRITE_START = "sprite('"
SPRITE_MID = "', "
SPRITE_END = ")"

def main():
    attackHitboxFile = open("all_active_1_5.txt", "r")
    contents = attackHitboxFile.readlines()
    charDictionarySet = {}
    currentChar = ''
    currentSet = None
    for line in contents:
        if line.strip().endswith(" starts here!"):
            char = line.split(" ")[0]
            # print char
            currentSet = set()
            charDictionarySet[char] = currentSet
        elif currentSet is None:
            continue
        else:
            currentSet.add(line.strip())
            # print line.strip()
    # print charDictionarySet.keys()

    outputDir = "./annotated/"
    inputDir = "./input/"

    fileList = os.listdir(inputDir)
    pattern = "*.py"
    # for entry in fileList:
    #     if fnmatch.fnmatch(entry, pattern):
    #         print entry
    #         print entry[entry.index("_")+1:entry.__len__()-3]

    fileList.remove("scr_ahe.py")   # some strange characters in Heart's files, skipping for now
    fileList.remove("scr_aheea.py")
    for entry in fileList:
        source = open(inputDir + entry, "r")
        target = open(outputDir + entry, "w")
        contents = source.readlines()
        fileAbbr = entry[entry.index("_") + 1:entry.__len__() - 3]
        if fileAbbr.__len__() > 3:
            fileAbbr = fileAbbr[0:3]
        if not charDictionarySet.__contains__(fileAbbr):
            print "Couldn't find: " + fileAbbr
            continue
        strBuffer = ""
        currentSet = charDictionarySet[fileAbbr]
        prevFrameCount = 1
        for line in contents:
            if line.__contains__("@State"):
                prevFrameCount = 1  # new move, restart frame counter
            if line.__contains__(SPRITE_START):
                # check if this sprite has a hitbox
                # find it's duration
                # print line
                start = line.index(SPRITE_START) + SPRITE_START.__len__()
                end = line.index(SPRITE_MID)
                sprite = line[start: end]
                # print sprite
                numberStart = line.index(SPRITE_MID) + SPRITE_MID.__len__()
                numberEnd = line.index(SPRITE_END)
                duration = int(line[numberStart:numberEnd])
                # print duration
                newFrameCount = prevFrameCount+duration-1
                line = line.strip("\n") + "\t# " + str(prevFrameCount) + "-" + str(newFrameCount)
                prevFrameCount = newFrameCount + 1
                if currentSet.__contains__(sprite):
                    line = line[0:] + "\t **attackbox here**"

                line += "\n"

            # print line
            target.write(line)

    print "DONE"


if __name__ == "__main__":
    main()
