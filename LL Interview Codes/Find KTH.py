class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
            else:
                values.add(current.value)
                previous = current
            current = current.next

def find_kth_from_end(linked_list, k):
    slow = linked_list.head
    fast = linked_list.head

    for _ in range(k):
        if fast is None:
            return None  # k is larger than the length of the linked list
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
result = find_kth_from_end(my_linked_list, k)

if result:
    print(result.value)  # Output: 4
else:
    print("The linked list is shorter than k elements.")
