#Day29-Merge-overlapping-intervals
intervals=[[1,3],[2,6],[8,10],[9,11]]
intervals.sort()
merged=[intervals[0]]
for i in range(1,len(intervals)):
    if merged[-1][1]>=intervals[i][0]:
        merged[-1][1]=max(merged[-1][1],intervals[i][1])
    else:
        merged.append(intervals[i])
print(merged)
#Time complexity:O(n log n)
#Space complexity:O(n)
