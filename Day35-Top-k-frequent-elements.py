#Day35-Top-k-frequent-elements
nums = [1,1,1,2,2,3]
freq={}
k=2
ans=[]
bucket=[[] for _ in range(len(nums)+1)] 
for num in nums:
    freq[num]=freq.get(num,0)+1
for num,count in freq.items():
    bucket[count].append(num)
for i in range(len(bucket)-1,0,-1):
    for num in bucket[i]:
        ans.append(num)
        if len(ans)==k:
            break
    if len(ans)==k:
        break
print(ans)
#Time complexity:O(n)
#Space complexity:O(n)
