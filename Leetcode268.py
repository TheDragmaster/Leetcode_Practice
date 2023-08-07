class Solution:
    def missingNumber(self, nums: List[int]) -> int:        #nums is the input array 
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res
        

        #We use XOR(exclusive or) to compare the bit value of our input and the bit value of the array range and get the difference and print the missing value 