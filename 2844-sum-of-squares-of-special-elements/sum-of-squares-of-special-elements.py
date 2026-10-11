class Solution(object):
    def sumOfSquares(self, nums):
        n= len(nums)
        sum=0
        for i, num in enumerate(nums):
            if n%(i+1)==0:
                sum= sum +nums[i]**2
        
        return sum
        