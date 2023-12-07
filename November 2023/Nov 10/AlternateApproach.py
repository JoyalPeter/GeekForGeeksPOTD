def printMinNumberForPattern(S):
    # Initialize current_max (to make sure that
    # we don't use repeated character
    curr_max = 0

    # Initialize last_entry (Keeps track for
    # last printed digit)
    last_entry = 0
    i = 0
    ans = ""
    # Iterate over input array
    while i < len(S):
        # Initialize 'noOfNextD' to get count of
        # next D's available
        noOfNextD = 0
        if S[i] == "I":
            # If letter is 'I'

            # Calculate number of next consecutive D's
            # available
            j = i + 1
            while j < len(S) and S[j] == "D":
                noOfNextD += 1
                j += 1
            if i == 0:
                curr_max = noOfNextD + 2
                last_entry += 1

                # If 'I' is first letter, print incremented
                # sequence from 1
                ans += str(last_entry)
                ans += str(curr_max)

                # Set max digit reached
                last_entry = curr_max
            else:
                # If not first letter

                # Get next digit to print
                curr_max += noOfNextD + 1

                # Print digit for I
                last_entry = curr_max
                ans += str(last_entry)

            # For all next consecutive 'D' print
            # decremented sequence
            for k in range(noOfNextD):
                last_entry -= 1
                ans += str(last_entry)
                i += 1

        # If letter is 'D'
        elif S[i] == "D":
            if i == 0:
                # If 'D' is first letter in sequence
                # Find number of Next D's available
                j = i + 1
                while j < len(S) and S[j] == "D":
                    noOfNextD += 1
                    j += 1

                # Calculate first digit to print based on
                # number of consecutive D's
                curr_max = noOfNextD + 2

                # Print twice for the first time
                ans += str(curr_max)
                ans += str(curr_max - 1)

                # Store last entry
                last_entry = curr_max - 1
            else:
                # If current 'D' is not first letter

                # Decrement last_entry
                ans += str(last_entry - 1)
                last_entry -= 1
        i += 1
    return ans


S = "IDIDI"
ans = printMinNumberForPattern(S)
print(ans)
