def recamanSequence(n):
    seq=[0]*n
    seqSet=set()
    seqSet.add(0)
    if n==1:
        return seq
    for i in range(1,n):
        num=seq[i-1]-i
        if(num>0 and num not in seqSet):
            seq[i]=num
            seqSet.add(num)
        else:
            seq[i]=seq[i-1]+i
            seqSet.add(seq[i-1]+i)
    return seq

print(recamanSequence(5))