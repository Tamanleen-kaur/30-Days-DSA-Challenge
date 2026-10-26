#Day56-Find-the-perfect-square
num=int(input("enter the number:"))
is_square=False
for i in range(1,num+1):
    if i*i==num:
        is_square=True
        break
if is_square:
    print(num,"is a perfect square")
else:
    print(num,"is a not perfect square")
#Time complexity:O(n)
#Space complexity:O(1)
