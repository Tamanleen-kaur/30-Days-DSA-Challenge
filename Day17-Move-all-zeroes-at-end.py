#Day17-Move-all-zeroes-at-end
arr=[0,4,0,2,7,0,3,0,5]
i=0
j=0
while j<len(arr):
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
        j=j+1
    elif arr[j]==0:
        j=j+1
print(arr)
#Time complexity:O(n)
#Space complexity:O(1)
