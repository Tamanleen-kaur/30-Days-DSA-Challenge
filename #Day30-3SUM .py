#Day30-3SUM (BRUTE FORCE APPROACH)
arr=[-1,0,1,2,-1,-4]
result=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==0:
                triplet=sorted([arr[i],arr[j],arr[k]])
                if triplet not in result:
                    result.append(triplet)
print(result)
#Time complexity:O(n^3)
#Space complexity:O(n)


# 3SUM (OPTIMAL APPROACH) 
nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
nums.sort()
ans=[]
for i in range(len(nums)):
    if i!=0 and nums[i]==nums[i-1]: #i!=0 means on at index 0 
        continue
    j=i+1
    k=len(nums)-1
    while j<k:
        total_sum=nums[i]+nums[j]+nums[k]
        if total_sum>0:
            k-=1
        elif total_sum<0:
            j+=1
        else:
            temp=[nums[i],nums[j],nums[k]]
            ans.append(temp)
            j+=1
            k-=1
            while j<k and nums[j]==nums[j-1]:
                j=j+1
            while j<k and nums[k]==nums[k+1]:
                k=k-1
print(ans)
#Time complexity:O(n^2)
#Space complexity:O(1)
