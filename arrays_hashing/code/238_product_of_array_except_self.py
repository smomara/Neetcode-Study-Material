class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(len(nums)):
            ret[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]
        
        return ret