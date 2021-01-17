import copy
import pickle
import sys
import multiprocessing
import dill
import joblib
from klepto.archives import dir_archive
from _collections import deque

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    newcomb = manager.list()
    newcombold = manager.list()

    all_combinations = [[(0, 0)], [(1, 0)], [(2, 0)], [(3, 0)], [(0, 1)], [(1, 1)], [(2, 1)], [(3, 1)]]
    all_combinations.extend([[(0, 2)], [(1, 2)], [(2, 2)], [(3, 2)], [(0, 3)], [(1, 3)], [(2, 3)], [(3, 3)]])
    print(all_combinations)
    all_unchecked_combinations = all_combinations


def check(part, lnewcomb, lnewcombold):
    c = multiprocessing.current_process().name
    tempnewcomb = []
    tempnewcombold = []
    for idx, j in enumerate(part):
        if j[-1][0] + 1 <= 3 and (j[-1][0] + 1, j[-1][1]) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] + 1, j[-1][1]))
            tempnewcomb.append(new)

        if j[-1][1] + 1 <= 3 and (j[-1][0], j[-1][1] + 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0], j[-1][1] + 1))
            tempnewcomb.append(new)

        if j[-1][1] + 1 <= 3 and j[-1][0] + 1 <= 3 and (j[-1][0] + 1, j[-1][1] + 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] + 1, j[-1][1] + 1))
            tempnewcomb.append(new)

        if j[-1][1] - 1 >= 0 and (j[-1][0], j[-1][1] - 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0], j[-1][1] - 1))
            tempnewcomb.append(new)

        if j[-1][0] - 1 >= 0 and (j[-1][0] - 1, j[-1][1]) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] - 1, j[-1][1]))
            tempnewcomb.append(new)

        if j[-1][0] - 1 >= 0 and j[-1][1] - 1 >= 0 and (j[-1][0] - 1, j[-1][1] - 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] - 1, j[-1][1] - 1))
            tempnewcomb.append(new)

        if j[-1][0] + 1 <= 3 and j[-1][1] - 1 >= 0 and (j[-1][0] + 1, j[-1][1] - 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] + 1, j[-1][1] - 1))
            tempnewcomb.append(new)

        if j[-1][0] - 1 >= 0 and j[-1][1] + 1 <= 3 and (j[-1][0] - 1, j[-1][1] + 1) not in j:
            new = copy.deepcopy(j)
            new.append((j[-1][0] - 1, j[-1][1] + 1))
            tempnewcomb.append(new)

        tempnewcombold.append(j)
    lnewcomb += tempnewcomb
    lnewcombold += tempnewcombold

if __name__ == '__main__':
    for i in range(10):
        print('test ' + str(i))
        newcomb = manager.list()
        newcombold = manager.list()
        step = len(all_unchecked_combinations)//4

        proc1 = multiprocessing.Process(target=check, args=(all_unchecked_combinations[0:step], newcomb, newcombold))

        proc2 = multiprocessing.Process(target=check, args=(all_unchecked_combinations[step + 1:2*step], newcomb, newcombold))

        proc3 = multiprocessing.Process(target=check, args=(all_unchecked_combinations[2*step + 1:3*step], newcomb, newcombold))

        proc4 = multiprocessing.Process(target=check, args=(all_unchecked_combinations[3*step + 1::], newcomb, newcombold))

        proc1.start()
        proc2.start()
        proc3.start()
        proc4.start()

        proc1.join()
        proc2.join()
        proc3.join()
        proc4.join()
        print("proc finished with length " + str(len(newcomb)))
        proc1.kill()
        proc2.kill()
        proc3.kill()
        proc4.kill()
        print("proc killed")

        all_unchecked_combinations = newcomb
        print("newcomb copied")
        all_combinations.extend(newcombold)

    all_combinations.extend(all_unchecked_combinations)

    print("finished with:" + str(len(all_combinations)) + " paths")

    print("printing")

    joblib.dump(copy.copy(all_combinations), "comb_mp")
    print("done with longest:" + str(len(all_combinations[-1])))