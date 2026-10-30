#Day60-To-store-the-reverse-number
num=int(input("enter your number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=(reverse*10)+digit 
    num=num//10
print(reverse)
#Time complexity:O(log n)
#Space complexity:O(1)
