class Solution:
    '''
    understand:
    the first function takes in a list of strings and basically encodes it:
    ["hello", "world"] -> 5#hello5#world

    plan: no data structure yet
    1. variable with empty string
    2. for word in strings
        2a. length(word) + # + word to the empty string
    3. return newly created string


    decode:
    takes in encoded string and returns original array


    plan:
    1. have empty array to put words
    2. have an i counter. i = 0 as of right now
    3. for i in range(len(s)):
        3a. if s[i] == number:
            3b. i = i + 2
            3c. while i 


    '''
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        original_message = []
        i = 0
        digit = ''

        while i < len(s):
            if s[i] != "#":
                digit += s[i]
                i = i + 1
            else:
                length = int(digit)
                original_message.append(s[i+1:i+ length +1])
                digit = ''
                i = i + length + 1
        return original_message

