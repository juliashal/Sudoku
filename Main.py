import random
import pandas as pd
import numpy as np
import itertools

size = 9  # size of square (YxY)
min_num = 1  # minimum number to generate
max_num = 9  # maximum number to generate

rows = [set() for i in range(0, size)]
cols = [set() for i in range(0, size)]
list = [None]*size*size
cycle_list = [i for i in range(1, size+1)]
random.shuffle(cycle_list)

for x in range(0, size):
    print("Row {}".format(x))
    for y in range(0, size):
        print("Column {}".format(y))
        i = x+y*size

        for a in itertools.cycle(cycle_list):
            if a in cols[x]:
                continue
            elif a in rows[y]:
                continue
            else:
                cols[x].add(a)
                rows[y].add(a)
                list[i] = a
                print(a)
                break

        print(rows)
        print(cols)

print(rows)
print(cols)

# Problem  - Can't iterate back

print(np.array(list).reshape((9, 9)))  # to show as matrix
