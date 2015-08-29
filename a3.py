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

K = 6370.693485653059
twopi = 2 * math.pi

def normalized(rad):
    return (rad + math.pi) % twopi - math.pi

def distance(x, y):
    return math.acos(min(max(x.sin * y.sin + x.cos * y.cos * math.cos(x.lon - y.lon), -1), 1)) * K

def lat_distance(x, ysin, ycos):
    return math.acos(min(max(x.sin * ysin + x.cos * ycos, -1), 1)) * K

def lon_angle(d, sin2x, cos2x):
    return math.acos(min(max((math.cos(d / K) - sin2x) / cos2x, -1), 1))

def in_bounds(theta, a, b):
    if theta < a:
        theta += twopi
    return p_theta <= a + b

def closest_pair(loci, loci_):

    n = len(loci)

    if n <= 3:
        return min_pair((x, y, distance(x, y)) for x, y in it.combinations(loci, 2))

    L, R = loci[:n//2], loci[n//2:]
    split = R[-1].lat
    L_, R_ = [l for l in loci_ if l in L], [r for r in loci_ if r in R]

    sin_split, cos_split = math.sin(split), math.cos(split)
    sin2split, cos2split = sin_split * sin_split, cos_split * cos_split

    closest = min(closest_pair(L, L_), closest_pair(R, R_), key=op.itemgetter(2))

    L = (l for l in L_ if lat_distance(l, sin_split, cos_split) < closest[2])
    R = [r for r in R_ if lat_distance(r, sin_split, cos_split) < closest[2]]
    lenR = len(R)
    i = 0
    def inc():
        i = i + 1 % lenR
    for x in L:
        theta = lon_angle(closest[2], sin2split, cos2split)
        a, b = normalized(x.lon - theta)
        while a > R[i].lon:
            inc()


    loci = (locus for locus in loci if lat_distance(locus, sin_split, cos_split) < closest[2])
    pairs = ((x, y, distance(x, y)) for x, y in it.combinations(loci, 2))
    pairs = it.chain((closest,), pairs)

    return min_pair(pairs)

Locus = namedtuple('Locus', ('city', 'lat', 'lon', 'sin', 'cos'))

N = int(sys.stdin.readline())
C = it.count(1)
while N > 0:
    loci = []
    for _ in range(N):
        l = sys.stdin.readline().split()
        lat, lon = map(math.radians, map(float, l[-2:]))
        sin, cos = math.sin(lat), math.cos(lat)
        city = ' '.join(l[:-2])
        loci.append(Locus(city, lat, lon, sin, cos))
    loci.sort(key=op.attrgetter('lat'))
    a, b, d = closest_pair(loci, sorted(loci, key=op.attrgetter('lon')))
    a, b = sorted([a.city, b.city])
    print('Scenario {}:'.format(next(C)))
    print('Closest pair: {} {}'.format(a, b))
    print('Distance: {0:.1f}'.format(d))
    N = int(sys.stdin.readline())
