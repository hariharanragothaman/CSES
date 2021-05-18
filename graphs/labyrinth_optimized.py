from sys import stdin
from collections import deque

input = stdin.readline

characters = ["U", "D", "L", "R"]


def find_start():
    for r in range(n):
        for c in range(m):
            if g[r][c] == "A":
                return r, c


def get_neighbors(r, c):
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c, 0))
    if r < n - 1:
        neighbors.append((r + 1, c, 1))
    if c > 0:
        neighbors.append((r, c - 1, 2))
    if c < m - 1:
        neighbors.append((r, c + 1, 3))
    return neighbors


def dfs(r, c):
    queue = deque()
    queue.append((r, c))
    g[r][c] = "#"
    while queue:
        field_r, field_c = queue.popleft()
        neighbors = get_neighbors(field_r, field_c)
        for y, x, d in neighbors:
            if g[y][x] == ".":
                g[y][x] = "#"
                b[y][x] = d
                queue.append((y, x))
            elif g[y][x] == "B":
                b[y][x] = d
                return y, x
    return -1, -1


def get_path(end_r, end_c):
    path = deque()
    r = end_r
    c = end_c
    while b[r][c] != -1:
        path.appendleft(characters[b[r][c]])
        if b[r][c] == 3:
            c -= 1
        elif b[r][c] == 2:
            c += 1
        elif b[r][c] == 1:
            r -= 1
        elif b[r][c] == 0:
            r += 1
    return path


n, m = [int(x) for x in input().split()]
g = [list(input().rstrip()) for _ in range(n)]
b = [[-1] * m for _ in range(n)]

start_r, start_c = find_start()
end_r, end_c = dfs(start_r, start_c)
if end_r == -1:
    print("NO")
else:
    path = get_path(end_r, end_c)
    print("YES")
    print(len(path))
    print(*path, sep="")
