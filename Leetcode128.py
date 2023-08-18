class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)          #Pass array into a set
        longest = 0

        for n in nums:
            #Check if it is the start of a sequence
            if(n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:    #Check current number 
                    length += 1         # Keep checking for consecutibve numbers to put into the set 
                longest = max(length, longest)
        return longest