from collections import Counter
from networkx import DiGraph, min_cost_flow

f = lambda star, k: '{}_{}'.format(star, k)

for g in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = DiGraph()
    C = Counter()
    stars = [input().strip() for _ in range(N)]
    donors = []
    max_flow = 0
    for _ in range(M):
        l = input().strip().split()
        donor, favs = l[0], l[1:]
        C.update(favs)
        donors.append((donor, favs))
        if favs:
            max_flow += 1
    G.add_node(0, demand=-max_flow)
    G.add_node(1, demand=max_flow)
    for star in stars:
        for k in range(C[star]):
            G.add_edge(f(star, k), 1, capacity=1)
    for donor, favs in donors:
        G.add_edge(0, donor, capacity=1)
        for fav in favs:
            for k in range(C[fav]):
                G.add_edge(donor, f(fav, k), weight=k+1)
    mfmc = min_cost_flow(G)
    print('Event {}:'.format(g), max(sum(mfmc[f(star, k)][1] for k in range(C[star])) for star in stars))
