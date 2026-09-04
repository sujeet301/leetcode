class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # minimum from i to the end
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        # maximum from 0 to i
        left = 0

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1