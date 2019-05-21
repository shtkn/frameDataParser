Used to parse the results of dantarion's bbtool into numbers most fighting game players are familiar with.

## How to Run
parseAttack.py assumes you have annotated scr_*.py files (compare the ones in ./input to the ones ./output for examples) that mark which sprites have attackboxes associated with them. Each character has 2 files, one for the character, and one for teh character's effects (like projectiles and other graphics).

Change the values in main() to point at your source files (effect_source and char_source) to parse values for that character. Output will be in ${char_source}_out.txt

### How to make annotated scr_*.py files
Use createAnnotatedDataFiles.py. This assumes you have access to the original scr_*.py files and a list of which sprites have hitboxes in an all_active.txt. Obtain the original files via dantarion's bbtool https://github.com/dantarion/bbtools.
