class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l,r):
            p = l
            for j in range(l,r):
                if nums[j] <= nums[r]:
                    nums[p], nums[j] = nums[j], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                return quickSelect(p+1, r)
            elif p > k:
                return quickSelect(l, p-1)
            else:
                return nums[p]
        
        return quickSelect(0,len(nums)-1)
                
                

        

        