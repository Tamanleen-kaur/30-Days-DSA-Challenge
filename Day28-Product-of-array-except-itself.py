#DAY28-PRODUCT OF ARRAY EXCEPT ITSELF (BRUTE FORCE)
arr=[1,2,3,4]
prefix=[1]*len(arr)
suffix=[1]*len(arr)
result=[1]*len(arr)
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]*arr[i-1]
for i in range(len(arr)-2,-1,-1):
    suffix[i]=suffix[i+1]*arr[i+1]
for i in range(len(arr)):
    result[i]=prefix[i]*suffix[i]
print(result)
#Time complexity:O(n)
#Space complexity:O(n)



#PRODUCT OF ARRAY EXCEPT ITSELF (OPTIMIZED)
arr=[1,2,3,4]
result=[1]*len(arr)
for i in range(1,len(arr)):
    result[i]=result[i-1]*arr[i-1]
suffix=1
for i in range(len(arr)-2,-1,-1):
    suffix=suffix*arr[i+1]
    result[i]=result[i]*suffix
print(result)
#Time complexity:O(n)
#Space complexity:O(1)

