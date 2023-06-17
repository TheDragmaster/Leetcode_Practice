# Kind of like sliding window except the roght pointer stays at the end of the array and the left pointer keeps inching forward as it finds - values with the sums of values O(n)
# The brute force solution would be O(n^3) with 3 nested loops involved. Since we know we are only looking for the MaxSubArray we can ignore low values/ - values


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]  # Initialize everything to 0
        curSum = 0

        for n in nums:  # For each number in nums
            if curSum < 0:  # If current sum is less than 0,
                curSum = 0  # Reset the value
            curSum += n  # Add current number to n
            maxSub = max(maxSub, curSum)
        return maxSub
