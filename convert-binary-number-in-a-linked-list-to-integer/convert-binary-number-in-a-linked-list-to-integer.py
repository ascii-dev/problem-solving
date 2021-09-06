# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bit_string = "0"
        current_node = head
        
        while current_node is not None:
            bit_string += str(current_node.val)
            current_node = current_node.next
        
        return int(bit_string, base=2)
