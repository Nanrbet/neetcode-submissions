class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums[i] in set of subtracted
        # 7 - 3 = 4 {4:i, 1:3}
        res = dict()
        for i in range(len(nums)):

            if nums[i] in res:
                return [res[nums[i]], i]
            res[target-nums[i]] = i