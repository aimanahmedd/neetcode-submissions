class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        understand:
        input: string s
        output: boolean representing palindrome or not

        "tab a cat"
        return false -> you can't flip and it be the same

        match:
            two pointers check both ends to make sure same

        plan:
        1. make a left and right pointer, left = 0 (first index) while right
        = len(s) -1 (end index)
        2. while right > left:
            while !right.isalnum():
                right -=1
            while !left.islanum():
                left+=1
            
            if s[right] != s[left]:
                return False
        3. return True
        '''
        left, right = 0, len(s)-1

        while right > left:
            while not s[right].isalnum() and right > left:
                right-=1
            while not s[left].isalnum() and right > left:
                left+=1
            
            if s[right].lower() != s[left].lower():
                return False
            
            right-=1
            left+=1
        return True
        