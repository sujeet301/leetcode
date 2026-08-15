class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)

        xor = 0
        count_zero = 0

        for num in nums:
            xor ^= num

            if num == 0:
                count_zero += 1

        if xor != 0:
            return n

        if count_zero == n:
            return 0

        return n - 1