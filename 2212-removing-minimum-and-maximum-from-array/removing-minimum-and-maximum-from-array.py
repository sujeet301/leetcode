class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Both from the left
        option1 = right + 1

        # Both from the right
        option2 = n - left

        # Min from left, max from right
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)