"""
N in [0..10^6]
A[i] in [-2^31..2^31]
"""
import itertools


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def naive(nums):
    for i_a, a in enumerate(nums):
        for i_b, b in enumerate(nums[i_a+1:], i_a+1):
            for i_c, c in enumerate(nums[i_b+1:], i_b+1):
                if is_triangle(a, b, c):
                    return 1
    return 0


def solution(nums):
    n = len(nums)
    if n < 3:
        return 0
    nums.sort()
    for a, b, c in itertools.izip(nums, nums[1:], nums[2:]):
        if is_triangle(a, b, c):
            return 1
    return 0



def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Exepcted %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([10, 2, 5, 1, 8, 20], 1)
assert_solution([10, 50, 5, 1], 0)
assert_solution([3, 4, 5], 1)
assert_solution([100, 1, 2], 0)
assert_solution([3, 4, 5, 20], 1)
assert_solution([1, 1, 3, 4, 5], 1)
assert_solution([10, 10, 10], 1)
assert_solution([10, 10, 5], 1)

assert_solution([], 0)
assert_solution([1], 0)
assert_solution([1, 1], 0)

assert_solution(list(range(12**3)), 1)


print("All tests passes")
