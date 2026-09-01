#Day 01-Sum Of Numbers
#Method 1: Using a Loop
num=int(input("Enter a number:"))
total=0
for i in range(num+1):
    total=total+i
print("Total sum:",total)
#Time complexity:O(n)
#Space complexity:O(1)

#Method 2: Using Mathematical Formula
#Formula: n(n+1)/2
total_sum=num*(num+1)//2
print("Total sum using formula:",total_sum)
#Time complexity:O(1)
#Space complexity:O(1)


