#Day20-Prefix-sum
arr=[2,4,1,5,3]
for i in range(1,len(arr)):
    arr[i]=arr[i-1]+arr[i]
print(arr)
#Time complexity:O(n)
#Space complexity:O(1)
