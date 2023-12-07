def areRotations(s1, s2):
    if s1 == s2:
        return True
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 != len_s2:
        return False
    s1=s1+s1
    for i in range(len_s1):
        if(s1[i:i+len_s2]==s2):
            return True
    else:
        return False
    

s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
ans = areRotations(s1, s2)
if ans:
    print("1")
else:
    print("0")
s1 = "mightandmagic"
s2 = "andmagicmigth"
ans = areRotations(s1, s2)
if ans:
    print("1")
else:
    print("0")
