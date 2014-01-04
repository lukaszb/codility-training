

def solution(nums):
    lefts, rights = sum(nums[:1]), sum(nums[1:])
    minval = abs(lefts - rights)
    for i in range(1, len(nums) - 1):
        lefts += nums[i]
        rights -= nums[i]
        minval = min(minval, abs(lefts - rights))
    return minval


def test(nums, expected):
    actual = solution(nums)
    assert actual == expected, "Expected %r, got %r" % (expected, actual)

test([1000, -1000], 2000)
test([-1, -2, -4], 1)
test([3, 1, 2, 4, 3], 1)
test([3, 1, 2], 0)
test([1, 2, 3, 4], 2)
test([1, 2, 3, 4, 5], 3)
