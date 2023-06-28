def mergeOverlappingIntervals(intervals):
    output = []
    # Write your code here.
     
    print("Print the interval" , intervals)
    intervals.sort(key = lambda  x: x[0])
    cur = intervals[0]
    output.append(cur)
    print("Print the after sort interval" , intervals)
    for i in intervals:
        print("print each element " , i)
        curStart , curEnd = cur
        nextStart , nextEnd = i

        if curEnd >= nextStart:
           cur[1]  = max(curEnd, nextEnd) 
        else:
            cur = i
            output.append(cur)
    
    return output
