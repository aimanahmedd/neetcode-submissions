class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        understand:
        input: string phrase
        outuput: output boolean representing palindrome or not

        palindrome: reads the same front and back
        -> case sensitive
        -> ignores nonalphanum (. , ! ? etc.)
        
        string length: 1 <= s.length <= 1000
        string can be all the same characters front and back or even one letter

        match:
            two pointers to keep track from both ends and see if both ends are the
            same

        plan:
        1. left and right pointer, left first index in string right is last index in
        string
        2. while right > left:
            while right > left and not s[right].alnum():
                right-=1
            while right > left and not s[left].alnum():
                left+=1

            if s[right].lower() != s[left].lower():
                return False

        3. return True

        '''
        left, right = 0, len(s)-1

        while right > left:
            while right > left and not s[right].isalnum():
                right-=1
            while right > left and not s[left].isalnum():
                left+=1

            if s[right].lower()!= s[left].lower():
                return False

            left+=1
            right-=1
            
        return True