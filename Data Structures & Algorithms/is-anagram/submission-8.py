class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        understand:
        input: two string words
        output: boolean to represent 

        match: 
            use hashmap to store the count for each letter and make
            sure it matches the other


        plan:
        1. create empty hashmap for word s
        2. loop through word s, storing the the count for each letter
        3. loop through t but checking against hashmap for s
            3a. if any mismatches return false right away
        4. return true

        '''

        s_count = {}

        t_count = {}

        for char in s:
            if char not in t:
                return False
            else:
                if char in s_count:
                    s_count[char] += 1
                else:
                    s_count[char] = 1
        
        # {r: 2, a: 2, c: 2, e:1}

        for char in t:
            if char not in s:
                return False
            else:
                if char in t_count:
                    t_count[char] += 1
                else:
                    t_count[char] = 1

        
        for key in s_count:
            if s_count[key] != t_count[key]:
                return False
        return True
        