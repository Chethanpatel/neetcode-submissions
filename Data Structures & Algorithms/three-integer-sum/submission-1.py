class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()

                        if temp not in res:
                            res.append(temp)
                            
        return list(res)

