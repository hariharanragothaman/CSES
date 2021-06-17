## This is standard Djikstra algorithm

from collections import defaultdict

def find_shortest_distance_from_source_to_all_targets(graph, source=1):
    pass

if __name__ == '__main__':
    v, e = list(map(int, input().split()))

    g = defaultdict(list)

    i = 0
    while i < e:
        s, t, d = list(map(int, input().split()))
        g[s].append(t)
        g[t].append(s)
        i += 1
    print(f"The graph is: {g}")