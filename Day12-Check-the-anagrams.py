#Day12-Check-the-anagrams
string1="listen"
string2="silent"
freq1={}
freq2={}
for ch in string1:
    freq1[ch]=freq1.get(ch,0)+1
print(freq1)
for ch in string2:
    freq2[ch]=freq2.get(ch,0)+1
print(freq2)
if freq1==freq2:
    print("anagrams")
else:
    print("not anagrams")
#Time Complexity:O(n)
#Space Complexity:O(n)
