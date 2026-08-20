class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        understand:
        input: sequence of characters
        output: length of longest substring

        "zxyzxyz"
        -> 3 xyz is longest substring

        "xxxx"
        -> 1 because x is longest substring

        O(n) time complexity
        may be a case with 0 characters

        match:
            sliding window to keep track of longest substring

        plan:
        1. left and right pointer, left equal to zero right equal to zero
        2. substring = set longestsub = 0
        3. while right < len(s):
            while s[right] in substring:
                substring.remove(s[left])
                left+=1
            
            substring.add(s[right])
            longestsub = max(longestsub, len(substring))
            right+=1

        '''

        left, right = 0, 0
        subString = set()
        longestSub = 0

        while right < len(s):
            while s[right] in subString:
                subString.remove(s[left])
                left+=1
            
            subString.add(s[right])
            longestSub = max(longestSub, len(subString))
            right+=1
        return longestSub