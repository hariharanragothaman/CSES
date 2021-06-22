"""
To count the number of subarrays having a definite sum

Constraints:
The numbers are all +ve - 1 to 2*10^5

"""

def count_subarrays_with_target_sum(arr, n, target):
    result_count = 0

    prefix_sum = [0] * (n+1)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
    # print("The prefix sum array is:", prefix_sum)

    j = 0
    for i in range(n+1):
        if prefix_sum[i] > target:
            while j < i:
                tmp = prefix_sum[i] - prefix_sum[j]
                if tmp == target:
                    result_count += 1
                    break
                elif tmp < target:
                    break
                j += 1

        elif prefix_sum[i] == target:
            result_count += 1
    print(result_count)


if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    count_subarrays_with_target_sum(arr, n, target)
