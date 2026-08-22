class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        understand:
        length of longest substring

        input: string s with a series of characters
        output: length of longest string

        string of multipl of same characters -> 1
        "zxyzxyz" -> 3 (xyz)

        upto 50k o(n)

        match:
            sliding window method to keep of track of all substrings
        
        plan:
        1. left and right pointer to point to the first element of string
        2. make longestlength var = equal
        3. make hashmap to keep track of all letters we see
        4. while right < len(s):
            if s[right] in hashmap:
                hashmap.pop(s[left])
                left+=1


            hashmap[s[right]] = 1
            right+=1

            longestlength = max(longestLength, len(hashmap))
        5. return longestlength
        '''
        left, right = 0, 0
        longestSub = 0
        prevChars = {}

        while right < len(s):
            while s[right] in prevChars:
                prevChars.pop(s[left])
                left+=1
            
            prevChars[s[right]] = 1
            right+=1
            longestSub = max(longestSub, len(prevChars))

        return longestSub
        