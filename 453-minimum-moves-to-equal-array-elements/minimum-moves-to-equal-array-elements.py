class Solution(object):
    def minMoves(self, nums):
        minimum = min(nums)
        answer = 0

        for num in nums:
            answer += num - minimum

        return answer
        