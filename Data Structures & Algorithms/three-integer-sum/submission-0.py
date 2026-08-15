class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = [-num for num in nums]

        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]+nums[j] in target:
                    result.append([nums[i], nums[j], -1*(nums[i]+nums[j])])

        print(result)
        return result