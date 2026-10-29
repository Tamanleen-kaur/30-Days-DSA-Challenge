#Day59-Count-digits
count=0
num=1234567
i=0
while num!=0:
    num=num//10
    count+=1
print("number of digits:",count)
#Time complexity:O(log n)
#Space complexity:O(1)
