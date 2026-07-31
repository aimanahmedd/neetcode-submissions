class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        understand:
        anagram - string w same chars as prev string (order of chars can be diff)

        racecar == carrace
        -> all same characters! true

        jar != jam
        -> not all the same characters! false:(

        input: two string words
        output: boolean depending on whether they are anagrams of one another

        match:
            use a hashmap to keep track of all the characters that appear
            and how many times they appear

        plan:
            1. check if length equals to one another, if not return false
            2. make a hashmap to store s chars and hashmap to store t chars
            3. go through string s
                a. if char in s hash +1
                b. if not add to hash
            4. go through string t
                a. if char in t hash +1
                b. if not add to hash
            5. go through s hash
                check if char is in t hash
                    if so check if they appear the same amount of times
                        if not return false
        '''

        if len(s) != len(t):
            return False
        
        sHash = {}
        tHash = {}

        for char in s:
            if char in sHash:
                sHash[char] +=1
            else:
                sHash[char] = 1

        for char in t:
            if char in tHash:
                tHash[char] +=1 
            else:
                tHash[char] = 1
        
#check how to just access values in hashmaps
        for key in sHash:
            if key not in tHash:
                return False
            else:
                if sHash[key] != tHash[key]:
                    return False
        return True

        