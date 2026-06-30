class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        understand:
        input: gets a string (may or may not be a plaindrome)
        output: boolean representing if pal or not

        ignores all nonalphanumeric chars!
            spaces, punctuation, and symbols

        case sensitive: W != w

        lenght is between 1 to 1000

        match:
            two pointers method - right pointer and left pointer

        plan:
            1. make a left pointer set to 0 and right pointer set to len(s)-1
            2.
!!!heyyeh

            tab a cat

            while right > left:
                while not s[left].isalnum() and right > left:
                    left +=1
                while not s[right].isalnum() and left < right:
                    right-=1

                if s[left].lower() != s[right].lower():
                    return False

                right-=1
                left+=1

            return True
        '''


        left = 0
        right = len(s)-1

        while right > left:
            while not s[left].isalnum() and right > left:
                left+=1
            while not s[right].isalnum() and left < right:
                right-=1

            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1
        return True