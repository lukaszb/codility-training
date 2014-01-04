# encoding: UTF8
"""
A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
Array A contains only 0s and/or 1s:
0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
Write a function:
def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the number of passing cars.
The function should return −1 if the number of passing cars exceeds 1,000,000,000.
For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.
Assume that:
    N in [1..100 000]
    A[i] in [0..1]
Complexity:
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
"""


def solution(nums):
    going_east = 0
    passing = 0
    for num in nums:
        if num == 0:
            going_east += 1
        else:
            passing += going_east
            if passing > 10 ** 9:
                return -1
    return passing


def assert_passing_cars(nums, expected):
    result = solution(nums)
    if len(nums) > 10:
        nums = nums[:5] + ['...'] + nums[-5:]
    msg = "Expected %r, got %r | For input: %r" % (expected, result, nums)
    assert result == expected, msg


BIG = 20 * 1000
assert_passing_cars([0] + [1] * BIG, BIG)

assert_passing_cars([0, 1, 0, 1, 1], 5)
assert_passing_cars([1], 0)
assert_passing_cars([0], 0)
assert_passing_cars([0, 1], 1)
assert_passing_cars([0, 1, 1], 2)
assert_passing_cars([0] * 50000 + [1] * 50000, -1)


print("All tests passed")
