#Day48-koko-eating-bananas
piles = [3, 6, 7, 11]
h = 8
low = 1
high = max(piles)
while low < high:
    mid = low + (high - low) // 2
    hours = 0
    for pile in piles:
        hours += (pile + mid - 1) // mid
    if hours <= h:
        high = mid
    else:
        low = mid + 1
print(low)
#Time complexity:O(n log m) 
#Space complexity:O(1) 
