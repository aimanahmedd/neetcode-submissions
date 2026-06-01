class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencyCount = {}
        left = 0
        answer = 0

        for right in range(len(s)):
            if s[right] in frequencyCount:
                frequencyCount[s[right]]+=1
            else:
                frequencyCount[s[right]] = 1
            
            while (right-left+1) - max(frequencyCount.values()) > k:
                frequencyCount[s[left]] -=1
                left+=1
            answer = max(answer, right-left+1)
        return answer
        