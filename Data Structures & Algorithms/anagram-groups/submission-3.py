class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            understand:
            input: list of strings 
            output: array of arrays with grouped anagrams

            [act, pot, cat, top]

            [[act, cat], [pot, top]]

            match:
                using an array

            plan:
            1. create a defaultdict(list) so you can easily access index

            2. go through for loop for each other
                a. create a new array to act as key with placeholders of
                how many times each letter appeared in the array
                b. go through each char in word and subtract unicode wih unicode of a and add to new array
            3. insert to hashmap
            4. return list of hashvalues
        '''

        groupedAnagrams = defaultdict(list)

        for word in strs:
            newArray = [0] * 26

            for char in word:
                newArray[ord(char) - ord("a")] = newArray[ord(char) - ord("a")] +1
            groupedAnagrams[tuple(newArray)].append(word)
        return list(groupedAnagrams.values())
        