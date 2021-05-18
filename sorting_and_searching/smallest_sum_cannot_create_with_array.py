## This is the Missing Coin Sum Problem
"""
You have n coins with positive integer values.
What is the smallest sum you cannot create using a subset of the coins?
"""

from collections import deque
from bisect import bisect_left

def smallest_sum_that_cannot_be_formed(arr, n):
    arr.sort()
    # print(arr)

    for num in range(1, 10**9 + 1):
        # print("********************************************************************")
        # print(f"The value of num is: {num}")

        if num in arr:
            # print(f"The number is in array - Continuing....")
            continue
        elif num not in arr:
            # print(f"The number not in array - Checking if it can be formed")
            # Check if it can be formed
            q = deque()
            q.append((num, 0))

            # Because a numbers can be formed only by numbers smaller than it in this question
            # as all numbers are > 0
            bisect_index = bisect_left(arr, num)
            # print(f"The bisect index is: {bisect_index}")

            def dfs():
                can_form = False
                visited = set()
                while q:
                    # Applying BFS
                    # print("The queue is:", q)
                    current_target, current_index = q.popleft()

                    for i in range(current_index, bisect_index):
                        new_target = current_target - arr[i]
                        # print(f"The new target is: {new_target}")

                        if new_target == 0:
                            can_form = True
                            # print("The number can be formed!!!")
                            return can_form
                        elif new_target > 0:
                            # Searching again from the current index allows duplicates
                            # So - search from the next index
                            q.append((new_target, i+1))

                return can_form

            flag = dfs()
            if flag:
                continue
            else:
                # print(f"The number cannot be formed {num}")
                return num


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = smallest_sum_that_cannot_be_formed(arr, n)
    print(result)