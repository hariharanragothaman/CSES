import bisect


def longest_increasing_subsequence(arr):
    temp = []
    for n in arr:
        index = bisect.bisect_left(temp, n)
        if index == len(temp):
            temp.append(n)
        else:
            temp[index] = n
    return temp


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_increasing_subsequence(arr)
    print(len(result))
