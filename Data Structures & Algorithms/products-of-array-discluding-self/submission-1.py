class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        s = set(nums)
        counter = False
        if 0 in s:
            for n in nums:
                if counter and (n == 0):
                    return [0 for n in nums]
                else:    
                    if n!=0:
                        product = n*product
                    else:
                        counter = True
            return [(n == 0)*int(product) for n in nums]
        for n in nums:
            product = n*product
        ans = [int(product/n) for n in nums]
        return ans