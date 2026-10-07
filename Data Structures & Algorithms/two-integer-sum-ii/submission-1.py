class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        index1 = 0 
        index2 = n-1
        while(numbers[index1] + numbers[index2] != target):
            if numbers[index1] + numbers[index2] > target:
                index2-=1
            if numbers[index1] + numbers[index2] < target:
                index1+=1
        return [index1+1,index2+1]
            
        