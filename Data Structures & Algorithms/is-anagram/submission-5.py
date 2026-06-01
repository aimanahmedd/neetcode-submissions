class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        understand:
        input: string s and string t
        output: boolean
        return true if the two strings are anagrams of each other

        all lowercase letters
        just letters no additional characters
        no empty strings
        are they all the same length as well

        match: hashmap to keep track of letter frequency

        plan:
        i want to go through each string and basically count the letter frequency
        of each character. i then want to compare the hashmaps and see if they match
        if there are any differences return false

        1. make a hashmap for s and make a hashmap for t
        2. go through string s and store frequency in s hashmap
        3. go through string t and store frequence in t hashmap
        4. choose a hashmap (maybe s hashmap) loop through and check matching
        
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

        for key in sHash:
            if key not in tHash:
                return False
            elif sHash[key] != tHash[key]:
                return False
        return True
        