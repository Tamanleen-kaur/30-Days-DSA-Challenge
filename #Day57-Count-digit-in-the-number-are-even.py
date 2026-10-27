#Day57-Count-digit-in-the-number-are-even
count=0
num=1234567
i=0
while num!=0:
    digit=num%10
    if digit%2==0:
        count+=1
    num=num//10
print("number of digits:",count)
#Time complexity:O(log n)
#Space complexity:O(1)
