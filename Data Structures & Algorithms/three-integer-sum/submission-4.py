class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # '''
        # make an array to return (all array combos inside)
        result = []
        # sort the array to be in order
        nums.sort()
#[-4,-1,-1,0,1,2]
        # loop through the array
        for i in range(len(nums)):
        # left pointer to be the index after current index and right pointer to be last index
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
        # while right is greater than left
            while right > left:
        # calculate a sum and check if it equals 0
                tmp = nums[i] +nums[left] + nums[right]
        # if its less than 0 move up left
                if tmp < 0:
                    left+=1
                elif tmp > 0:
                    right-=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while right > left and nums[left] == nums[left-1]:
                        left+=1
        # if its greater than 0 move down right
        # if its equal to zero add to array

        # return array
        return result

        # '''
        