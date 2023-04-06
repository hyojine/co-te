# https://leetcode.com/problems/reverse-linked-list/

class Solution:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        
        new=ListNode()
        cur=new
        while vals:
            cur.next=ListNode(vals.pop())
            cur=cur.next
        return new.next