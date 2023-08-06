class Solution:                                         # We use Dynamic programming to keep track of the bit values we have already calculated and that are repeated to find new values
    def countBits(self, n: int) -> List[int]:           #Basically avoid calculating a value we have already calculated 
        dp = [0] * (n + 1)
        offset = 1 #Highest power foumd 

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp 