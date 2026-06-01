class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newSortedList = sorted(nums)
        answerArray = []

        for i in range(len(newSortedList)):
            if i > 0 and newSortedList[i] == newSortedList[i-1]:
                continue

            left = i+1
            right = len(newSortedList)-1
            while right > left:
                threeSum = newSortedList[i] + newSortedList[left]+ newSortedList[right]
                
                if threeSum < 0:
                    left+=1
                elif threeSum > 0:
                    right-=1
                else:
                    answerArray.append([newSortedList[i], newSortedList[left], newSortedList[right]])
                    left+=1

                    while right > left and newSortedList[left] == newSortedList[left-1]:
                        left+=1
        return answerArray


    '''
      [-4, -1, -1, -1 0, 1, 2]

      sortedList = sort(nums)
      answerArray = []

      for i in range(len(sortedList))
        if i > 0 and sortedList[i] == sortedList[i-1]:
            continue

        left = i+1
        right = len(sortedList) - 1

        while right > left:
            sum = sortedList[i] + sortedList[left] + sortedList[right]

            if sum < 0:
                left+=1
            elif sum > 0:
                right -=1
            else:
                answerArray.append([sortedList[i], sortedList[left], sortedList[right]])
                left+=1
                while right > left and sortedList[left] == sortedList[left-1]:
                    left+=1
        return answer
    '''



        