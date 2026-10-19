#Day49-Search-in-rotated-sorted-array-using-linear-search
nums=[4,5,0,1,2,3]
target=1
for i in range(len(nums)):
    if nums[i]==target:
        print("element at index:",i)
        break
else:
    print(-1)
#Time complexity:O(n)
#Space complexity:O(1)
