#Day-6-Reverse-a-Number
num=int(input("enter your number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=(reverse*10)+digit 
    num=num//10
print("Reverse number:",reverse)
#Time Complexity:O(log n)
#Space Complexity:O(1)
