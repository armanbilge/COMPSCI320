import sys
import itertools as it
import operator as op
from collections import namedtuple

Triangle = namedtuple('Triangle', ('a', 'b', 'c', 'g'))
triangle = sorted(it.chain.from_iterable((Triangle(x, y, z, g) for x, y, z in it.permutations((a, b, c))) for a, b, c, g in map(str.split, it.starmap(sys.stdin.readline, it.repeat((), int(sys.stdin.readline()))))), key=op.attrgetter('g'))
table = [0] * len(triangle)
table[0] = 1
for i in range(1, len(table)):
    table[i] = 1 + max(table[j] if triangle[i].a == triangle[j].c and triangle[i].g > triangle[j].g else 0 for j in range(i))
print(max(table))
