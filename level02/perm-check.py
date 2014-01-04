

def solution(nums):
    """
    Check if given nums are permutation 1..N.
    """
    if not nums:
        return 0
    seen = set()
    for num in nums:
        if num < 1 or num > len(nums) or num in seen:
            return 0
        seen.add(num)
    return 1



def assert_is_perm(nums):
    assert solution(nums) == 1, "Given numbers %r are not permutation" % nums

def assert_is_not_perm(nums):
    assert solution(nums) == 0, "Given numbers %r are permutation" % nums



assert_is_perm([4, 1, 3, 2])
assert_is_perm([2, 1, 3])

assert_is_not_perm([])
assert_is_not_perm([5, 5])
assert_is_not_perm([1, 1, 2, 3])

print("All tests passed")
