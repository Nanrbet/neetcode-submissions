class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        left_prod = 1
        for i in range(n):
            res[i] = left_prod
            left_prod *= nums[i]
        right_prod = 1
        for i in range(n):
            res[n-i-1] *= right_prod
            right_prod *= nums[n-i-1]
        return res


            