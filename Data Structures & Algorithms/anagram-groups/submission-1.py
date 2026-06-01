class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Hashmap:
        key sorted word: value list of the word
        act: [act, cat]

        '''
        hashed = defaultdict(list) #value as a list
        for word in strs:
            charArray = [0]*26
            for char in word:
                charArray[ord(char)-ord("a")] +=1
            hashed[tuple(charArray)].append(word) #frequency of chars as key
        return list(hashed.values()) 