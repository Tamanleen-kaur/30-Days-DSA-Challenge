#Day53-Search-in-rotated-sorted-array(II)-using-binary-search
arr=[7,7,7,7,7,7,7,1,2,3,4,5,7,7]
target=1
found=False
for i in range(len(arr)):
    if arr[i]==target:
        found=True
        break
print(found)
#Time complexity:O(n)
#Space complexity:O(1)
