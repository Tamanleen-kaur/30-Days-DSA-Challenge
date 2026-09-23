#Day23-Two-pointer-Two-sum
arr=[3,6,7,12,14,19,25]     
target_sum= 32
i=0
j=len(arr)-1
while i<j:
    curr_sum=arr[i]+arr[j]
    if curr_sum==target_sum:
        print("left:",arr[i],"right:",arr[j])
        break
    elif curr_sum>target_sum:
        j=j-1
    elif curr_sum<target_sum:
        i=i+1
    else:
        print("not found")
#Time complexity:O(n)
#Space complexity:O(1)
