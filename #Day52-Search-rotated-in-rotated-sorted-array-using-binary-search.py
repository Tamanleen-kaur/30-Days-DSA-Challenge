#Day52-Search-rotated-in-rotated-sorted-array-using-binary-search
nums=[7,8,9,1,2,3,4]
mini=float("inf")
start=0
end=len(nums)-1
while start<=end:
    mid=(start+end)//2
    if nums[mid]<=nums[end]:
        mini=min(mini,nums[mid])
        end=mid-1
    else:
        mini=min(mini,nums[start])
        start=mid+1
print(mini)
#Time complexity:O(log n)
#Space complexity:O(1)
