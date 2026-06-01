class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sWordHash = {}
        tWordHash = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in sWordHash:
                sWordHash[char] +=1
            else:
                sWordHash[char] = 1
        
        for char in t:
            if char in tWordHash:
                tWordHash[char] +=1
            else:
                tWordHash[char] = 1

        for key in sWordHash:
            if key not in tWordHash or sWordHash[key] != tWordHash[key]:
                return False
        for key in tWordHash:
            if key not in sWordHash or sWordHash[key] != tWordHash[key]:
                return False
        return True
