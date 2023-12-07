#Create a dict with counts as key and array of elements with their count equal to key
#sort the keys and append their values to an array until length of array >=k
#return k element of the array
def topK( nums, k):
	topElements=[]
	elementCount={}
	elements=list(set(nums))
	elements.sort(reverse=True)
	for i in elements:
		c=nums.count(i)
		elementCount[c]=elementCount.get(c,[])
		elementCount[c].append(i)
	counts=list(elementCount.keys())
	counts.sort(reverse=True)
	i=0
	while(len(topElements)<k):
		topElements.extend(elementCount[counts[i]])
		i+=1
	return topElements[:k]

nums = [1,1,2,2,3,3,3,4]
k = 2
ans=topK(nums,k)
print(ans)