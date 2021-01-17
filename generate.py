import copy
import pickle
import sys

all_combinations = [[(0, 0)], [(1, 0)], [(2, 0)], [(3, 0)], [(0, 1)], [(1, 1)], [(2, 1)], [(3, 1)]]
all_combinations += [[(0, 2)], [(1, 2)], [(2, 2)], [(3, 2)], [(0, 3)], [(1, 3)], [(2, 3)], [(3, 3)]]
print(all_combinations)
all_unchecked_combinations = all_combinations
for i in range(11):
    print('test' + str(i))
    newcomb = []
    newcombold = []
    for idx, j in enumerate(all_unchecked_combinations):
        sys.stdout.write("\r" + str(idx) + "of" + str(len(all_unchecked_combinations)))
        sys.stdout.flush()


        if j[-1][0] + 1 <= 3 and (j[-1][0] + 1, j[-1][1]) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] + 1, j[-1][1]))
            newcomb.append(new)

        if j[-1][1] + 1 <= 3 and (j[-1][0], j[-1][1] + 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0], j[-1][1] + 1))
            newcomb.append(new)

        if j[-1][1] + 1 <= 3 and j[-1][0] + 1 <= 3 and (j[-1][0] + 1, j[-1][1] + 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] + 1, j[-1][1] + 1))
            newcomb.append(new)

        if j[-1][1] - 1 >= 0 and (j[-1][0], j[-1][1] - 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0], j[-1][1] - 1))
            newcomb.append(new)

        if j[-1][0] - 1 >= 0 and (j[-1][0] - 1, j[-1][1]) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] - 1, j[-1][1]))
            newcomb.append(new)

        if j[-1][0] - 1 >= 0 and j[-1][1] - 1 >= 0 and (j[-1][0] - 1, j[-1][1] - 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] - 1, j[-1][1] - 1))
            newcomb.append(new)

        if j[-1][0] + 1 <= 3 and j[-1][1] - 1 >= 0 and (j[-1][0] + 1, j[-1][1] - 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] + 1, j[-1][1] - 1))
            newcomb.append(new)

        if j[-1][0] - 1 >= 0 and j[-1][1] + 1 <= 3 and (j[-1][0] - 1, j[-1][1] + 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] - 1, j[-1][1] + 1))
            newcomb.append(new)

        newcombold.append(j)

    all_unchecked_combinations = newcomb
    all_combinations += newcombold

all_combinations += all_unchecked_combinations

print("finished")

print("printing")
outfile = open("comb.json", 'wb')
all_combinations = [x for x in all_combinations if 1 < len(x)]
all_combinations.sort(key=len)
pickle.dump(all_combinations, outfile)
outfile.close()
print("done with longest:" + str(len(all_combinations[-1])))