def distinctSubseqCount(strng):
    states = [0 for i in range(len(strng) + 1)]
    states[0] = 1  # empty string
    letters = {}
    for i in strng:
        letters[i] = -1
    stateIndx = 1
    for i in range(len(strng)):
        prevIndx = letters[strng[i]]
        letters[strng[i]] = i
        if prevIndx != -1:
            states[stateIndx] = (2 * states[stateIndx - 1]) - states[
                prevIndx
            ]  # prevIndx-1 not required since states have 1 based indexing due to state[0] is empty string
        else:
            states[stateIndx] = 2 * states[stateIndx - 1]
        stateIndx += 1
    print(states,letters)
    return states[-1]
    # def subSeqs(self,strg,subSeqSet,currSubSeq,strLen,currIndx):
    #     if strLen==currIndx:
    #         subSeqSet.append(currSubSeq)
    #         return

    #     subSeqSet.append(currSubSeq)
    #     self.subSeqs(strg,subSeqSet,currSubSeq+strg[currIndx],strLen,currIndx+1)
    #     self.subSeqs(strg,subSeqSet,currSubSeq,strLen,currIndx+1)


def betterString(str1, str2):
    str1 = str1.rstrip()
    # str1Arr=[]
    # str2Arr=[]
    # # str1Set.add(str1)
    # # print(str1Set)
    # self.subSeqs(str1,str1Arr,"",len(str1),0)
    # str1Set=set(str1Arr)
    # # str2Set.add(str2)
    # self.subSeqs(str2,str2Arr,"",len(str2),0)
    # str2Set=set(str2Arr)
    # # print(str2Set)
    # if(len(str1Set)<len(str2Set)):
    #     return str2
    # else:
    #     return str1
    str1Count = distinctSubseqCount(str1)
    str2Count = distinctSubseqCount(str2)
    if str2Count > str1Count:
        return str2
    else:
        return str1


str1 = "gfg"
str2 = "ggg"
print(betterString(str1, str2))
