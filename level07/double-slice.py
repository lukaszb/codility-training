

def solution(nums):
    n = len(nums)
    lefts = [0] * n

    for i in range(1, n-1):
        lefts[i] = max(0, lefts[i-1] + nums[i])

    rights = [0] * n
    for i in range(n-2, 0, -1):
        rights[i] = max(0, rights[i+1] + nums[i])

    max_dslice = 0
    for i in range(i, n-1):
        max_dslice = max(max_dslice, lefts[i-1] + rights[i+1])
    return max_dslice


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([1, 2, 3], 0)
assert_solution([1, 2, 3, 4, 5], 7)
assert_solution([3, 2, 6, -1, 4, 5, -1, 2], 17)

assert_solution([1, 1, 0, 10, -100, 10, 0], 21)
assert_solution([1, 1, 0, 10, -100, 10], 11)


print("All tests passed")
