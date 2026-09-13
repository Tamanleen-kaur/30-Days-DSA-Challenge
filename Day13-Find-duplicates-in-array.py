#Day13-Find-duplicates-in-array
arr=[2,3,5,3,2,6,1,9,7,2]
unique=set()
duplicates=set()
for i in range(len(arr)):
    if arr[i] in unique:
        duplicates.add(arr[i])
    else:
        unique.add(arr[i])
print(duplicates)
#Time complexity:O(n)
#Space complexity:O(n)
