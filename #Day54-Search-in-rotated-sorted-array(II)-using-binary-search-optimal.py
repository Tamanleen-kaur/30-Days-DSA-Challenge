#Day54-Search-in-rotated-sorted-array(II)-using-binary-search-optimal.
arr=[7,7,7,7,7,7,7,1,2,3,4,5,7,7]
start=0
target=1
end=len(arr)-1
while start<=end:
    mid=(start+end)//2
    if arr[mid]==target:
        print(mid)
        break
    if arr[start]==arr[mid]==arr[end]:
        start+=1
        end-=1
    elif arr[mid]<=arr[end]:
        if arr[mid]<target<=arr[end]:
            start=mid+1
        else:
            end=mid-1
    else:
        if arr[start]<=target<arr[mid]:
              end=mid-1
        else:
             start=mid+1
else:
    print(-1)
#Time complexity:O(n)
#Space complexity:O(1)
