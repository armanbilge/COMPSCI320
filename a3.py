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
    lat1, lon1, lat2, lon2 = x.lat, x.lon, y.lat, y.lon
    theta = lon1 - lon2
    dist = math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(theta))
    if dist > 1:
        dist = 0
    elif dist < -1:
        dist = math.pi
    else:
        dist = math.acos(dist)
    dist = math.degrees(dist) * 60 * 1.1515 * 1.609344
    return dist

def min_pair(pairs):
    return min(pairs, key=lambda p: p[2])

def closest_pair(loci):

    n = len(loci)

    if n <= 3:
        return min_pair((x, y, distance(x, y)) for x, y in it.combinations(loci, 2))

    L, R = loci[:n//2], loci[n//2:]
    split = R[-1].lat

    closest = min(closest_pair(L), closest_pair(R), key=op.itemgetter(2))
    loci = (locus for locus in loci if abs(locus.lat - split) < closest[2])
    pairs = it.chain([closest], ((x, y, distance(x, y)) for x, y in it.combinations(loci, 2)))

    return min_pair(pairs)

Locus = namedtuple('Locus', ['city', 'lat', 'lon'])

N = int(sys.stdin.readline())
C = it.count(1)
while N > 0:
    loci = []
    for _ in range(N):
        l = sys.stdin.readline().split()
        lat, lon = map(float, l[-2:])
        city = ' '.join(l[:-2])
        loci.append(Locus(city, lat, lon))
    loci.sort(key=op.attrgetter('lat'))
    a, b, d = closest_pair(loci)
    a, b = sorted([a.city, b.city])
    print('Scenario {}:'.format(next(C)))
    print('Closest pair: {} {}'.format(a, b))
    print('Distance: {0:.1f}'.format(d))
    N = int(sys.stdin.readline())
