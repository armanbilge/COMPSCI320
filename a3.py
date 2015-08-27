# Arman Bilge
# abil933
# 8079403
# COMPSCI 320 Assignment 3
# Efficiently finds the nearest pair of points on a globe

import sys
import math
import itertools as it
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

def closest_pair(loci):
    if len(loci) == 2:
        return loci[0], loci[1], distance(loci[0], loci[1])
    elif len(loci) == 3:
        return min(((x, y, distance(x, y)) for x,y in it.combinations(loci, 2)), key=lambda p: p[2])
    split = sum(locus.lat for locus in loci) / len(loci)
    A = [locus for locus in loci if locus.lat <= split]
    B = [locus for locus in loci if locus.lat > split]
    a = closest_pair(A)
    b = closest_pair(B)
    pairs = it.chain([a, b], ((x, y, distance(x, y)) for x in A for y in B))
    return min(pairs, key=lambda p: p[2])

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
    a, b, d = closest_pair(loci)
    a, b = sorted([a.city, b.city])
    print('Scenario {}:'.format(next(C)))
    print('Closest pair: {} {}'.format(a, b))
    print('Distance: {0:.1f}'.format(d))
    N = int(sys.stdin.readline())
