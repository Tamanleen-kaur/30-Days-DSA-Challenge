#Day25-Merge-sorted-array
arr1=[1,3,5,7]
arr2=[2,4,6,8]
arr_ans=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        arr_ans.append(arr1[i])
        i=i+1
    else:
        arr_ans.append(arr2[j])
        j=j+1
while i<len(arr1):
    arr_ans.append(arr1[i]) #Insert remaining elements
    i=i+1
while j<len(arr2):
    arr_ans.append(arr2[j])#Insert remaining elements
    j=j+1
print(arr_ans)
#Time complexity:O(n)
#Space complexity:O(n)
