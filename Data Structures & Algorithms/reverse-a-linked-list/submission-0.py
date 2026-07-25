# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        match: two pointers method (have one pointer set to prev and one to current)

        plan:
        reverse this list to make the current pointer point to its previous
        and return the new head of this list (aka last node)

        1. make a prev pointer (null) and a current pointer which is node head

        2. while curr does not equal to null
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp
        3. return prev
        '''

        prev = None
        curr = head

        while curr != None:
            tmp = curr.next
            curr.next = prev #we want the current val to point to prev
            #we set it to none because it is a sll so we dont want the next to 
            #still be there
            prev = curr
            curr = tmp
        return prev


        [1, 2, 3, 4]
