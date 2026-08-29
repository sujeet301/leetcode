class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # Sort by value
        arr.sort()

        ans = [0] * n

        i = 0

        while i < n:
            j = i

            # Find all values connected by the limit
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Get original indices of this group
            indices = []

            for k in range(i, j + 1):
                indices.append(arr[k][1])

            # Sort indices
            indices.sort()

            # Values are already sorted
            for k in range(len(indices)):
                ans[indices[k]] = arr[i + k][0]

            i = j + 1

        return ans