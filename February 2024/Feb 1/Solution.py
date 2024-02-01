def checkPangram(s):
    if len(s) < 26:
        return False
    letters = set()
    for i in s.lower():
        if i >= "a" and i <= "z":
            letters.add(i)

    return len(letters) == 26


s1 = "Bawds jog, flick quartz, vex nymph"
s2 = "aBcD"
print(checkPangram(s1))
print(checkPangram(s2))
