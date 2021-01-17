import pyautogui as ag
import itertools as it
import copy
import pickle
import imagextract
import threading
import time
import multiprocessing

ag.PAUSE = 0.04
topleft = (300, 630)
width = 150
height = 150



def proctestcombs(a, L, C):
    for h in reversed(C):
        if a <= len(h):
            word = ""
            for i in h:
                word += text[i[0] + 4 * i[1]]
            if word in wordlists[len(word)]:
                print("cor-word: " + word)
                L.append(h)

def docombs(J):
    print("looping")
    while True:
        if J:
            combs = copy.copy(J)
            first = combs[0]
            ag.moveTo(topleft[0] + width * first[0][0], topleft[1] + height * first[0][1])
            ag.mouseDown()

            for k in first:
                ag.moveTo(topleft[0] + width * k[0], topleft[1] + height * k[1])
            J.remove(first)
            ag.mouseUp()
            # time.sleep(0.1)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    goodcombs = manager.list()

    wordsfile = open("words.txt", "r")
    unstrippedwords = wordsfile.readlines()
    words = set(s.rstrip() for s in unstrippedwords)

    pos = []
    ag.moveTo(topleft[0], topleft[1])




    wordlists = [set() for i in range(100)]
    for j in words:
        wordlists[len(j)].add(j)
    for i in range(4):
        for j in range(4):
            pos.append((i, j))

    infile = open("comb.json", 'rb')
    all_combinations = pickle.load(infile)
    usedwords = set()

    print("trying:" + str(len(all_combinations)) + "combinations")
    print("with longest:" + str(len(all_combinations[-1])))

    input("Press Enter to continue...")

    text = list(imagextract.readtext())

    for i in range(len(text)):
        if text[i] == "j":
            if input("Press y to replace j with p") == "y":
                text[i] = "p"


    def testcombs(a, b=1000):
        for h in reversed(all_combinations):
            if a <= len(h) < b:
                word = ""
                for i in h:
                    word += text[i[0] + 4 * i[1]]
                if word in wordlists[len(word)]:
                    print("cor-word: " + word)
                    goodcombs.append(h)


    thread = multiprocessing.Process(target=docombs, args=[goodcombs])
    thread1 = threading.Thread(target=testcombs, args=(1, 7))
    thread2 = threading.Thread(target=testcombs, args=[7, 10])
    thread3 = multiprocessing.Process(target=proctestcombs, args=[10, goodcombs, all_combinations])


    try:
        thread.start()
        thread3.start()
        thread2.start()
        thread1.start()
    except:
       print("Error: unable to start thread(s)")

    print("ok")

