class DisjointSetUnionFast:
    def __init__(self, n):
        n += 1
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


if __name__ == '__main__':
    cities, roads, queries = list(map(int, input().split()))
    dsu = DisjointSetUnionFast(cities)

    days = 0

    days_map = [0 for i in range(cities + 1)]

    i = 0
    while i < roads:
        u, v = list(map(int, input().split()))
        days += 1

        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            if days_map[u] == 0:
                days_map[u] = days

            if days_map[v] == 0:
                days_map[v] = days

        i += 1

    # print(f"The hashmap is:", days_map)

    j = 0
    while j < queries:
        a, b = list(map(int, input().split()))
        if days_map[a] == 0 or days_map[b] == 0:
            print(-1)
        else:
            res = max(days_map[a], days_map[b])
            print(res)
        j += 1