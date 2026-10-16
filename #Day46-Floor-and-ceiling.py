#Day46-Floor-and-ceiling
arr = [2, 4, 6, 8, 10]
target = 7
floor=-1
ceiling=-1
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        floor=arr[mid]
        ceiling=arr[mid]
    elif arr[mid]<target:
        floor=arr[mid]
        left=mid+1
    else:
        ceiling=arr[mid]
        right=mid-1
print(floor)
print(ceiling)
#Time complexity:O(log n)
#Space complexity:O(1)
