class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)     #Keep recursively working as we keep adding K value of combinations 
                comb.pop()
        backtrack(1, [])                         #Choose values between 1 and n 
        return res              