# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd (a,b):
            while b>0:
                a,b=b,a%b
            return a
        
        cur=head
        while cur.next: #making sure it doesnt run on the last node
            n1, n2=cur.val, cur.next.val
            cur.next= ListNode(gcd(n1, n2), cur.next) #adding the node
            cur=cur.next.next #moving the pointer for next run
        return head
