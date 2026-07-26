# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        understand:
        input: SLL
        output: reverse SLL

        1 -> 2 -> 3 -> 4
        4 -> 3 -> 2 -> 1

        match:
            two pointers switch what each node points to

        plan:
        1. make a prev pointer (null) and a current pointer (keep track what it points 
        to) (head)
        2. while current does not equal to null:
            tmp = current.next
            current.next = prev

            prev = current
            current = tmp
        3. return prev
        '''
        previous = None
        current = head

        while current != None:
            tmp = current.next
            current.next = previous

            previous = current
            current = tmp
        return previous