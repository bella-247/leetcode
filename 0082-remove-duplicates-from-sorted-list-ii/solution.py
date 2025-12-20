# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup_val = None
        dummy = ListNode(0, head)
        itr = dummy
        
        while itr:
            if itr.next:
                if itr.next.next:
                    if itr.next.val == itr.next.next.val:
                        dup_val = itr.next.val
                        if itr.next == head: # checks if the node i am removing is the head node and if true it replaces the head pointer to the next one
                            head = itr.next.next
                        itr.next = itr.next.next
                        continue

                if itr.next.val == dup_val:
                    if itr.next == head: # checks if the node i am removing is the head node and if true it replaces the head pointer to the next one
                        head = itr.next.next
                    itr.next = itr.next.next
                    continue
                    
                
            itr = itr.next
            
        return head

