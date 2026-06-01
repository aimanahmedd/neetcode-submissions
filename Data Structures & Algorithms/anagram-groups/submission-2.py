class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        understand:
        input: list of strings
        output: list of list of strings

        all lowercase and can be samr word and empy string

        plan:
        1. creating a defaultdict(list) so i can group each word based off
        alphabetically and there is no error with putting an element in the lists
        2. go through a for loop for each word:
            2a. in the for loop create a new array (which will act as the key) 
            that keeps track the frequency of letters
            2b. go inside the word (for loop), to get place in new array subtract
            unicode of character with unicode of a and add 1
            2c. insert into hashmap (the tupled version)
        3. return list of values from hashmap
        '''
        groupAnagrams = defaultdict(list)

        for word in strs: 
            charArrayForWord = [0] * 26 
            for char in word:
                charArrayForWord[ord(char) - ord("a")] = charArrayForWord[ord(char) - ord("a")] + 1
            groupAnagrams[tuple(charArrayForWord)].append(word) 
        
        return list(groupAnagrams.values())