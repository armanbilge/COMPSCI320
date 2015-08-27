# Arman Bilge
# abil933
# 8079403
# COMPSCI 320 Assignment 3
# Efficiently finds the nearest pair of points on a globe

import sys
import math
import itertools as it
import operator as op
from collections import namedtuple

def distance(x, y):
    return math.acos(x.sin * y.sin + x.cos * y.cos * math.cos(x.lon - y.lon)) * 6370.69348565306

def min_pair(pairs):
    return min(pairs, key=op.itemgetter(2))

def closest_pair(loci):

    n = len(loci)

    if n <= 3:
        return min_pair((x, y, distance(x, y)) for x, y in it.combinations(loci, 2))

    L, R = loci[:n//2], loci[n//2:]
    split = R[-1].lat

    closest = min_pair((closest_pair(L), closest_pair(R)))
    loci = (locus for locus in loci if abs(locus.lat - split) < closest[2])
    pairs = it.chain((closest,), ((x, y, distance(x, y)) for x, y in it.combinations(loci, 2)))

    return min_pair(pairs)

Locus = namedtuple('Locus', ('city', 'lat', 'lon', 'sin', 'cos'))

N = int(sys.stdin.readline())
C = it.count(1)
while N > 0:
    loci = []
    for _ in range(N):
        l = sys.stdin.readline().split()
        lat, lon = map(float, l[-2:])
        sin, cos = math.sin(math.radians(lat)), math.cos(math.radians(lat))
        city = ' '.join(l[:-2])
        loci.append(Locus(city, lat, lon, sin, cos))
    loci.sort(key=op.attrgetter('lat'))
    a, b, d = closest_pair(loci)
    a, b = sorted([a.city, b.city])
    print('Scenario {}:'.format(next(C)))
    print('Closest pair: {} {}'.format(a, b))
    print('Distance: {0:.1f}'.format(d))
    N = int(sys.stdin.readline())
