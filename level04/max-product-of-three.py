"""
N in [3..10^5]
A[i] in [-1000..1000]
"""

def product(a, b, c):
    return a * b * c


def naive(nums):
    max_product = nums[0] * nums[1] * nums[2]
    for i_a, a in enumerate(nums):
        for i_b, b in enumerate(nums[i_a+1:], i_a+1):
            for i_c, c in enumerate(nums[i_b+1:], i_b+1):
                max_product = max(max_product, product(a, b, c))
    return max_product


def solution(nums):
    n = len(nums)
    if n < 10:
        return naive(nums)
    nums.sort()
    if nums[-3] > 0:
        # All positives, we can use last 3 numbers
        return product(*nums[-3:])
    elif nums[-1] > 0:
        # There are maximum 2 positives, rest is <= 0, so we take biggest
        # positive and 2 lowest negatives
        return nums[-1] * nums[0] * nums[1]
    else:
        # Take biggest negatives or zeros to get maximal value
        return product(*nums[-3:])


def solution(nums):
    has_zero = 0 in nums
    negatives = [num for num in nums if num < 0]
    positives = [num for num in nums if num > 0]

    negatives.sort()
    positives.sort()

    importants = []
    if len(negatives) > 10:
        importants += negatives[:3] + negatives[-3:]
    else:
        importants += negatives

    if has_zero:
        importants += [0, 0, 0]

    if len(positives) > 10:
        importants += positives[:3] + positives[-3:]
    else:
        importants += positives

    return naive(importants)


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Exepcted %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([-3, 1, 2, -2, 5, 6], 60)
assert_solution([3] * 100, 27)
assert_solution([-3] * 100, -27)
assert_solution([-3, 3] * 50, 27)
assert_solution([-10, 5, 10], -500)
assert_solution([-10, 1, 5, 10], 50)
assert_solution([-10, -5, 1, 2], 100)
assert_solution([-10, -5, 0, 2], 100)
assert_solution(([0] * 50) + [100], 0)
assert_solution([-100] + ([0] * 50) + [100], 0)
assert_solution([-100, -10] + ([0] * 50) + [100], 100000)

BIG = 20 * 1000
assert_solution(list(range(BIG + 1)), BIG * (BIG - 1) * (BIG - 2))


nums = ([-2] * BIG) + ([1] * BIG)
assert_solution(nums, 4)

import random
nums = [random.randint(-10, 10) for x in range(BIG)] + [1000, 500, 20]
assert_solution(nums, 1000 * 500 * 20)

assert_solution(list(range(-1000, 1001)), (-1000) * (-999) * 1000)


print("All tests passes")
