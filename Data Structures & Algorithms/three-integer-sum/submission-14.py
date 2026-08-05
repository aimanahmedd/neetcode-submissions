class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerArr = []
        nums.sort()

#[-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while right > left:
                tmp = nums[i] + nums[left] + nums[right]

                if tmp < 0:
                    left+=1
                elif tmp > 0:
                    right -=1
                else:
                    answerArr.append([nums[i], nums[left], nums[right]])
                    left+=1

                    while right > left and nums[left] == nums[left-1]:
                        left+=1

        return answerArr

        