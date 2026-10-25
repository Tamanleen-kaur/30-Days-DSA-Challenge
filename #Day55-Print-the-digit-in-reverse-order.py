#Day55-Print-the-digit-in-reverse-order
num=int(input("enter the number:"))
while num>0:
    digit=num%10
    print(digit)
    num=num//10
#Time complexity:O(log n)
#Space complexity:O(1)
