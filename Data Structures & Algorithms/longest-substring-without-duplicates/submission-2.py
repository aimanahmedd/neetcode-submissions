class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 #points to the first letter in string s
        prevChars = set() #set of all the previous letters we have encountered
        longest = 0 #the longest substring length

        for right in range(len(s)):
            while s[right] in prevChars: #while the duplicate character is in the window,
            # we shrink the window until no more duplicates!!!!
                prevChars.remove(s[left])
                left+=1
            prevChars.add(s[right])
            longest = max(longest, right-left+1)

        return longest
        '''
        {p }
        longest = 2





        zxyzxyz
         L
        R R R

        { x y z}


        left = 0
        mapPrevChars = set()
        longest = 0

        for right in range(len(s)):
            if s[right] in mapPrevChars:
                mapPrevChars.remove(s[right])
                left+=1
            map.add(s[right])
            longest = max(longest, right-left+1)
        return longest
        '''
