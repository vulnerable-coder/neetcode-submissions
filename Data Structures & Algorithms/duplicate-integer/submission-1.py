class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_map = {}
        for item in nums:
            if not frequency_map.get(item):
                frequency_map[item] = 1
            else:
                frequency_map[item] += 1
        for _,val in frequency_map.items():
            if val>1:
                return True
        return False