class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        prevChars = set()
        longestString = 0

        for right in range(len(s)):
            while s[right] in prevChars:
                prevChars.remove(s[left])
                left+=1
            prevChars.add(s[right])
            longestString = max(longestString, right-left+1)
        return longestString

        