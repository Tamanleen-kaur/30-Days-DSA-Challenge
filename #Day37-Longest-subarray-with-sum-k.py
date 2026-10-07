#Day37-Longest-subarray-with-sum-k
arr=[10,5,2,7,1,9]
prefix_sum=0
seen={}
k=15 #target
max_length=float("-inf")
for i in range(len(arr)):
    prefix_sum=prefix_sum+arr[i]
    if prefix_sum==k:
        max_length=i+1
    if prefix_sum-k in seen:
        length=i-seen[prefix_sum-k] #[current_index-old_index]
        max_length=max(length,max_length)
    if prefix_sum-k not in seen:
        seen[prefix_sum]=i
print("the length of the longest subarray is:",max_length)
#Time complexity:O(n)
#Space complexity:O(n)
