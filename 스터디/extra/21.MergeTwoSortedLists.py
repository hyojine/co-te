# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        cur=list3
        while list1 or list2:
            if list1 and list2:
                if list1.val<=list2.val:
                    cur.next=ListNode(list1.val)
                    list1=list1.next
                else:
                    cur.next=ListNode(list2.val)
                    list2=list2.next
            elif not list1:
                cur.next=ListNode(list2.val)
                list2=list2.next
            elif not list2:
                cur.next=ListNode(list1.val)
                list1=list1.next
            cur=cur.next
        return list3.next