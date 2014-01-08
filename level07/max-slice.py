

def solution(nums):
    max_slice = 0
    temp = 0

    all_negatives = True
    max_value = nums[0]

    for num in nums:
        if num >= 0:
            all_negatives = False
        max_value = max(max_value, num)
        temp = max(temp + num, 0)
        max_slice = max(max_slice, temp)

    if all_negatives:
        return max_value
    return max_slice


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([3, 2, -6, 4, 0], 5)


N = 200 * 1000
assert_solution([1] * N, N)
assert_solution(list(range(1, N + 1)), N * (N + 1) // 2)

assert_solution([-10, -3, -4, -6, 0], 0)
assert_solution([-10, -3, -4, -6, 0, -2], 0)
assert_solution([-10, -3, -4, -6], -3)


print("All tests passed")
