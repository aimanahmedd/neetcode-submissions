class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        understand:
        input: string s which is a phrase
        output: boolean depending if palindrome or not

        "tab a cat"
        -> false because does not return the same thing backwards

        1 char can be considered a palindrom
        ignore all non alphanum

        match:
        two pointers: we can chack equalness front and back

        plan:
        1. pointer for left and right, left = first index right = last index
        2. while right > left:
            while right > left and not s[right].isalnum():
                right-=1
            while right > left and not s[left].isalnum():
                left+=1

            if s[right].lower() != s[left].lower():
                return False

            left+=1
            right-=1
        3. return True
        '''
        left, right = 0, len(s)-1

        while right > left:
            while right > left and not s[right].isalnum():
                right-=1
            while right > left and not s[left].isalnum():
                left+=1
            
            if s[left].lower() != s[right].lower():
                return False

            left+=1
            right-=1
        return True
        