class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        understand:
        input: string s of uppercase chars and integer k
        output: longest substring with 1 distinve character

        "XYYX" k=2
        -> 4 (all become Y)

        "AAABABB" we can only change 1 char!
        -> 5 after changing B to A

        never an empty string, but cases where we can make 0 changes

        all UPPER CASE Characters

        100k

        match:
            sliding window to keep track of longest substring

        plan:
        1. make a left and right pointer pointing to first element in string
        2. first do for loop to find the most amount of characters in the string
        and store in hashmap each character count
        3. get the highest letter
        4. for loop through s, k amount of times and change the different character to be the highest caracter
        5. sliding window and find the longest substring
        '''
        left, right = 0, 0
        charCount = {}
        maxFreq = 0
        longestSub = 0

        while right < len(s):
            #first figure out how many replacement we need
            if s[right] in charCount:
                charCount[s[right]]+=1
                maxFreq = max(maxFreq, charCount[s[right]])
            else:
                charCount[s[right]] = 1
                maxFreq = max(maxFreq, charCount[s[right]])

            windowSize = right-left + 1
            replacements = windowSize - maxFreq

            if replacements > k:
                charCount[s[left]] -=1
                left+=1

            longestSub = max(longestSub, right-left+1)
            right+=1
        return longestSub
                





        
        