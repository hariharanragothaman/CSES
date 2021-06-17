from heapq import heappop, heappush
# import resource, sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
# sys.setrecursionlimit(10**7)


def shortest_path(arr, R, C):
    """
    1. Check if there is path b/w them - this can be done by classic DFS
    2. For the shortest path - keep adding 1 to their neighbours,
        as we are popping, update the smallest one.

    # In this we just applied raw-logic and just converted it into heap
    """
    def find_start():
        for i in range(R):
            for j in range(C):
                if arr[i][j] == "A":
                    return i, j

    start = find_start()

    # Sub-routine to get neighbours
    def neighbours(r, c):
        for rows, cols, _direction in (
            (r - 1, c, "U"),
            (r, c - 1, "L"),
            (r + 1, c, "D"),
            (r, c + 1, "R"),
        ):
            if 0 <= rows < R and 0 <= cols < C:
                yield rows, cols, _direction

    # Actual Solution to the problem
    q = [(0, start, "")]
    visited = set()
    path_exists = False
    shortest_dist = float("inf")
    result_path = ""

    while q:
        # print(f"The queue is: {q}")
        # dist, node, path = q.pop()
        dist, node, path = heappop(q)
        node_row, node_col = node

        for nei in neighbours(node_row, node_col):
            nr, nc, direction = nei
            # print(f"The nei and direction is: {(nr, nc)}, {direction}")
            if arr[nr][nc] == "B":
                path_exists = True
                if dist + 1 < shortest_dist:
                    shortest_dist = dist + 1
                    result_path = path + direction

            elif arr[nr][nc] == "." and (nr, nc) not in visited:
                visited.add((nr, nc))
                heappush(q, (dist + 1, (nr, nc), path + direction))
                # q.append((dist + 1, (nr, nc), path + direction))

    return path_exists, shortest_dist, result_path


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        s = [c for c in input()]
        arr[i] = s

    result, dist, res_path = shortest_path(arr, n, m)

    if result:
        print("YES")
        print(dist)
        print(res_path)
    else:
        print("NO")
