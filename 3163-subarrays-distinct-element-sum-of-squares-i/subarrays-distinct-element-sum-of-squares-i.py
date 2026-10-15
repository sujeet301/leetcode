class Solution(object):
    def sumCounts(self, nums):
        answer = 0
        n = len(nums)

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                answer += len(seen) ** 2

        return answer