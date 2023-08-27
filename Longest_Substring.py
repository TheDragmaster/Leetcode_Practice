#Make a set for the substring to make sure you do not end up with a duplicate 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0       #Initialize the left pointer 
        res = 0

        for r in range (len(s)):            # Initialize the right pointer 
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
