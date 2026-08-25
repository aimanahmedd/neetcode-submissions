class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        understand:
        input: string s
        output: length of the longest substring without duplicate characters

        "zxyzxyz"
        -> 3: xyz longest substring with no duplicate characters

        s.length between 0 and 50k
        only ASCII characters

        can be all repeating same characters

        match:
            sliding window to keep track of window of substring

        plan:
            1. left and right pointer equal to 0 (first char in s)
            2. create a hashmap to keep track of prev chars
            create variable to keep track of longest
            3. while right < len(s):
                    while s[right] in prevChars:
                        prevChars.pop(s[left])
                        left+=1

                prevChars[s[right]] = 1
                right+=1
                longest = max(longest, len(prevChars))

            4. return prevChars
        '''
        left, right = 0, 0
        longest = 0
        prevChars = {}
        while right < len(s):
            while s[right] in prevChars:
                prevChars.pop(s[left])
                left+=1
            prevChars[s[right]] = 1
            right+=1
            longest = max(longest, len(prevChars))
        return longest
        