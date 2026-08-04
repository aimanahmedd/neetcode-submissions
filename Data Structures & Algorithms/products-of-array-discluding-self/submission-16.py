class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods, right_prods, answer_arr = [1]*len(nums), [1]*len(nums), [1]*len(nums)

        left_product, right_product = 1, 1

        for i in range(len(nums)):
            if i > 0:
                left_product = left_product * nums[i-1]
            left_prods[i] = left_product

        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                right_product = right_product * nums[i+1]
            right_prods[i] = right_product

        for i in range(len(answer_arr)):
            answer_arr[i] = left_prods[i] * right_prods[i]

        return answer_arr