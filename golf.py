import itertools as it
from networkx import DiGraph, max_flow_min_cost

f = lambda star, k: '{}_{}'.format(star, k)

for g in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = DiGraph()
    stars = [input().strip() for _ in range(N)]
    for star, k in it.product(stars, range(M)):
        G.add_edge(f(star, k), 1, {'capacity': 1})
    for _ in range(M):
        l = input().strip().split()
        donor, favs = l[0], l[1:]
        G.add_edge(0, donor, {'weight': 0, 'capacity': 1})
        n = len(favs)
        for fav in favs:
            for k in range(M):
                G.add_edge(donor, f(fav, k), {'weight': k + 1})
    mfmc = max_flow_min_cost(G, 0, 1)
    print('Event {}:'.format(g), max(sum(mfmc[f(star, k)][1] for k in range(M)) for star in stars))
