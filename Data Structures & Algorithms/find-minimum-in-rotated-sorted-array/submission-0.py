class Solution:
    def findMin(self, nums: List[int]) -> int:
        numMin = nums[0]
        for num in nums:
           numMin = min(numMin, num)
        return numMin 
        