"""
A = 1
C = 2
G = 3
T = 4

A < C < G < T
"""

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

def min_nucleotides(dna, rng):
    i, j = rng
    j += 1
    min_val = 10
    for ch in dna[i:j]:
        if ch == A:
            return 1
        min_val = min(min_val, MAP[ch])
    return min_val

def min_nucleotides_for_ranges(dna, ranges):
    dna = ''.join(dna.split())
    return [min_nucleotides(dna, rng) for rng in ranges]


def solution(dna, p, q):
    ranges = [(p[i], q[i]) for i in range(len(p))]
    return min_nucleotides_for_ranges(dna, ranges)


def assert_min_nucleotides(dna, ranges, expected):
    result = min_nucleotides_for_ranges(dna, ranges)
    #if len(nums) > 10:
        #nums = nums[:5] + ['...'] + nums[-5:]
    msg = "Expected %r, got %r" % (expected, result)
    assert result == expected, msg


assert_min_nucleotides('GAC ACC ATA', [(0, 8), (0, 2), (4, 5), (7, 7)], [1, 1, 2, 4])



print("All tests passed")
