class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)  # Maps every character into the count
        buckets = defaultdict(
            list
        )  # freq of character is going to be mapped to a list of those characters / bucketsort

        for char, cnt in count.items():
            buckets[cnt].append(char)

        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        return "".join(res)
