from collections import defaultdict

def connected_components(graph, n):
    components, visited = [], [False] * n

    def dfs(start):
        component, stack = [], [start]

        while stack:
            start = stack[-1]

            if visited[start]:
                stack.pop()
                continue
            else:
                visited[start] = True
                component.append(start)

            for i in graph[start]:
                if not visited[i]:
                    stack.append(i)

        return component

    for i in range(n):
        if not visited[i]:
            components.append(dfs(i))

    return components


if __name__ == '__main__':
    ncities, nroads = map(int, input().split())
    g = defaultdict(list)
    while nroads > 0:
        u, v  = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        nroads -= 1

    _connected_components = connected_components(g, ncities+1)
    # print(_connected_components)

    for c in _connected_components:
        if 0 in c:
            _connected_components.remove(c)

    print(len(_connected_components) - 1)

    res = [c[-1] for c in _connected_components]
    for k in zip(res, res[1:]):
        print(*k)