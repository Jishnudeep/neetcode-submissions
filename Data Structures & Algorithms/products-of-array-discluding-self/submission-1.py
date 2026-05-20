class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l 

        prefix = 1
        #1st forward pass
        for i in range(l):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        print(res)

        postfix = 1
        for i in range(l-1, -1, -1):
            res[i] = res[i] * postfix 
            postfix = postfix * nums[i]

        print(res)

        return res

