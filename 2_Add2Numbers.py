# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        current = head
        carry = 0
        while l1 is not None or l2 is not None or carry!=0:
            digit1 = l1.val if l1 else 0 
            digit2 = l2.val if l2 else 0 

            res_sum = digit1 + digit2 + carry 
            current.next = ListNode(res_sum % 10)
            carry = res_sum // 10 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next 
        return head.next 
