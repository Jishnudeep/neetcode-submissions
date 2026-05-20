class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force 
        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i!=j: 
                    product *= nums[j]
                
            output.append(product)

        return output