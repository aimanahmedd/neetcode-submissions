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

'''
okay so my solution is pretty straight forward but i would not come up with this
if was in an actual interview. basically what i started out with doing is making an
array, and collecting all the multiplications from the left side of each number. and
you first have to put the current multiplication in the array AND then change the 
multiple. so for example:
if our arrya is [1,2,4,6]
the left multipls would be [1, 1, 2, 8] because this represents each multiplication
to the left of each number
next i went through the right side and basically started at the last index, and would 
go backwards. I would then take the current right multiplication we were on and 
multiply it with what was at the index in the answer array, because this basically 
gives the multiplication of everything to the left and everything to the right of this
number. so then i would change the right multiplication and multiply it with the
number in nums[i]
i would last return the answer array!
'''