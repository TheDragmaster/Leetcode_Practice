class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()             #Create a Hashset, increases space complexity to 0(n) instead of 0(1)

        for n in nums:               #Cycle through and keep adding to hashset until duplicate is found and return True if no duplicates then return False
            if n in hashset:
                return True
            hashset.add(n)
        return False