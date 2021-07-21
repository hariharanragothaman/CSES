class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


def solve(arr, a, b):
    rQ = RangeQuery(data=arr)
    if a == b:
        return arr[b-1]
    op = rQ.query(a-1, b-1)
    return op

if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    while i < q:
        a, b = map(int, input().split())
        op = solve(arr, a, b)
        print(op)
        i += 1