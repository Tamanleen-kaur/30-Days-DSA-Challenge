#Day51-Search-min-rotated-sorted-array-using-linear-search
nums=[4,5,0,1,2,3]
mini=float("inf")
for i in range(len(nums)):
    mini=min(mini,nums[i])
print(mini)
#Time complexity:O(n)
#Space complexity:O(1)
