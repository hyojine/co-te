# https://leetcode.com/problems/add-two-numbers/submissions/924551966/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l3=ListNode()
        cur=l3
        plus=0
        while l1 or l2:
            if l1==None:
                sumoftwo=l2.val+plus
                l2=l2.next
            elif l2==None:
                sumoftwo=l1.val+plus
                l1=l1.next
            else:
                sumoftwo=l1.val+l2.val+plus
                l1=l1.next
                l2=l2.next
            if sumoftwo>=10:
                plus=sumoftwo//10
            else:
                plus=0
            sumoftwo%=10
            cur.next=ListNode(sumoftwo)
            cur=cur.next
        if plus:
            cur.next=ListNode(plus)
        return l3.next
        