class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # Step 1: Append the new value to the end of the heap
        self.heap.append(value)
        current_index = len(self.heap) - 1

        # Step 2: Heapify up
        while current_index > 0:
            parent_index = self._parent(current_index)
            if self.heap[parent_index] < self.heap[current_index]:
                self._swap(parent_index, current_index)
                current_index = parent_index
            else:
                break


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)

myheap.insert(100)

print(myheap.heap)

myheap.insert(75)

print(myheap.heap)
