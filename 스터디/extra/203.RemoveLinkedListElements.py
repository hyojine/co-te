# https://leetcode.com/problems/remove-linked-list-elements/description/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new=ListNode() # val=0
        cur=new
        while head:
            if head.val==val:
                head=head.next
            else:
                cur.next=head
                cur=cur.next
                head=head.next
        if cur.next and cur.next.val==val:
            cur.next=None
                
        return new.next
