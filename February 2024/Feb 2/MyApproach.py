def atoi(s):
    try:
        ans = int(s)
    except:
        return -1
    else:
        return ans

print(atoi('123'))
print(atoi('-4123'))
print(atoi('1a3'))