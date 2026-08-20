class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        understand:
        input: integer array of number and target number
        output: integer array of pair that add up to target number

        [1, 2, 3, 4] target is 3
        -> [1, 2]


        smallest length for numbers is 2 and biggest length is 30000
        -1000 and 1000
        target: -1000 and 1000

        match:
            two pointer method

        plan:
        1. create left and right pointer, first element and last element
        2. while right > left
            tmp = numbers[right] + numbers[left]

            if tmp < target:
                left+=1
            elif tmp > target:
                right-=1
            else:
                return [left+1, right+1]

        '''
        left, right = 0, len(numbers)-1

        while right > left:
            tmp = numbers[right] + numbers[left]

            if tmp < target:
                left+=1
            elif tmp> target:
                right-=1
            else:
                return [left+1, right+1]
        