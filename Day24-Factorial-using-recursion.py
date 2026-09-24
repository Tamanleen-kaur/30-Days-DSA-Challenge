#Day24-Factorial-using-recursion
def fact(num):
    if num<1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))
#Time complexity:  O(n)
#Space complexity:  O(n) because of recursion call stack
