class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]     #Reversing so that python starts from the right and works to the left for the binary addition 

        for i in range(max(len(a), len(b))):        #Make i start itterating at whatever the longest string is so it computes all the way to the end
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0      #ord converts the value into a integer
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2) # mod by 2 (It just works :p)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res
