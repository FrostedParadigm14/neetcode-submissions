# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_next = None
        while head != None:
            temp = head.next
            head.next = new_next
            new_next = head
            head = temp

        return new_next
        


'''
 3 -> 4 -> 5 -> 6
 flip the pointers in place
 new_next = null

until empty
 next_node -> curr.next (4)
 curr.next -> null // new_next
 new_next -> curr (3)
 curr -> next_node


'''
        