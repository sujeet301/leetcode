class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        answer = 0

        for i, num in enumerate(nums):
            if i < n // 2:
                answer -= num * num
            else:
                answer += num * num

        return answer