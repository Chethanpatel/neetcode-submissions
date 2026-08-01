from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = dict(enumerate(nums))

        for i in range(len(nums)):
            complement = target - nums[i]

            j = next(
                (k for k, v in maps.items()
                 if v == complement and k != i),
                None
            )

            if j is not None:
                return [i, j]