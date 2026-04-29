class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # declare variables
        res = dict()
        res_list = []
        # count each frequency in n
        for val in nums:
            res[val] = res.get(val, 0) + 1
        # we sort to get top k
        return list(sorted(res, key=lambda x: res[x], reverse=True))[:k]