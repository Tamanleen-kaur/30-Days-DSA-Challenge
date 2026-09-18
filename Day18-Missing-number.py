#Day18-Missing-number
#Method1
arr=[3,1,0,5,2]
for num in range(0,6):
    if num not in arr:
        print(num,"this is a missing number")
#Time complexity:O(n^2)
#Space complexity:O(1)


#Method2
arr=[3,1,0,5,2]
for_sum=0
arr_sum=0
for num in range(0,6):
    for_sum=for_sum+num
print(for_sum)
for i in range(len(arr)):
    arr_sum=arr_sum+arr[i]
print(arr_sum)
missing_number=(for_sum)-(arr_sum)
print(missing_number,"is a missing number")
#Time complexity:O(n)
#Space complexity:O(1)


#Method3
arr=[3,1,0,5,2]
n=len(arr)
total_sum=n*(n+1)//2
arr_sum=0
for num in arr:
    arr_sum=arr_sum+num
missing_number=total_sum-arr_sum
print(missing_number,"is missing number")
#Time complexity:O(n)
#Space complexity:O(1)



