#Day58-Smallest-digit-in-a-number
num=int(input("enter the number:"))
small=9
while num>0:
    digit=num%10
    if digit<small:
        small=digit
    num=num//10
print("the smallest digit is:",small)
#Time complexity:O(log n)
#Space complexity:O(1)
