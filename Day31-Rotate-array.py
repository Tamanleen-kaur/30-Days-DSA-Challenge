#Day31-ROTATE LIST (USING BUILT-IN FUNCTION)
k=int(input("enter the value of k:"))
arr=[1,2,3,4,5,6,7,8]
k=k%len(arr) 
arr[:k]=reversed(arr[:k])
arr[k:]=reversed(arr[k:])
print(arr)
#Time Complexity:O(n)
#Space Complexity:O(n)







#RIGHT ROTATE LIST (TWO POINTERS)
def rotate(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
arr=[1,2,3,4,5,6,7,8,9] 
k=int(input("enter the value of k:"))
k= k % len(arr)
#first reverse the whole array
rotate(arr,0,len(arr)-1)
#second reverse k elements of array
rotate(arr,0,k-1)
#third reverse n-k elements of array
rotate(arr,k,len(arr)-1)
print(arr)
#Time complexity:O(n)
#Space complexity:O(1) 



#LEFT ROTATE LIST(TWO POINTERS)
def rotate(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
arr=[1,2,3,4,5,6,7,8,9]
k=int(input("enter the value of k:")) 
k=k%len(arr)
#first reverse k elements of array
rotate(arr,0,k-1)
#second reverse n-k elements of array
rotate(arr,k,len(arr)-1)
#third reverse the whole array
rotate(arr,0,len(arr)-1)
print(arr) 
#Time complexity:O(n) 
#Space complexity:O(1)


