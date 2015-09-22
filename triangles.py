import sys
import itertools as it
import operator as op
from collections import namedtuple

Triangle = namedtuple('Triangle', ('a', 'b', 'g'))
triangle = sorted(set(it.chain.from_iterable((Triangle(x, y, g) for x, y, _ in it.permutations((a, b, c))) for a, b, c, g in map(str.split, it.starmap(sys.stdin.readline, it.repeat((), int(sys.stdin.readline())))))), key=op.attrgetter('g'))
table = [1] * len(triangle)
for i, ti in enumerate(triangle[1:], 1):
    tia, tig = ti.a, ti.g
    table[i] = 1 + max(x if tia == tj.b and tig > tj.g else 0 for x, tj in zip(table, triangle[:i]))
print(max(table))
