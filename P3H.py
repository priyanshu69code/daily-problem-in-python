class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def short(list):
    while

def mergeTwoLists(self, list1, list2):
    trv = list1
    while trv.next != None:
        trv = trv.next
    trv.next = list2


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

