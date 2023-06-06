class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [
            -s for s in stones
        ]  # Python has no max heaps so we are initializing with min heaps by making it negative(-8) then pulling the true value (8)
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
