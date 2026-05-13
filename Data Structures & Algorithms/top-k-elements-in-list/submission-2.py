from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        b = [[] for item in range(len(nums)+1)]
        o = []
        for item in nums:
            a[item]+=1
        for item, f in a.items():
            b[f].append(item)
        for item in reversed(b):
            if not item:
                continue
            if k>len(item):
                o.extend(item)
                k = k-len(item)
            else:
                o.extend(item[:k])
                break
        return o