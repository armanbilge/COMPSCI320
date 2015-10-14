from math import ceil

for g in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    stars = [input().strip() for _ in range(N)]
    donors = {donor: list(favs) for donor, favs in map(lambda x: (x[0], x[1:]), (input().strip().split() for _ in range(M)))}
    print('Event {}:'.format(g), ceil(sum(1 for _ in filter(lambda x: len(x) > 0, donors.values())) / N))
