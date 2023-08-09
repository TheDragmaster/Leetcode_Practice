class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)     #Cashe as an array, Also using top to bottom approach 
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):      #Shift pointer to start all the way at the end 
            for w in wordDict:
                if (i + len(w)) <= len(s) and s [i : i + len(w)] == w:  #Makes sure there is enough numbers to compare before starting anything 
                    dp[i] = dp[i + len(w)]
                if dp[i]:       #If dp of i is true then break 
                    break
        return dp[0]
