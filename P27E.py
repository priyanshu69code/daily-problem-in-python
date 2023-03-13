class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    lenA = getLength(headA)
    lenB = getLength(headB)
    diff = abs(lenA - lenB)

    # Traverse the longer linked list by the difference in length
    if lenA > lenB:
        while diff:
            headA = headA.next
            diff -= 1
    else:
        while diff:
            headB = headB.next
            diff -= 1

    # Traverse both linked lists simultaneously
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None

def getLength(head: ListNode) -> int:
    length = 0
    while head:
        length += 1
        head = head.next
    return length
