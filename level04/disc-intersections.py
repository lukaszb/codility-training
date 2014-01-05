"""
N in [0..10^5]
A[i] in [0..2^31]
"""


MAX_RESULT = 10 ** 7


def solution(nums):
    n = len(nums)
    starts = [0] * n
    ends = [0] * n

    # prepare helper arrays
    for i, r in enumerate(nums):
        starts[max(i-r, 0)] += 1
        ends[min(i+r, n - 1)] += 1

    active = 0
    intersections = 0

    # sweep away!
    for i, r in enumerate(nums):
        started = starts[i]
        ended = ends[i]
        current = active * started + (started * (started - 1) / 2)
        intersections += current
        if intersections > MAX_RESULT:
            return -1
        active += started - ended
    return intersections


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([1, 5, 2, 1, 4, 0], 11)
assert_solution([], 0)
assert_solution([3, 3, 0, 2, 2, 2], 14)

BIG = 100
discs = [1 for x in range(BIG)]
assert_solution(discs, 2 * BIG -3)

L = 50 * 1000
assert_solution([0] * L, 0)


print("All tests passed")
