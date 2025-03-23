class ListNode:
  def __init__(self, data):
        self.data = data
        self.next = None
class addLinked:
    def addTwoNums(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        curr = dummy
        
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_total = val1 + val2 + carry
            carry = val_total // 10
            curr.next = ListNode(val=val_total % 10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next  
