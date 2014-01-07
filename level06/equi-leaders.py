"""
N in [1..10^5]
A[i] in [-10^9..10^9]

Should return number of equi-leaders.

Expected time complexity: O(N)
Expected memory complexity: O(N)
"""
from collections import defaultdict


def solution(nums):
    n = len(nums)
    result = 0

    lefts = defaultdict(int)

    rights = defaultdict(int)
    for num in nums:
        rights[num] += 1

    max_count = 0
    leader = None

    for i, num in enumerate(nums[:-1], 1):
        # lefts would contain results for first i elements
        # rights would contain last (n - i) elements
        lefts[num] += 1
        rights[num] -= 1

        if lefts[num] > max_count:
            max_count = lefts[num]
            leader = num

        if lefts[leader] > (i // 2):
            if rights[leader] > ((n - i) // 2):
                result += 1

    return result


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([4, 3, 4, 4, 4, 2], 2)
assert_solution([1], 0)
assert_solution([1, 1], 1)
assert_solution([1, 2], 0)
assert_solution([2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1], 6)

BIG = 20 * 1000
assert_solution([1] * BIG, BIG - 1)

LARGE = 50 * 1000
assert_solution([1] + [0] * LARGE + [1], 49997)


print("All tests passed")
