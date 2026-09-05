#Day-5-Fibonacci-series
num=int(input("enter your number:"))
a=0
b=1
while a<=num:
    print(a,end="") 
    a,b=b,a+b 
#Time complexity:o(n) 
#Space complexity:o(1)
