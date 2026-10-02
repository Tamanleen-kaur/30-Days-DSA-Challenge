#Day32-2Sum-Using-Set
arr = [4, 7, 2, 9, 5, 1, 8]
target = 10
seen=set()
for num in arr:
    needed=target-num
    if needed in seen:
        print(needed,num)
        break
    else:
        seen.add(num)
#Time complexity:O(n)
#Space complexity:O(n)
