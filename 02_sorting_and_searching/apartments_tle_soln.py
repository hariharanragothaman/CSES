"""
n applicants and m free apartments
Distribute m such that, as many applicants get it.

Each applicant has a desired size - so they will accept any apartment whose size is close enough to the desired size
if the desired size is x, applicant will accept [x-k, x+k] range
print the number of applicants who will get an apartment

Example:
    4, 3, 5
    k = 5
    There are 3 free apartments
    60, 45, 80, 60 - desire

    45, 60, 60, 80 - sorting the desires
    30, 60, 75 - apt size - sort it too

"""
import bisect

def binary_search(array, val):
    index = bisect.bisect_left(array, val)
    if index != len(array) and array[index] == val:
        return index
    else:
        return -1

n, m, k = map(int, input().split())
desired_apt_size = list(map(int, input().split()))
apt_size = list(map(int, input().split()))

hmap = {}
for i, val in enumerate(desired_apt_size):
    hmap[val] = i

# Sorting both the lists
desired_apt_size.sort()
apt_size.sort()

result_count = 0

for d in desired_apt_size:
    # print("The accepted range",accepted_range)
    for value in range(d-k, d+k+1):
        res = binary_search(apt_size, value)
        if res != -1:
            # instead of this we can just reduce the count of free apartments to optimize
            # print(f"The limit found is for {d}, {value}")
            apt_size.remove(value)
            result_count += 1
            break

print(result_count)