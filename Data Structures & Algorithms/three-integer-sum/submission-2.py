class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         list to return
        result = []
#         sort the list to be in order
        nums.sort()
#         loop through sorted list
        for i in range(len(nums)):

            # [-4, -1, -1, 0, 1, 2]
            if i > 0 and nums[i] == nums[i-1]:
                continue


#         two pointers method: left is number after current right is the last one
            left = i + 1
            right = len(nums)-1
#         get sum of all three numbers
            while right > left:
                totalSum = nums[i] + nums[left] + nums[right]
#         if the sum is too small, move up left
                if totalSum < 0:
                    left+=1
#         if the sum is too big, move down right
                elif totalSum > 0:
                    right-=1
#         if sum equals to zero, add to this the list
                else:
                    result.append([nums[i], nums[left], nums[right]])
#       move up left pointer so we get all combinations
                    left+=1

                    while right > left and nums[left] == nums[left-1]:
                        left+=1



        return result



# [-4, -1, -1, 0, 1, 2]
        
        