class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerArray = []
        nums.sort()

        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1

            while right > left:
                tmp = nums[left] + nums[right] + nums[i]

                if tmp < 0:
                    left +=1
                elif tmp > 0:
                    right-=1
                else:
                    answerArray.append([nums[left], nums[right], nums[i]])
                    left+=1

                    while right > left and nums[left] == nums[left-1]:
                        left+=1
        return answerArray