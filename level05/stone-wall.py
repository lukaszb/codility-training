"""

N in [1..10^5]
A[i] in [1..10^9]

"""

def solution(heights):
    stack = []
    blocks = 0

    for height in heights:
        while stack and stack[-1] > height:
            stack.pop()

        if not stack or stack[-1] < height:
            stack.append(height)
            blocks += 1

    return blocks



def assert_blocks(heights, expected):
    result = solution(heights)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_blocks([8, 7, 7, 8, 9, 4, 5, 8, 8], 7)

assert_blocks([3, 2, 1], 3)
assert_blocks([3, 1, 2], 3)
assert_blocks([2, 3, 5, 2], 3)
assert_blocks([2, 3, 2, 3, 5, 2], 4)


print("All tests passed")
