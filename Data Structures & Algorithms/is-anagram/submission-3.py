class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        allWords = {}

        sWord = sorted(s)

        allWords[tuple(sWord)] = 1

        tWord = sorted(t)

        if(tuple(tWord) in allWords):
            return True
        else:
            return False
        