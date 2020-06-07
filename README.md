Used to parse the results of dantarion's bbtools into numbers most fighting game players are familiar with.

## How to Run
parseAttack.py assumes you have annotated scr_*.py files (compare the ones in ./input to the ones ./output for examples) that mark which sprites have attackboxes associated with them. Each character has 2 files, one for the character, and one for teh character's effects (like projectiles and other graphics).

Change the values in main() to point at your source files (effect_source and char_source) to parse values for that character. Output will be in ${char_source}_out.txt

### How to make annotated scr_*.py files
Use createAnnotatedDataFiles.py. This assumes you have access to the original scr_*.py files and a list of which sprites have hitboxes in an all_active.txt. Obtain the original files via dantarion's bbtool https://github.com/dantarion/bbtools.

### How to make all_active
Use findAllActive.py to generate all_active.txt, but if worst comes to worst you can manually edit it yourself.

### Making Changes
This code will break if the output of bbtools changes (which it will as more functions get actual names). You will need to modify parseAttack.py to account for this. parseAttackTest.py has a bunch of unit tests that show how things are expected to work right now. Once changes to bbtools happens, we can use the tests as a way to experiment with making changes to parseAttack.py.
