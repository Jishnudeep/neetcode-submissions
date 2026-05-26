class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        high = len(numbers)-1
        low = 0
        

        while low < high: 
            compute = numbers[low] + numbers[high]
            
            if compute > target: 
                high = high - 1
            elif compute < target:
                low = low + 1
            else:
                return [low + 1, high + 1]

        return []