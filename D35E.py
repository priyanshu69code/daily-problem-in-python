class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int) -> ListNode:
    # Skip any leading nodes with value val
    while head and head.val == val:
        head = head.next

    # Remove any remaining nodes with value val
    curr = head
    prev = None
    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head
