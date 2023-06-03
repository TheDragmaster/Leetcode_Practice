class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # We are using backtracking for efficiency and we are only computing from one set of computations to be efficient since both computations will bring the exact same results

        mod = 10**9 + 7
        dp = {}

        def dfs(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]

            dp[length] = 1 if length >= low else 0
            dp[length] += dfs(length + zero) + dfs(length + one)
            return dp[length] % mod

        return dfs(0)
