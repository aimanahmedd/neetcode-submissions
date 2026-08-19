class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        understand: 
        input: integer array of numbers and a target
        output: array of two numbers that add up to target

        the two numbers in output cannot be equal

        [2, 3, 3, 4]

        

        always exactly one solution

        match:
            two pointers solution and keep going up and down based of sum

        plan:

        nums.sort()
            1. left pointer = 0 right pointer = last elemetn in array

            2. while right> left:
                tmp = numbers[left] + numbers[right]

                if tmp < target:
                    left+=1
                elif tmp > target:
                    right-=1
                else:
                    if numbers[left] != numbers[right]:
                        return [numbers[left], numbers[right]]

        '''

        left, right = 0, len(numbers)-1

        while right > left:
            tmp = numbers[left] + numbers[right]

            if tmp < target:
                left+=1
            elif tmp> target:
                right-=1
            else:
                return [left+1, right+1]    

    