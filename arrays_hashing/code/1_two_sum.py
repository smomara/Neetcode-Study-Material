class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen:
                return [seen[x], i]
            seen[nums[i]] = i