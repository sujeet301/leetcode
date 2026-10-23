class Solution(object):
    def sortPermutation(self, nums):
        answer = -1

        for i, num in enumerate(nums):
            if i != num:
                answer &= num

        return max(answer, 0)