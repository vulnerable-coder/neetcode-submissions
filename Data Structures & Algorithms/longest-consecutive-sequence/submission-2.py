class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        h = {k:i for i,k in enumerate(nums)}
        starts = []
        for item in nums:
            if h.get(item -1) is None and h.get(item+1) is not None:
                starts.append(item)
        m = 1
        for item in starts:
            p = item
            c = 0
            while h.get(p) is not None:
                c =c+1
                p =p+1
            if c>m:
                m=c
        return m