class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set([])
        n = len(nums)
        for i in range(n):
            if (nums[i] in hs):
                return True
            hs.add(nums[i])
        return False