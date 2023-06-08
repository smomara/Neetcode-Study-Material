class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(set(nums))

        i = len(nums) - 2
        longest = 1

        count = 1
        while i >= 0:
            if nums[i] == nums[i + 1] - 1:
                count += 1
            else:
                count = 1

            longest = max(longest, count)

            i -= 1
        
        return longest