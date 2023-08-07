class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1  #Basically definint bit so we can initializwe n so we can start reading
            res = res | (bit << (31 - i)) #Lets us grab the first value of the array and move it to the last bit 
        return res 
 