class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    # Initialize pointers
    prev = None
    curr = head

    # Traverse the list, updating pointers
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Return the new head
    return prev
