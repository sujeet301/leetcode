class Solution(object):
    def findMissingElements(self, nums):
        seen = set(nums)

        result = []

        for i in range(min(nums), max(nums) + 1):
            if i not in seen:
                result.append(i)

        return result