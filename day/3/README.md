# Solutions:

### All

#### Part 1

first, iterates over each line in the file and splits it in half into 'r1' 'r2',
representing the two rucksacks each elf is carrying.

then it turns the strings int lists, and finds the intersection between the two of
them, i.e. the items that are in both rucksacks.

once it funds the intersection, it finds that item's priority in the priority dict,
and adds it to the running sum.

#### Part 2

first, it stores each collection of 3 lines from the input in a list

finally, it finds the intersection of the three lists, finds the item's priority, and
adds it to the running sum.
