class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    # This is a one-liner that has nothing to do with arrays and hashing, but it works and is fun
    # return not (len(nums) == len(set(nums)))

    
    # This is the solution that actually has to do with arrays and hashing
    seen = {}
    
    for num in nums:
      if num in seen:
        return True
      else:
        seen[num] = 1
        
    return False
