from networkx import DiGraph, maximum_flow_value, maximum_flow, min_cost_flow, max_flow_min_cost

for g in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = DiGraph()
    G.add_node(0)
    G.add_node(1)
    stars = []
    for _ in range(N):
        star = input().strip()
        stars.append(star)
        G.add_node(star)
        G.add_edge(0, star, {'capacity': 1.0})
    for _ in range(M):
        l = input().strip().split()
        donor, favs = l[0], l[1:]
        G.add_edge(donor, 1, {'capacity': 1.0})
        for fav in favs:
            G.add_edge(fav, donor, {'capacity': 1.0})
    _, mf = maximum_flow(G, 0, 1)
    print(mf)
    for s in stars:
        print(mf[s].values())
    print('Event {}:'.format(g), max(sum(mf[s].values()) for s in stars))
