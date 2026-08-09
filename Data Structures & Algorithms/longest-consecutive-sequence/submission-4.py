class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        if len(nums) == 0:
            return 0
        
        checks = 0
        init_result = 1
        result = 0
        for num in hash_set:
            if num-1 not in hash_set:
                start_seq = num

                while checks < len(hash_set):
                    start_seq += 1
                    if start_seq in hash_set:
                        init_result += 1
                    
                    checks+=1

            result = max(result, init_result)

        return result
