class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1) Walk the list, collect values
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        # 2) Check if the list of values is the same forwards and backwards
        return vals == vals[::-1] # ab yeh start stop wala fundey ko agr khali chhod dega to yeh ek reverse loop ki trah kaam karega