

def solution(nums):
    nums = sorted(nums)
    for i, num in enumerate(nums, 1):
        if i != num:
            return i
    return len(nums) + 1


def solution(nums):
    n = len(nums) + 1
    if n == 1:
        return 1
    expected_sum = (n * (n+1)) // 2
    return expected_sum - sum(nums)



def test(nums, missing):
    actual = solution(nums)
    assert actual == missing, "Expected %r, got %r" % (missing, actual)


test([2, 3, 1, 5], 4)
test([], 1)
test([2, 3], 1)
test([1, 2], 3)
test(list(range(1, 101)), 101)
