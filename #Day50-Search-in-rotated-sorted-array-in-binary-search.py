#Day50-Search-in-rotated-sorted-array-in-binary-search
nums=[17,18,20,1,2,4,5,6,7,8,10,11,13,14,16]
target=5
start=0
end=len(nums)-1
while start<=end:
    mid=(start+end)//2
    if nums[mid]==target:
        print("target is at index:",mid)
        break
    if nums[mid]<=nums[end]:
        if nums[mid]<=target<=nums[end]:
            start=mid+1
        else:
            end=mid-1
    else:
        if nums[start]<=target<=nums[mid]:
            end=mid-1
        else:
            start=mid+1
else:
    print(-1)
#Time complexity:O(log n)
#Space complexity:O(1)
