from collections import Counter
from networkx import DiGraph, max_flow_min_cost

f = lambda star, k: '{}_{}'.format(star, k)

for g in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = DiGraph()
    C = Counter()
    stars = [input().strip() for _ in range(N)]
    donors = []
    for _ in range(M):
        l = input().strip().split()
        donor, favs = l[0], l[1:]
        C.update(favs)
        donors.append((donor, favs))
    for star in stars:
        for k in range(C[star]):
            G.add_edge(f(star, k), 1, {'capacity': 1})
    for donor, favs in donors:
        G.add_edge(0, donor, {'weight': 0, 'capacity': 1})
        for fav in favs:
            for k in range(C[fav]):
                G.add_edge(donor, f(fav, k), {'weight': k + 1})
    mfmc = max_flow_min_cost(G, 0, 1)
    print('Event {}:'.format(g), max(sum(mfmc[f(star, k)][1] for k in range(C[star])) for star in stars))
