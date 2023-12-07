import math
#convert all elements to strings of same size by appending 'a' and keep appending 'a' when same element is encountered
#sort the strings by length in descending and first k elements gives the answer
def topK( nums, k):
    topElements=[]
    nums.sort(reverse=True)
    longest=max(nums)
    longestSize=math.floor(math.log10(longest)+1) #size of longest element
    for i in range(len(nums)):
        s=str(nums[i])
        if len(s)<longestSize:
            s=s.ljust(longestSize,'a') #pad 'a' to make size equal to longest size
        nums[i]=s
    currentElement=nums[0]
    repetition=(currentElement)
    elements=[]
    for i in range(1,len(nums)):
        if currentElement!=nums[i]:
            elements.append(repetition)
            currentElement=nums[i]
            repetition=(currentElement)
            
        else:
            repetition+="a"
    elements.append(repetition)
    sortedElements=sorted(elements,key=len,reverse=True)
    
    for i in range(k):
        topElements.append(int(sortedElements[i].rstrip('a')))
    return topElements

nums = [1,1,2,2,3,3,3,4]
k = 2
ans=topK(nums,k)
print(ans)