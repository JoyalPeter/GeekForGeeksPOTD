def printMinNumberForPattern(S):
    if S == "I":
        return "12"
    elif S == "D":
        return "21"
    else:
        minNum = [
            i + 1 for i in range(len(S) + 1)
        ]  # if n is the length of string s, then the largest digit in answer will be n+1
        i = 0
        while i < (len(minNum) - 1):
            if S[i] == "I":
                if minNum[i] > minNum[i + 1]:
                    minNum[i], minNum[i + 1] = minNum[i + 1], minNum[i]
                    if i:  # if i=0, no need to reduce
                        i -= 1  # to check if the swapping affects the previous position
                else:
                    i += 1
            else:
                if minNum[i] < minNum[i + 1]:
                    minNum[i], minNum[i + 1] = minNum[i + 1], minNum[i]
                    if i:
                        i -= 1
                else:
                    i += 1
        minNum = [str(i) for i in minNum]
        return "".join(minNum)

S="IDIDI"
ans=printMinNumberForPattern(S)
print(ans)