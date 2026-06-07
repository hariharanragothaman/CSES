def khan(graph):
    n = len(graph)
    in_degree = [0] * n
    idx = [0] * n

    for i in range(n):
        for edge in graph[i]:
            in_degree[edge] += 1

    # print("The indegree is:", in_degree)

    q = []
    topo_sort = []

    # Adding all elements with indegree zero into the queue
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    nr = 0

    while q:
        node = q.pop()
        topo_sort.append(node)

        idx[topo_sort[-1]], nr = nr, nr+1

        # Reducing the in-degree
        for edge in graph[topo_sort[-1]]:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                q.append(edge)

    return topo_sort, idx, nr == n


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    g = {}
    for i in range(n):
        g[i] = []

    j = 0
    while j < m:
        # u has to be completed before v
        u, v = list(map(int, input().split()))
        g[u-1].append(v-1)
        j += 1
    # print(g)

    result, order, possible = khan(g)
    if possible:
        res = [c+1 for c in result]
        print(*res)
    else:
        print('IMPOSSIBLE')