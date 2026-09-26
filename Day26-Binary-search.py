#Day26-Binary-search
arr=[2,3,4,5,6,7,8,9]
target=4
start=0
end=len(arr)-1
while start<=end:
    mid=(start+end)//2
    if arr[mid]>target:
        end=mid-1
    elif arr[mid]<target:
        start=mid+1
    elif arr[mid]==target:
        print("element found at:",mid)
        break
#Time complexity:O(log n)
#Space complexity:O(1)
