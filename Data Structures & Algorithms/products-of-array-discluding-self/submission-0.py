class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1 #base for left side multiplication
        r_mult = 1 #base for right side multiplication
        answer_array = [1] * len(nums) #this will keep track of our multiplications in general

        for i in range(len(nums)):
            answer_array[i] = l_mult
            l_mult = l_mult * nums[i]

        #answer_array = [1, 1, 2, 8]  

        for i in range(len(nums)-1, -1, -1):
            answer_array[i] = answer_array[i] * r_mult
            r_mult = r_mult*nums[i]
        
        return answer_array
            


        #answer_array = [48,24,6,1]