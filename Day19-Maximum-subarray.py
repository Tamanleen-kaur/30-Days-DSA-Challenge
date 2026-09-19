#Day19-Maximum-subarray
#Method1 (BRUTE FORCE)
arr=[1,4,3,2,6]
max_subarray=float("-inf")
for i in range(0,len(arr)):
    curr_sum=0
    for j in range(i,len(arr)):
        curr_sum=curr_sum+arr[j]
    if max_subarray<curr_sum:
        max_subarray=curr_sum
print("Maximum subarray sum:",max_subarray)
#Time complexity:O(n^2)
#Space complexity:O(1)


#Method2 (OPTIMAL WAY)
arr=[1, -2, 4, 5, -7, 0, 6] 
curr_sum = 0
subarray_sum = arr[0]
for i in range(len(arr)):
    curr_sum = curr_sum + arr[i]
    if curr_sum > subarray_sum:
        subarray_sum = curr_sum
    if curr_sum < 0:
            curr_sum = 0
print("Maximum subarray sum:",subarray_sum)
#Time complexity:O(n)
#Space complexity:O(1)
