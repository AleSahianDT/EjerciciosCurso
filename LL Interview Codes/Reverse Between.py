def reverse_between(self, m, n):
    if not self.head:
        return None

    dummy = Node(0)
    dummy.next = self.head
    prev = dummy

    for i in range(m):
        prev = prev.next

    current = prev.next
    for i in range(n - m):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    self.head = dummy.next