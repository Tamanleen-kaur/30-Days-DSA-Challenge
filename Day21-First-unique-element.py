#Day21-First-unique-element
arr=[3,4,5,3,2,4,1,5]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
print(freq)
for num in freq:
    if freq[num]==1:
        print(num)
        break
#Time complexity:O(n)
#Space complexity:O(n)
