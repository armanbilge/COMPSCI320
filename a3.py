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

def distance(x, y):
    return math.acos(min(max(x.sin * y.sin + x.cos * y.cos * math.cos(x.lon - y.lon), -1), 1)) * K

def lat_distance(x, ysin, ycos):
    return math.acos(min(max(x.sin * ysin + x.cos * ycos, -1), 1)) * K

def lon_angle(d, sin2x, cos2x):
    return math.acos(min(max((math.cos(d / K) - sin2x) / cos2x, -1), 1))

def in_bounds(theta, a, b):
    if a == b:
        return True
    return (theta - a) % twopi <= (b - a) % twopi

def closest_pair(loci, loci_):

    n = len(loci)

    if n <= 3:
        return min(((x, y, distance(x, y)) for x, y in it.combinations(loci, 2)), key=op.itemgetter(2))

    L, R = loci[:n//2], loci[n//2:]
    split = L[-1].lat
    setL, setR = set(L), set(R)
    L_, R_ = [l for l in loci_ if l in setL], [r for r in loci_ if r in setR]

    sin_split, cos_split = math.sin(split), math.cos(split)
    sin2split, cos2split = sin_split * sin_split, cos_split * cos_split

    closest = min(closest_pair(L, L_), closest_pair(R, R_), key=op.itemgetter(2))

    L = (l for l in L_ if lat_distance(l, sin_split, cos_split) < closest[2])
    R = [r for r in R_ if lat_distance(r, sin_split, cos_split) < closest[2]]
    theta = lon_angle(closest[2], sin2split, cos2split)
    lenR = len(R)
    if lenR > 0:
        i = 0
        j = (i+1) % lenR
        for x in L:
            a, b = (x.lon - theta) % twopi, (x.lon + theta) % twopi
            while not in_bounds(a, R[i].lon, R[j].lon):
                i = (i+1) % lenR
                j = (j+1) % lenR
            while not in_bounds(b, R[i].lon, R[j].lon):
                closest = min(closest, (x, R[j], distance(x, R[j])), key=op.itemgetter(2))
                i = (i+1) % lenR
                j = (j+1) % lenR

    return closest

Locus = namedtuple('Locus', ('city', 'lat', 'lon', 'sin', 'cos'))

N = int(sys.stdin.readline())
C = it.count(1)
while N > 0:
    loci = []
    for _ in range(N):
        l = sys.stdin.readline().split()
        lat, lon = map(math.radians, map(float, l[-2:]))
        lon %= twopi
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
