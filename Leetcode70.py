# Using dynamic programming to simplify the problem as much as possible, We only need to keep track of 2 numbers and start from the end value to computer the 
# End solution 
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
