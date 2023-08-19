class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]       #Keep track of previous end value
        for start, end in intervals[1:]:    #Iterate through remaining list of intervals starting at index 1
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1            #We are only keeping track of how many items we deleted 
                prevEnd = min(end, prevEnd)
        return res 

