#Day33-Longest-consecutive-sequence (BRUTE FORCE)
arr=[100,4,200,1,3,2]
arr.sort() 
current_length=1
max_length=1
i=0
j=len(arr)-1
while i<j:
    if arr[i]+1==arr[i+1]:
        current_length=current_length+1
        max_length=max(max_length,current_length)
        
    else:
        current_length=1
    i=i+1
print("length of consecutive sequence:",current_length)
#Time complexity:O(n logn)
#Space complexity:O(n)


#Longest-consecutive-sequence (OPTIMAL APPROACH)
arr=[100, 4, 200, 1, 3, 2]
num_set=set(arr)
max_length=0
for num in num_set:
    if num-1 not in num_set: 
        while num+1 in num_set:
            curr_length=curr_length+1
            num=num+1
            max_length=max(max_length,curr_length)
print(max_length)
#Time complexity:O(n)
#Space complexity:O(n)
