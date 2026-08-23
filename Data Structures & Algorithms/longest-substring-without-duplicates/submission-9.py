class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        understand:
        input: string s with a series of characters
        output: longest length without any duplicates

        "zxyzxyz"
        -> output: 3 
        everytime we find a duplicate, we move the newest longest duplicate down

        "xxxx"
        -> 1

        case where we dont have an answer (empty string)

        ASCII character

        match:
        sliding window, because keep track of future to find no duplicates

        plan:
        1. make left and right pointer, both point to 0 (first element in string)
        2. O(1) hashmap to keep track of all prev characters we have
        3. make a variable to keep track of longest length
        4. while right < len(s):
            while s[right] in hashmap:
                hashmap.pop(s[left])
                left+=1


            hashmap[s[right]] = 1
            longestLength = max(longestLength, len(hashmap))
            right+=1

"a b c d "
{ b: 1, "": 1}
longestLength = 3
        '''
        left, right = 0, 0
        prevChars = {}
        longestLength = 0

        while right < len(s):
            while s[right] in prevChars:
                prevChars.pop(s[left])
                left+=1
            
            prevChars[s[right]] = 1
            longestLength = max(longestLength, len(prevChars))
            right+=1
        return longestLength


        