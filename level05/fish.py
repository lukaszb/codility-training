"""
A - array of N-integers;
A[i] - i-th fish size
A[i] in [0..10^9] (unique values)

B - array of N-integers
B[i] - direction of i-th fish; 1 means upstream (going to the higher values),
       0 means downstream (going to the lower values)
B[i] in [0, 1]

N in 1[..100 000]

"""
from itertools import izip


def solution(sizes, directions):
    stack = []

    escaped = 0

    for size, direction in izip(sizes, directions):
        if direction == 0:
            if stack:
                while stack and stack[-1] < size:
                    stack.pop()
                if not stack:
                    # wow, that fish ate all the fishes going upstream!
                    escaped += 1
            else:
                escaped += 1
        else:
            stack.append(size)

    #print stack, escaped
    return len(stack) + escaped





def assert_alives(sizes, directions, expected):
    result = solution(sizes, directions)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_alives([4, 3, 2, 1, 5], [0, 1, 0, 0, 0], 2)
assert_alives([5, 1, 3, 2, 4], [1, 0, 1, 1, 0], 1)
assert_alives([6, 7, 8, 9, 5, 1, 3, 2, 4], [1, 1, 1, 1, 1, 0, 1, 1, 0], 5)
assert_alives([6, 7, 4, 5, 2, 1, 3], [0, 1, 0, 1, 1, 1, 0], 3)

BIG = 20 * 1000
assert_alives(list(range(BIG)), [0] * BIG, BIG)


print("All tests passed")
