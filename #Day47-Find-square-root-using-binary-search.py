#Day47-Find-square-root-using-binary-search
n=30
i=0
j=n-1
ans=0
while i<=j:
    mid=(i+j)//2
    if mid**mid==n:
        ans=mid
        break
    elif mid**mid>n:
        j=mid-1
    else:
        ans=mid 
        i=mid+1
print(ans)
#Time complexity:O(n)
#Space complexity:O(1)
