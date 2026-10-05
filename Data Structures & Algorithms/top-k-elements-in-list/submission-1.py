class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter([])
        ans = []
        for n in nums:
            c[n] += 1
        return [pair[0] for pair in c.most_common(k)]
