"""
Possible bracket types: [] () {}

A - string
N - length of the string, in [0..200 000]

"""


CLOSING = {
    ']': '[',
    ')': '(',
    '}': '{',
}


def solution(text):
    stack = []
    for ch in text:
        if ch in CLOSING:
            if not stack:
                # encountered closing bracket but stack is already empty!
                return 0
            last = stack.pop()
            if last != CLOSING[ch]:
                # wrong bracket encountered
                return 0
        else:
            stack.append(ch)
    if stack:
        # there are still opened brackets on a stack
        return 0
    else:
        return 1


def assert_nesting(text, expected):
    result = solution(text)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_nesting('()', 1)
assert_nesting('()()', 1)
assert_nesting('[](){}', 1)
assert_nesting('{[]([])}', 1)
assert_nesting('[{[]([])}([[{}()]])]', 1)

assert_nesting('[)', 0)
assert_nesting('(]', 0)
assert_nesting('{[]([])]', 0)


print("All tests passed")
