#Day43-Check-whether-one-string-is-rotation-of-another
original_string="abcd"
check_string="cdab"
if len(original_string)!=len(check_string):
    print("Not possible due to length")
else:
    original_string=original_string+original_string #abcdabcd
    if check_string in original_string:
        print(check_string,"is rotation")
    else:
        print(check_string,"is not rotation")
#Time complexity:O(n)
#Space complexity:O(n)
