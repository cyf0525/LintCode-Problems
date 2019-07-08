"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        if head == None:
            return None
        slow = head
        fast = head.next
        while fast != None:
            fast = fast.next
            if fast != None:
                slow = slow.next
                fast = fast.next
        return slow