def sequence(n):
    if n == 1:
        return 1
    fn = 1
    mod = 1000000007
    k = 2
    for i in range(2, n + 1):
        s = 1
        for j in range(i):
            s *= k
            k += 1
        fn = (fn + s) % mod
    return fn

print(sequence(5))
