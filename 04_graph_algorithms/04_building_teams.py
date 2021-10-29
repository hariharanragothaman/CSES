import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

start_time = time.time()


def solve(g, vertices, edges):
    """
    we need to essentially create 2 disjoint sets.
    Check if we can form a bipartite graph or not...
    """
    color = [-1] * (vertices+1)

    for start in range(vertices):
        if color[start] == -1:
            color[start] = 0
            stack = [start]

            while stack:
                parent = stack.pop()
                for child in g[parent]:
                    if color[child] == -1:
                        color[child] = 1 - color[parent]
                        stack.append(child)
                    elif color[child] == color[parent]:
                        print('IMPOSSIBLE')
                        return

    print(f"The color map is:", color)
    color.pop(0)
    color = [c+1 for c in color]
    print(*color)

def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    pupils, friendships = map(int, input().split())
    g = defaultdict(list)
    while friendships:
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)
        friendships -= 1
    solve(g, pupils, friendships)


if __name__ == "__main__":
    LOCAL = True

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