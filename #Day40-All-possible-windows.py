#Day40-All-possible-windows
arr=[2,1,4,8,5,3]
k=3
for i in range((len(arr)-k)+1):
    print(arr[i:i+k])
#Time complexity:O(nk) k is constant
#Space complexity:O(k)

