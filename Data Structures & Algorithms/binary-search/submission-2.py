class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []: return -1
        n = len(nums)
        index1 = n-1
        index2 = int(n/2)
        check = True
        while (check):
            if (nums[index2] == target): return index2 
            if (nums[index1] == target): return index1 
            if nums[index2] < target:
                aux = index2
                index2 = int((index1 + index2)/2)
                if aux == index2: return -1
            if nums[index2] > target:
                aux = index2
                index2 = int(index2/2)
                index1 = aux
                if aux == index2: return -1