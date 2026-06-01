class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = set()
        maxCount = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            tmp = right-left+1
            if tmp > maxCount:
                maxCount = tmp
        return maxCount