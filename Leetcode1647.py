class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        used_freq = set()
        res = 0



        for c, freq in count.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                res += 1

            used_freq.add(freq) # freq either unique or a 0
        return res