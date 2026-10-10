class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = []

        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))

        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2

            needed = 0
            for d in diff:
                if d > mid:
                    needed += d - mid

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        answer = 0

        for i in range(len(diff)):
            if diff[i] > left:
                k -= diff[i] - left
                diff[i] = left

        for i in range(len(diff)):
            if k == 0:
                break

            if diff[i] == left and diff[i] > 0:
                diff[i] -= 1
                k -= 1

        for d in diff:
            answer += d * d

        return answer