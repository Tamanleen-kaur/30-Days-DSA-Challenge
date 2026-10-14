#Day44-Index-of-lower-bound
arr=[1,2,4,4,5,7]
start=0
end=len(arr)-1
target=4
while start<=end:
    mid=(end+start)//2
    if arr[mid]>=target:
        end=mid-1
    else:
       start=mid+1
print("index of lower bound element is:",start)
#Time complexity:O(log n)
#Space complexity:O(1)
