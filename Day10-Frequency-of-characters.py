#Day10-Frequency-of-characters
string=input("enter your string:")
freq={}
for ch in string:
    freq[ch]=freq.get(ch,0)+1
print(freq)
#Time complexity:O(n)
#Space complexity:O(n)
