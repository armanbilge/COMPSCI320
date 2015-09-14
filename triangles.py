import sys
import itertools as it
import operator as op

def repeatfunc(func, times):
    return it.starmap(func, it.repeat((), times))

T = sorted(tuple(sorted(l[:3])), l[-1] for l in map(str.split, repeatfunc(sys.stdin.readline, int(sys.stdin.readline()))), key=op.itemgetter(1))
