class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        result  = 0 

        for num in nums:
            current, streak = num, 0

            while current in hashset:
                streak += 1
                current += 1

            result = max(result, streak)
            
        return result
