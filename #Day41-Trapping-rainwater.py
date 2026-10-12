#Day41-Trapping-rainwater
container=[4,2,0,3,2,5]
ans=0
l_max=0
r_max=0
lp=0
rp=len(container)-1
while lp<rp:
    l_max=max(l_max,container[lp])
    r_max=max(r_max,container[rp])
    if l_max<r_max:
        ans=ans+l_max-container[lp]
        lp=lp+1
    else:
        ans=ans+r_max-container[rp]
        rp=rp-1
print("Max water trapped in container:",ans)
#Time complexity:O(n)
#Space Complexity:O(1)
