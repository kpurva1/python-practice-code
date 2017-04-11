#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode (0)
        curr = l3
        carry = 0
        x = 0
        y = 0
        sum = 0
        while l1 or l2:
            if (l1):
                x= l1.val
            else:
                x = 0
            if (l2):
                y =l2.val
            else:
                y = 0
            
            sum = x+y+carry
            carry = sum/10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if (l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
        if (carry > 0):
            curr.next = ListNode(carry)
        return l3.next
