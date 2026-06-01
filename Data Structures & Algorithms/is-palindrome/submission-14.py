class Solution:
    def isPalindrome(self, s: str) -> bool:
        # '''
        # two pointer left and right
        left = 0
        right = len(s) - 1
        # if character is not an alphanum, skip to the next character
        while right > left:
            while not s[right].isalnum() and right > left:
                right-=1
            while not s[left].isalnum() and right > left:
                left+=1
            
            if s[right].lower() == s[left].lower():
                right-=1
                left+=1
            else:
                return False
        # if both current characters match, move both inwards
        # else return false
        # return true at the end (meaning we did not find anything bad)
        return True

        #No lemon, no melon
        # "Was it a car or a cat I saw?"


        # '''