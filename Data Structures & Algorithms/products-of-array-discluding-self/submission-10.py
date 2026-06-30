class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [1]* len(nums)

        answer = [1] * len(nums)

        left_prod = 1
        right_prod = 1

        for i in range(len(nums)):
            if i == 0:
                left_prof = 1
            else:
                left_prod = left_prod * nums[i-1]
            left.append(left_prod)

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_prod = 1
            else:
                right_prod = right_prod * nums[i+1]

            right[i] = right_prod

        
        for i in range(len(answer)):
            answer[i] = left[i] * right[i]

        return answer
        