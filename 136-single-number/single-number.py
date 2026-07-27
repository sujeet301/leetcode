class Solution(object):
    def singleNumber(self, nums):
        r=0
        for num in nums:
            r^=num
        return r
        