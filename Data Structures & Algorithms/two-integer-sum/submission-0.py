class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            d = target - n
            if d in prev:
                m = prev[d]
                return [m,i]
            prev[n] = i