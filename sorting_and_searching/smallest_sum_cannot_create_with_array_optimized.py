n = int(input())
a = sorted(list(map(int, input().split())))

# print(f"The sorted array is: {a}")
currSum = 0
for i in range(n):
    # print(f"The current sum is: {currSum}")
    if currSum + 1 < a[i]:
        break
    currSum += a[i]

print(currSum + 1)
