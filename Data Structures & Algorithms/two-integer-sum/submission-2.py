class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_m = {k:v for v,k in enumerate(nums)}
        for index, item in enumerate(nums):
            if i_m.get(target - item) and i_m.get(target - item)!=index:
                return [index, i_m.get(target - item)]
        return []