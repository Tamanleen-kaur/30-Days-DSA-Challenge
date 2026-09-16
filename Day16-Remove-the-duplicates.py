#Day16-Remove-the-duplicates
arr=[2,3,4,3,5,7,5,8,1,8]
unique=set()
for num in arr:
    if num not in unique:
        unique.add(num)
print(unique)
#Time complexity:O(n) By using set
#Space complexity:O(n)


arr=[2,3,4,3,5,7,5,8,1,8]
unique=set()
for num in arr:
    if num not in unique:
        unique.add(num)
print(unique)
#Time complexity:O(n^2) By using list
#Space complexity:O(n)
