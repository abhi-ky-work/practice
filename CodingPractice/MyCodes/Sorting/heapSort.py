

arr = [30, 63, 10, 12, 20, 45, 50, 60, 40, 99]
HEAPSIZE = 8


class Heap:

    def __init__(self):
        self.heap_size = 0
        self.heap = [0]*HEAPSIZE

    def insert(self, data, show_fixing):

        if self.heap_size == HEAPSIZE:
            return "Heap is full"

        else:
            self.heap[self.heap_size] = data
            self.heap_size += 1

        self.fix_up(self.heap_size - 1, show_fixing)
        if show_fixing:
                print("============FinalHeap after Insert==============", self.heap)
                self.print_heap()
                print("============FinalHeap Ends======================")

    def fix_up(self, node_index, show_fixing):

        parent_index = (node_index - 1)//2

        if node_index > 0 and self.heap[node_index] > self.heap[parent_index]:
            self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
            self.fix_up(parent_index,show_fixing)

        if show_fixing:
            print("Heach change after a fix_up")
            self.print_heap()

    def get_max(self):
        return self.heap[0]

    def pop(self, show_fixing):
        if self.heap_size > 0:
            max_item = self.get_max()
            self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
            self.fix_down(0, show_fixing)
            self.heap_size -= 1
            if show_fixing:
                print("============FinalHeap after pop{}==============".format(self.get_max()), self.heap)
                self.print_heap()
                print("============FinalHeap Ends=================")
            return max_item
        else:
            return "Heap is empty"

    def fix_down(self, node_index, show_fixing):
        left_child_index = 2*node_index + 1
        right_child_index = 2*node_index + 2

        larger_index = node_index

        if left_child_index < self.heap_size and self.heap[left_child_index] > self.heap[node_index]:
            larger_index = left_child_index
        if right_child_index < self.heap_size and self.heap[right_child_index] > self.heap[node_index]:
            larger_index = right_child_index

        if node_index != larger_index:
            self.heap[larger_index], self.heap[node_index] = self.heap[node_index], self.heap[larger_index]
            self.fix_down(larger_index,show_fixing)
        
        if show_fixing:
            print("Heach change after a fix_down")
            self.print_heap()

    def print_heap(self):
        nodes = [0]
        while len(nodes) > 0:
            j = nodes.pop(0)
            if j <= (self.heap_size - 1)//2:
                left_node = "X"
                right_node = "X"
                if (2*j)+1 < self.heap_size:
                    left_node = self.heap[(j*2)+1]
                if (2*j)+2 < self.heap_size:
                    right_node = self.heap[(j*2)+2]

                print("      ", self.heap[j])
                print("   ----------")
                print("   |        |  ")
                print("   {}        {}".format(left_node, right_node))
                if (2*j)+1 < self.heap_size:
                    nodes.append((2*j)+1)
                if (2*j)+2 < self.heap_size:
                    nodes.append((2*j)+2)



print("Do you want to see heap fix steps ?")
show_fix = bool(int(input()))
print("Showing Fixing : ", show_fix)
print("Enter Heap Size")
heapsize = int(input())
HEAPSIZE = heapsize

heap = Heap()

for i in range(heapsize):
    print("Enter Item : {}".format(i+1))
    if show_fix:
        heap.insert(int(input()),True)
    else:
        heap.insert(int(input()),False)


print("========================POP=========================")
heap.pop(True)

# heap = Heap()

# for i in arr:
#     heap.insert(i,False)

# print("Final Heap : (length {}) ".format(heap.heap_size), heap.heap)
# heap.print_heap()

# print("MAX OF HEAP", heap.get_max())

# print("head after one pop : ", heap.heap)
# heap.pop(True)
# print("Size of heap after removal : ", heap.heap_size)

# heap.print_heap()