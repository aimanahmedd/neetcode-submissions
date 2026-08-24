class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        allPrevChars = {}
        longest = 0

        while right < len(s):
            while s[right] in allPrevChars:
                allPrevChars.pop(s[left])
                left+=1

            allPrevChars[s[right]] = 1
            longest = max(longest, len(allPrevChars))
            right+=1
        return longest


        