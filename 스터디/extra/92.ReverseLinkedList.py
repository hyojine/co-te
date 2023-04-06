# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head # 애초에 헤드에 값이 있음
        
        cnt=left-1
        new=ListNode()
        cur=new
        while cnt and head:
            cur.next=head
            cur=cur.next
            head=head.next
            cnt-=1
        
        rev=[]
        cnt=right-left+1
        while cnt and head:
            rev.append(head.val)
            head=head.next
            cnt-=1
        while rev:
            cur.next=ListNode(rev.pop())
            cur=cur.next
        while head:
            cur.next=head
            cur=cur.next
            head=head.next
        return new.next