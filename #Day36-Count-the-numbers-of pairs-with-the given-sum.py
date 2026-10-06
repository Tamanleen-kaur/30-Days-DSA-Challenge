#Day36-Count-the-numbers-of pairs-with-the given-sum
arr = [1, 1, 3]
target = 4
freq = {}
count = 0
for num in arr:
    needed = target - num
    if needed in freq:
        count += freq[needed] 
    freq[num] = freq.get(num, 0) + 1
print(count)
#Time complexity:O(n)
#Space complexity:O(n)
