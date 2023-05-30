class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits [::-1]  #Reverses the order of the array into list for us to start working from last digit forward to the first digit 
        one, i = 1, 0           #Given value one since we need to atleast add 1 and we initialized it to position 0

        while one:
            if i < len(digits):         #Makes sure that i is atleast inbounds
                if digits[i] == 9:
                    digits[i] = 0
                else:                       #If I is out of bounds we will be incrementing 
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1] #Reverses back into the correct format 