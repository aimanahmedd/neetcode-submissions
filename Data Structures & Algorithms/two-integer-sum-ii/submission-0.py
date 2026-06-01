class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # '''
        # have a left and right pointer
        left = 0
        right = len(numbers)-1
        # make an array to return
        result = []
        # while the right is greater than left
        while right > left:
            ans = numbers[left] + numbers[right]

            if ans > target:
                right-=1
            elif ans < target:
                left+=1
            else:
                result.append(left+1)
                result.append(right+1)
                return result
        # calculate the sum for both pointers
        # if its too big bring down rihgt pointer
        # if its small bring up left pointer
        # if its equal append it to the array

        # return array
        # '''
        