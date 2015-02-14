def combinationSum(candidates, target):
    results = [[] for i in xrange(0, target+1)]
    results[0].append([])

    candidates.sort()

    for c in candidates:
        for i in xrange(c, target+1):
            results[i].extend(r+[c] for r in results[i-c])

    return results[target]
