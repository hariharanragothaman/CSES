from collections import deque


def counting_rooms(g, R, C):
    """
    Floor is '.'
    Wall is '#'

    So if a floor is surrounded by all sides by a wall - then it's a room
    And we need to count the number of rooms

    # This question is basically asking us to find the number of connected components. Holy fuck. Haha
    :param g:
    :return:
    """

    def neighbours(r, c):
        for rows, cols in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            if 0 <= rows < R and 0 <= cols < C:
                yield rows, cols

    def dfs(g, root):
        q = deque()
        q.append(root)

        while q:
            row, cols = q.pop()
            g[row][cols] = "#"
            for nei in neighbours(row, cols):
                nr, nc = nei
                if g[nr][nc] == ".":
                    q.append((nr, nc))

    rooms = 0
    for i in range(R):
        for j in range(C):
            if g[i][j] == ".":
                dfs(g, (i, j))
                rooms += 1
    return rooms


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        s = [c for c in input()]
        arr[i] = s
    result = counting_rooms(arr, n, m)
    print(result)
