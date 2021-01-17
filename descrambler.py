import itertools
import re

wordsfile = open("words.txt", "r")
unstrippedwords = wordsfile.readlines()

test="Hsjetguenhni jdoae "

x = []
for s in unstrippedwords:
    print('a').
    x += re.findall(r'^(h?s?j?e?t?g?u?e?n?h?n?i? j?d?o?a?e ?)$', s)

for i in x:
    print(i)