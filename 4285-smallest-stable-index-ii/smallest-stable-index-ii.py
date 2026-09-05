class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # Store minimum from i to the end
        right = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        left = 0

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1