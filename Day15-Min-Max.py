#Find the minimum and maximum element from an array
arr=[5,7,3,4,6,1]
min_no=float("inf")
max_no=float("-inf")
for num in arr:
    if num<min_no:
        min_no=num
    elif num>max_no:
        max_no=num
print("max number is:",max_no)
print("min number is:",min_no)
#Time complexity:O(n)
#Space complexity:O(1)

