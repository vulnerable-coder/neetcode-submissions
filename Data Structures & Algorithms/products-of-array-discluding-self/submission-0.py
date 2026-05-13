class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        k = 1
        pre.append(k)
        for i in range(1, len(nums)):
            k=k*nums[i-1]
            pre.append(k)
        k=1
        for i in range(len(nums)-2, -1, -1):
            k = k*nums[i+1]
            suf.append(k)
        s = list(reversed(suf))
        s.append(1)
        return [a * b for a, b in zip(s, pre)]