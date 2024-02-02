def isNum(a):
    # Function to check if a character is a digit.
    if a >= "0" and a <= "9":
        return True
    return False

def atoi(s):
    # Function to convert a string to an integer.
    sign = 1  # Variable to store the sign of the number.
    res = 0  # Variable to store the final result.
    i = 0  # Variable to iterate through the string.
    n = len(s)  # Length of the string.
    if s[0] == "-":
        # Check if the first character is a negative sign.
        sign = -1  # Set the sign to negative.
        i += 1  # Move to the next character.
    for j in range(i, n):
        # Loop through each character in the string.
        if not isNum(s[j]):
            # Check if the character is a digit.
            return -1  # Return -1 if it is not a digit.
        res = res * 10 + ord(s[j]) - ord("0")
    return sign * res  # Return the final result after applying the sign.


print(atoi("123"))
print(atoi("-4123"))
print(atoi("1a3"))
