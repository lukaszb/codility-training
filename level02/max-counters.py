

def solution(count, operations):
    N = count + 1
    counters = [0] * N
    oldcmax = cmax = 0
    for idx in operations:
        if idx == count + 1:
            oldcmax = cmax
        else:
            if counters[idx] < oldcmax:
                counters[idx] = oldcmax
            counters[idx] += 1
            if counters[idx] > cmax:
                cmax = counters[idx]
    return [max(num, oldcmax) for num in counters[1:]]



def assert_result(count, operations, expected):
    actual = solution(count, operations)

    assert actual == expected, "Expected %r, got %r" % (expected, actual)


assert_result(5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2])
assert_result(3, [1, 1, 1, 3, 4, 2], [3, 4, 3])
assert_result(3, [4, 4, 4, 4, 4, 4, 4, 2, 2, 1, 3, 4, 1, 1, 3], [4, 2, 3])
assert_result(3, [2, 2, 1, 3, 4, 1, 1, 3], [4, 2, 3])
assert_result(3, [2, 2, 1, 3, 4, 1, 1, 3, 1, 4, 2, 2, 4, 3], [7, 7, 8])

BIG = 20 * 1000
assert_result(BIG, [BIG + 1] * BIG, [0] * BIG)


print("All tests passed")
