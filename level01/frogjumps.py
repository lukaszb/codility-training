
def solution(X, Y, D):
    distance = Y - X
    result = int(distance / D)
    if distance % D != 0:
        result += 1
    return result


def test(x, y, d, expected):
    actual = solution(x, y, d)
    assert actual == expected, "Expected %r, actual result was %r" % (expected,
                                                                      actual)

test(10, 85, 30, 3)
test(0, 100, 10, 10)
test(0, 0, 2, 0)
