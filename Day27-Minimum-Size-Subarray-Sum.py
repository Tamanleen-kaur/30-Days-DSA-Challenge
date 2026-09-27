#Day27-Minimum-Size-Subarray-Sum
arr=[2,3,1,2,4,3]
curr_sum=0
left=0
target=7
min_len=float("inf")
for right in range(len(arr)):
    curr_sum=curr_sum+arr[right]
    while curr_sum>=target:
        min_len=min(min_len,right-left+1)
        curr_sum-=arr[left]
        left+=1
if min_len==float("inf"):
    print(0)
else:
    print(min_len)
#Time complexity:O(n)
#Space complexity:O(1)
