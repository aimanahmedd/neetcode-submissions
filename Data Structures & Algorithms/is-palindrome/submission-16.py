class Solution:
    def isPalindrome(self, s: str) -> bool:
        # '''
        # have a lefr and right pointer
        left = 0
        right = len(s)-1
        # while the right is greater than the left
        # while the left pointer is not an alphanum char, keep moving it up
        # while the right pointer is not an alphanum char, keep moving it down

        #s="Was it a car or a cat I saw?"

        while right > left:
            while not s[left].isalnum() and right > left:
                left+=1
            while not s[right].isalnum() and right > left:
                right-=1
            
            if s[right].lower() != s[left].lower():
                return False
            else:
                left+=1
                right-=1
        return True


        # check if they are the same
        # if they are not return false
        # else move pointers


        # '''
        