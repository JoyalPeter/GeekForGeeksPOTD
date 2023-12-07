def isRotated(str1, str2):
    clockwise = str1[-2:] + (str1[:-2])
    anticlockwise = str1[2:] + (str1[:2])

    return str2 == clockwise or str2 == anticlockwise

a = "amazon"
b = "azonam"
print(isRotated(a,b))