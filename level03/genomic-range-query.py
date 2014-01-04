"""
A = 1
C = 2
G = 3
T = 4

A < C < G < T
"""
from collections import defaultdict


A = 'A'
C = 'C'
G = 'G'
T = 'T'


MAP = {
    A: 1,
    C: 2,
    G: 3,
    T: 4,
}


def min_neuclos_for_range(rng, left_counter):
    i, j = rng
    total = left_counter[j]
    if i > 0:
        on_left = left_counter[i - 1]
    else:
        on_left = defaultdict(int)

    for val in [1, 2, 3, 4]:
        if total[val] - on_left[val] > 0:
            return val


def min_neuclos(dna, ranges):
    dna = ''.join(dna.split())
    nums = [int(MAP[ch]) for ch in dna]

    # Create lefts counter
    left_counter = []
    values = defaultdict(int)
    for num in nums:
        values[num] += 1
        current = defaultdict(int)
        current.update(values)
        left_counter.append(current)

    return [min_neuclos_for_range(rng, left_counter) for rng in ranges]


def solution(dna, p, q):
    ranges = [(p[i], q[i]) for i in range(len(p))]
    return min_neuclos(dna, ranges)


def assert_min_nucleotides(dna, P, Q, expected):
    result = solution(dna, P, Q)
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


#assert_min_nucleotides('GAC ACC ATA', [(0, 8), (0, 2), (4, 5), (7, 7)], [1, 1, 2, 4])
assert_min_nucleotides('GAC ACC ATA', [0, 0, 4, 7], [8, 2, 5, 7], [1, 1, 2, 4])



print("All tests passed")
