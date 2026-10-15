class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        left = 1
        for i in range(n):                 # out[i] = product of everything LEFT of i
            out[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):     # multiply in everything RIGHT of i
            out[i] *= right
            right *= nums[i]
        return out
