def countX(L, R, X):
    count = 0
    X = str(X)
    for i in range(L + 1, R):
        s = str(i)
        if X in s:
            count += s.count(X)
    return count

print(countX(18,81,9))