def differentSymbolsNaive(s):
    pool = []
    distinctChars = 0
    for c in s:
        if not c in pool:
            pool.append(c)
            distinctChars += 1
    return distinctChars