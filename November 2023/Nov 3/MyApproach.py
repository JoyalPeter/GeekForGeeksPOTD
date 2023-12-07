def isRepeated(num1,num2,num3): #Function to check if num3 is same as num1 or num2
        return num1==num3 or num2==num3

def checkTriplet(arr, n):
	arr=[i*i for i in arr] #square all elements
	squares=set(arr) 
	for i in range(n-2):
		num1=arr[i]
		for j in range(i+1,n):
			num2=arr[j]
            #Finding the triplet by adding or subtracting the squares of two numbers       
			num3_largest=num1+num2 # addition if the 3rd value is the largest of them
			num3_small=abs(num1-num2) #subtracting if the 3rd value is not the largest
			if not isRepeated(num1,num2,num3_largest): #check for repetition. No pythagorean triplets have repetition 
				if num3_largest in squares:
					return 1
				if not isRepeated(num1,num2,num3_small):
					if num3_small in squares:
						return 1
	return 0

n=5
arr=[3, 2, 4, 6, 5]
ans=checkTriplet(arr,n)
if ans:
	print("Yes")
else:
	print("No")