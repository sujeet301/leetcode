class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        zero = nums.index(0)

        def check(step):
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n

                if nums[prev] > nums[curr]:
                    return False

            return True

        answer = float('inf')

        if check(1):
            answer = min(answer, zero)
            answer = min(answer, n - zero + 2)

        if check(-1):
            answer = min(answer, zero + 2)
            answer = min(answer, n - zero)

        if answer == float('inf'):
            return -1

        return answer