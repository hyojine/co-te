# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=new=ListNode()
        cur.next=head
        cur=cur.next
        if head:
            head=head.next
        while head:
            if cur.val==head.val:
                head=head.next
            else:
                cur.next=head
                cur=cur.next
                head=head.next
        if cur:
            cur.next=None
        return new.next