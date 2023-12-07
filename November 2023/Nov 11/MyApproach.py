"""Intuition 
1.  Convert all elements appearing once to "1"
    If "1"s are not in same position for both strings return false
2.  Store the corresponding element2 in str2 for element1 in str1 in a map
    If the same element2 is not repeated next time element1 is encountered return false
"""


def areIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return 0

    str1Elements = set(str1)
    str2Elements = set(str2)
    str1Arr = list(str1)
    str2Arr = list(str2)

    if len(str1Elements) != len(
        str2Elements
    ):  # if no of distinct elements are different return false
        return 0
    if len(str1Elements) == len(str1) and len(str2Elements) == len(
        str2
    ):  # if the strings contain all distinct elements with no repetition return true
        return 1

    str1Counts = {}
    str2Counts = {}

    # To Do -Convert to Function
    for i in str1:
        str1Counts[i] = str1Counts.get(i, 0) + 1
    for i in str2:
        str2Counts[i] = str2Counts.get(i, 0) + 1

    # To Do -Convert to Function
    for i in range(len(str1Arr)):
        key = str1Arr[i]
        if str1Counts[key] == 1:
            str1Arr[i] = "1"

    for i in range(len(str2Arr)):
        key = str2Arr[i]
        if str2Counts[str2Arr[i]] == 1:
            str2Arr[i] = "1"

    positionMapping = {}
    for i in range(len(str1)):
        if str1[i] != "1" and str2[i] != "1":
            j = positionMapping.get(str1[i], 0)
            if j:
                if j != str2[i]:
                    return 0
            else:
                positionMapping[str1[i]] = str2[i]
        elif str1[i] != "1" or str2[i] != "1":
            return 0

    return 1


str1 = "aab"
str2 = "xxy"
print(areIsomorphic(str1, str2))
