class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}

        for num in nums:
            table[num] = table.get(num, 0) + 1
        
        return sorted(table, key = table.get, reverse = True)[:k]