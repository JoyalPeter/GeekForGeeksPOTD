def sumOfDependencies(adj, V):
    nod = 0
    for i in adj:
        nod += len(i)
    return nod

print(sumOfDependencies([[2, 3], [3], [3], []] ,4))