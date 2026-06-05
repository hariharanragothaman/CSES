import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

start_time = time.time()


def solve(g, n, m, start=1):
    """
    Basically asking us to find the shortest path from 1 to n
    """

    vertex = list(range(1, n+1))
    dist = [float("inf")] * n
    initial = [-1] * n

    distance_map = dict(zip(vertex, dist))
    parents_map = dict(zip(vertex, initial))

    distance_map[start] = 0
    q = [(0, start)]

    while q:
        path_length, vertex = heappop(q)
        if path_length == distance_map[vertex]:
            for nei, edge_length in g[vertex]:
                if edge_length + path_length < distance_map[nei]:
                    distance_map[nei] = edge_length + path_length
                    parents_map[nei] = vertex
                    heappush(q, (edge_length+path_length, nei))

    if distance_map[n] == float('inf'):
        print('IMPOSSIBLE')
    else:
        print(distance_map[n]+1)
        res, dest = [n], n
        while parents_map[dest] != -1:
            c = parents_map[dest]
            res.append(c)
            dest = c
        res = res[::-1]
        print(*res)

def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    computer, connection = map(int, input().split())
    g = defaultdict(list)
    while connection > 0:
        u, v = map(int, input().split())
        g[u].append((v, 1))
        g[v].append((u, 1))
        connection -= 1
    solve(g, computer, connection)


if __name__ == "__main__":
    LOCAL = False

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("../io/data.in", "r")
        sys.stdout = open("../io/data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()