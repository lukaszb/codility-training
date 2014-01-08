"""
N in [0.10^6]
A[i] in [0..10^9]

[10, 5, 6, 9, 2, 9, 4] => 7 (9 - 2)
[3, 3, 3] => 0
[5, 4, 3, 2, 1] => 0 (no profit is possible)
[] => 0

Example for [10, 5, 9, 2, 4]:

i, min_on_left, val, profit
0, 10 (initially, min_on_left = nums[0]), 10, 0  # we can skip this step
1, 10, 5, -5
2, 5, 9, 4 <== biggest profit
3, 5, 2, 3
4, 2, 4, 2

Expected time complexity: O(N)
Expected memory complexity: O(1)
"""


def solution(nums):
    if not nums:
        return 0
    min_val = nums[0]
    profit = 0
    for val in nums[1:]:
        profit = max(profit, val - min_val)
        min_val = min(min_val, val)
    return profit


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([23171, 21015, 21123, 21366, 21013, 21367], 354)

assert_solution([10, 5, 6, 9, 2, 9, 4], 7)
assert_solution([10, 5, 9, 2, 4], 4)
assert_solution([3, 3, 3], 0)
assert_solution([5, 4, 3, 2, 1], 0)

N = 200 * 1000
assert_solution([1] * N, 0)
assert_solution(list(range(1, N + 1)), N - 1)


print("All tests passed")
