#Day39-Continous-subarrays-equal-to-sum-k
arr = [1, 2, 1, 2, 1]
k = 3
freq = {0: 1} 
count = 0
for num in arr:
    curr_sum += num
    if curr_sum - k in freq:
        count += freq[curr_sum - k]
    freq[curr_sum] = freq.get(curr_sum, 0) + 1
print("number of subarrays:",count)
#Time complexity:O(n)
#Space complexity:O(n)
