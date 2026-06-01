"""
okay my plan:
    - check if lengths of both words are same, if not automatically reutn false
    -create hashmap of word s and word t, and track each letter and see how many
    times the letter appears in the word
    - check word s hashmap and check if the letter appears in the t hashmap AND same amount
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterOfS = {}
        letterOfT = {}

        for i in range(0, len(s)):
            if s[i] in letterOfS:
                letterOfS[s[i]] = letterOfS[s[i]] + 1
            else:
                letterOfS[s[i]] = 1
        
        for i in range(0, len(t)):
            if t[i] in letterOfT:
                letterOfT[t[i]] = letterOfT[t[i]] + 1
            else:
                letterOfT[t[i]] = 1

        for key in letterOfS:
            if key not in letterOfT or letterOfS[key] != letterOfT[key]:
                return False
        return True