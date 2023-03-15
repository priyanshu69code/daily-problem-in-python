def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]
