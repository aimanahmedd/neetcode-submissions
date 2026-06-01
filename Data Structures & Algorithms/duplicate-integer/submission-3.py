class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmapTracker = {}
        for num in nums:
            if num not in hashmapTracker:
                hashmapTracker[num] = 1
            else:
               return True
        return False