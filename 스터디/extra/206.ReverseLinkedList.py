# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        
        new=ListNode()
        while vals:
            new.next=ListNode(vals.pop())
            new=new.next
        return new.next