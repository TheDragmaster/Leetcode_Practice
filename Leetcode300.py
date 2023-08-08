class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)                   #LIS = Longest Increaseing Subset

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:                # I needs to be bigger than J to continue potentially increasing the subset
                    LIS[i] = max (LIS[i], 1 + LIS[j])   # IF condition above is true then update LIS
        return max(LIS)