#Day8-Check-palindrome-string
string=input("enter the string:")
reverse_string=string[::-1]
if string==reverse_string:
    print("yes our string is palindrome")
else:
    print("no string is not palindrome")
#Time complexity:O(n)
#Space complexity:O(n)
