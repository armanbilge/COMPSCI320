import math
import itertools as it
import networkx as nx
from networkx import DiGraph

for g in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    stars = [input().strip() for _ in range(N)]
    donors = {donor: list(favs) for donor, favs in map(lambda x: (x[0], x[1:]), (input().strip().split() for _ in range(M))) if len(favs) > 0}
    L = math.ceil(sum(1 for _ in filter(lambda x: len(x) > 0, donors.values())) / N)
    G = DiGraph()
    for donor, favs in donors.items():
        G.add_edge(0, donor, capacity=1)
        for fav in favs:
            G.add_edge(donor, fav)
    for l in it.count(L):
        for star in stars:
            G.add_edge(star, 1, capacity=l)
        if nx.maximum_flow_value(G, 0, 1) == len(donors):
            print('Event {}:'.format(g), l)
            break
        for star in stars:
            G.remove_edge(star, 1)
