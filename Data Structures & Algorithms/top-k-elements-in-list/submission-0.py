class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        bucket_arr = [[] for i in range(len(nums)+1)]

        for num, freq in hashmap.items():
            bucket_arr[freq].append(num)

        res =[]

        for i in range(len(bucket_arr)-1, 0, -1):
            for num in bucket_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res