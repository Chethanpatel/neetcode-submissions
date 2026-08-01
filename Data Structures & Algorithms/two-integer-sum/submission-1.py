class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = dict(enumerate(nums))

        for i in range(len(nums)):
            if target - nums[i] in maps.values():
                return [i, next((k for k, v in maps.items() if v == target - nums[i] and k!=i) , None)]

        
        