


def solution(distance, falls):
    if len(falls) == 1 and falls[0] and distance == 1:
        return 0
    elif len(falls) < distance:
        return -1
    positions = set(range(1, distance + 1))
    for minute, pos in enumerate(falls):
        if pos in positions:
            positions.remove(pos)
            if not positions:
                return minute
    return -1


def assert_jumps(distance, falls, minute):
    actual = solution(distance, falls)
    if len(falls) > 10:
        falls = ['TRUNCATED'] + falls[-9:]
    msg_for = '(%r, %r)' % (distance, falls)
    if minute == 1:
        msg = "Frog is not expected to get through the river for %s" % msg_for
    else:
        msg = "Expected to jump at minute %r for %s, got %r" % (minute,
                                                                 msg_for,
                                                                 actual)
    assert actual == minute, msg


assert_jumps(1, [1], 0)
assert_jumps(2, [1], -1)

assert_jumps(6, [6, 5, 4, 3, 2, 2, 2, 2, 1], 8)
assert_jumps(4, [1, 1, 3, 5, 6, 2, 4], 6)
assert_jumps(5, [1, 3, 1, 4, 2, 3, 5, 4], 6)

assert_jumps(5, [1, 2, 3, 4], -1)
assert_jumps(5, [1, 2, 3, 4, 6, 7, 8, 9, 10], -1)
assert_jumps(3, [1] * 10, -1)

BIG = 10 * 1000
assert_jumps(BIG, range(1, BIG + 1), BIG - 1)



print("All tests passed")
