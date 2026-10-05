class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = set([])
        j = 0
        for i in range(len(nums)):
            if (target-nums[i]) in hs:
                for k in range(len(nums)):
                    if (nums[k] == target - nums[i]):
                        return [k, i]
            hs.add(nums[i])

        
