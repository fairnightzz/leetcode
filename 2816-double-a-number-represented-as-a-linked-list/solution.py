# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number = []
        while head:
            number.append(head.val)
            head = head.next
        
        number = number[::-1]
        ans = None
        carry = 0
        for num in number:
            doubled = num*2 + carry
            node = ListNode(doubled%10, ans)
            carry = doubled // 10
            ans = node
        if carry == 1:
            node = ListNode(1, ans)
            ans = node

        return ans


        