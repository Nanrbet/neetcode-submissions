class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 7 - 3 = 4 {4:i, 1:3}
        seen = dict()
        for i,v in enumerate(nums):
            if v in seen:
                return [seen[v], i] # first number index and the index of the difference
            seen[target-v] = i