class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force
        # for i in range(len(nums)):
        #     checker = nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
            
        # return False

        #hashmap approach 
        result_set = set()

        for num in nums: 
            if num in result_set:
                return True
            result_set.add(num)
        
        return False

            