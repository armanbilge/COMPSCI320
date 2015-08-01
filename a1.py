# Arman Bilge
# abil933
# 8079403
# COMPSCI 320 Assignment 1
# Implements the Gale-Shapley algorithm

import sys
import itertools as it

def gale_shapley(blue, pink):

    n = len(blue)
    free_blue = set(range(n))
    free_pink = set(range(n))
    pairs = set()

    def engage(b, p):
        free_blue.remove(b)
        free_pink.remove(p)
        pairs.add((b,p))

    def free(pair):
        b, p = pair
        free_blue.add(b)
        free_pink.add(p)
        pairs.remove(pair)

    while any(len(blue[i]) > 0 for i in free_blue):
        b = next(i for i in free_blue if len(blue[i]) > 0)
        p = blue[b].pop(0)
        if p in free_pink:
            engage(b, p)
        else:
            bp = next(x[0] for x in pairs if x[1] == p)
            if (pink[p].index(b) < pink[p].index(bp)):
                free((bp, p))
                engage(b, p)
    return pairs

for i in it.islice(it.count(), 1, None):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    parse = lambda i: int(i) - 1
    blue = [list(map(parse, sys.stdin.readline().split())) for _ in range(n)]
    pink = [list(map(parse, sys.stdin.readline().split())) for _ in range(n)]
    pairs = sorted(gale_shapley(blue, pink))
    print('Instance {}:'.format(i))
    for p in pairs:
        print(p[1] + 1)
