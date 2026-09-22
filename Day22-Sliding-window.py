#Day22-Sliding-window
arr=[2,1,4,8,5,3]
k=3
window=sum(arr[:k])
max_sum=window
for i in range(k,len(arr)):
    window=window+arr[i]-arr[i-k]
    if window>max_sum:
        max_sum=window
print(max_sum)
#Time complexity:O(n)
#Space complexity:O(1)
