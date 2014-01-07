from collections import defaultdict


def solution(nums):
    nums_map = {}  # would store first index for each encountered number
    counter = defaultdict(int)  # would store number of total occurences

    for i, num in enumerate(nums):
        if num not in nums_map:
            nums_map[num] = i
        counter[num] += 1
        if counter[num] > len(nums) // 2:
            return nums_map[num]
    return -1


def assert_solution(nums, expected):
    result = solution(nums)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_solution([3, 2, 3, 4, 3, 3, 3, -1], 0)
assert_solution([2, 1, 2, 2, 2, 1, 1, 1, 1], 1)
assert_solution([2, 2, 2, 2, 1, 1, 1, 1], -1)


print("All tests passed")
