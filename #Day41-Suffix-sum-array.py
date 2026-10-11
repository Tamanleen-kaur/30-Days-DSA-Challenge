#Day41-SUFFIX SUM ARRAY
arr=[5,4,3,2,1]
suffix=[0]*len(arr)
suffix[-1]=arr[-1]
for i in range(len(arr)-2,-1,-1):
    suffix[i]=arr[i]+suffix[i+1]
print(suffix)
#Time complexity:O(n)
#Space complexity:O(n)
