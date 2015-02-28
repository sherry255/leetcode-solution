from combinatorics import comb

def subsets(S):
    S.sort()
    return [list(c) for i in xrange(len(S)+1) for c in comb(S, i)]
