class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Doing a greedy solution basically starting from the end and working our way to the beggining.
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
