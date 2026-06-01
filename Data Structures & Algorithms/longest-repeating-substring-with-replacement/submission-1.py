class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countSet = {} #a set to track how many times the character appears
        left = 0 #left pointer
        answer = 0

        for right in range(len(s)): #right pointer to go through the string
            countSet[s[right]] = 1 + countSet.get(s[right], 0) #incrementing the count for a charcter,
            #and adding one if there is nothing there as of yet
            while (right-left + 1) - max(countSet.values()) > k: #while the num of replacements of the window is invalid
                countSet[s[left]] -=1 #decrease the char count
                left+=1 #increase left pointer
            answer = max(answer, right-left+1)
        return answer
        

'''
so basically what i did was i started out by creating a hashmap, just to track how
many times a character came up. the reason we tracked character counts was to check
if the window was valid- so we could see basically if the num replacements is in
fact less than what we need. I then created a left and right pointer. with our right
pointer, i add it to the charcount set, and then i checked if the window we were on 
was valid. i did this by doing the length - max and if it wasnt, id increase the
left pointer and subtract one from that freq. after that i basically just calculated
what the max answer was, and just returned it after the loop was finished!:)
'''