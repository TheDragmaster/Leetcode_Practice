class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r =0, len(nums) - 1                                  #Using binary search to find the target and increasing efficency by finding mid point from first and last value and searching 
                                                                # forward if the value is smaller than the mid point and so on and so forward. We use 2 pointers to calculate mid point 
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m 
        return -1