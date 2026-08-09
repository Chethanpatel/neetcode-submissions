class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        if len(nums) == 0:
            return 0

        result = 1
        for num in hash_set:
            if num-1 not in hash_set:
                start_seq = num
                checks = 0
                while checks < len(hash_set):
                    start_seq += 1
                    if start_seq in hash_set:
                        result += 1
                    
                    checks+=1

        return result
