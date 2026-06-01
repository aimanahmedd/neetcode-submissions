"""
okay my plan:
    - check if lengths of both words are same, if not automatically reutn false
    -create hashmap of word s and word t, and track each letter and see how many
    times the letter appears in the word
    - check word s hashmap and check if the letter appears in the t hashmap AND same amount
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_word_hashmap = {}
        t_word_hashmap = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in s_word_hashmap:
                s_word_hashmap[char] = s_word_hashmap[char]+1
            else:
                s_word_hashmap[char] = 1
        
        for char in t:
            if char in t_word_hashmap:
                t_word_hashmap[char] = t_word_hashmap[char]+1
            else:
                t_word_hashmap[char] = 1
        
        for key in s_word_hashmap:
            if key not in t_word_hashmap or t_word_hashmap[key] > s_word_hashmap[key]:
                return False
        for key in t_word_hashmap:
            if key not in s_word_hashmap or s_word_hashmap[key] > t_word_hashmap[key]:
                return False
        return True
        