#Day-9-Count-the-vowels
string=input("enter the string:")
count=0
for ch in string:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
        count+=1
print("no. of vowles are",count)
#Time complexity:O(n)
#Space complexity:O(1)
