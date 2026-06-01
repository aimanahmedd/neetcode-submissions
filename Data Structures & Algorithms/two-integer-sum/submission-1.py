class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}

        for i in range(len(nums)):
            ans = target - nums[i]

            if ans in prevNums:
                return [prevNums[ans], i]
            else:
                prevNums[nums[i]] = i


        '''
        7+2 = 9
        9 - 2 = 7
        

        prev nums = {}

        for index in nums:
            subtratcion answer = target - nums[index]

            if answer in prevNums:
                return [prevNums[answer], index]
            else:
                prevNums[nums[index]] = index
        '''