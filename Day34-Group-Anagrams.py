#Day34-Group-Anagrams
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
freq = {}
for word in words:
    key="".join(sorted(word))
    if key not in freq:
        freq[key]=[]
    freq[key].append(word)
ans=list(freq.values())
print(ans)
#Time Complexity:O(n k log k)
#Space Complexity:O(n k)
