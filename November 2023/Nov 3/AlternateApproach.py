def checkTriplet( arr, n):
        maximum = 0

        # Find the maximum element
        for num in arr:
            maximum = max(maximum, num)

        # Hashing array
        hash_table = [0] * (maximum + 1)

        # Increase the count of array elements in the hash table
        for num in arr:
            hash_table[num] += 1

        # Iterate for all possible 'a'
        for i in range(1, maximum + 1):

            # If 'a' is not present in the array, continue
            if hash_table[i] == 0:
                continue

            # Iterate for all possible 'b'
            for j in range(1, maximum + 1):

                # If 'a' and 'b' are the same and there is only one 'a'
                # or if there is no 'b' in the original array, continue
                if (i == j and hash_table[i] == 1) or hash_table[j] == 0:
                    continue

                # Find 'c'
                val = (i * i + j * j) ** 0.5

                # If 'c^2' is not a perfect square, continue
                if int(val) != val:
                    continue

                # If 'c' exceeds the maximum value, continue
                if val > maximum:
                    continue

                # If there exists 'c' in the original array, we have the triplet
                if hash_table[int(val)]:
                    return True

        return False

n=5
arr=[3, 2, 4, 6, 5]
ans=checkTriplet(arr,n)
if ans:
	print("Yes")
else:
	print("No")