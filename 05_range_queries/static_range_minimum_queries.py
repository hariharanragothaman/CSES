class SegmentTree:
    def __init__(self, arr, function):
        self.tree = [None for _ in range(len(arr))] + arr
        self.size = len(arr)
        self.fn = function
        self.build_tree()

    def build_tree(self):
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, p, v):
        p += self.size
        self.tree[p] = v
        while p > 1:
            p = p // 2
            self.tree[p] = self.fn(self.tree[p * 2], self.tree[p * 2 + 1])

    def query(self, l, r):
        l, r = l + self.size, r + self.size
        res = None
        while l <= r:
            if l % 2 == 1:
                res = self.tree[l] if res is None else self.fn(res, self.tree[l])
            if r % 2 == 0:
                res = self.tree[r] if res is None else self.fn(res, self.tree[r])
            l, r = (l + 1) // 2, (r - 1) // 2
        return res


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    seg_tree = SegmentTree(arr, function=min)
    i = 0
    while i < k:
        left, right = list(map(int, input().split()))
        left, right = left-1, right-1
        result = seg_tree.query(left, right)
        print(result)
        i += 1