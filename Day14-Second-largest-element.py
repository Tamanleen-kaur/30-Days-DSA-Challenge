#Day14-Second-largest-element (Only valid for positive numbers)
arr=[5,4,9,6,2]
first_largest=float("-inf")
second_largest=float("-inf")
for i in range(len(arr)):
    if first_largest<=arr[i]:
        first_largest=arr[i]
for i in range(len(arr)):
    if arr[i]<first_largest and arr[i]>second_largest:
        second_largest=arr[i]
print("second largest element:",second_largest)
#Time complexity:O(n)
#Space complexity:O(1)



#valid for both positive and negative numbers
arr=[-5,-4,-9,-6,-2]
first_largest=float("-inf")
second_largest=float("-inf")
for i in range(len(arr)):
    if first_largest<arr[i]:
        second_largest=first_largest (old largest gets second largest) 
        first_largest=arr[i]
    elif  first_largest>arr[i] and second_largest<arr[i] and arr[i]!=first_largest:
      second_largest=arr[i]
print(second_largest)
#Time complexity:O(n)
#Space complexity:O(1)
