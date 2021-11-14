n = int(input())
arr = list(map(int, input().split()))

n = len(arr)
i = 0
moves = 0

mx = arr[0]

i = 1
while i < n:
    if arr[i] < mx:
        moves += mx - arr[i]

    mx = max(arr[i], mx)
    i += 1

print(moves)
