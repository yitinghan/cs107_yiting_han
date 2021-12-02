from math import floor
from typing import List


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        peek = idx
        l = self.left(idx)
        r = self.right(idx)

        if l < self.size and self.compare(self.elements[l], self.elements[peek]):
            peek = l

        if r < self.size and self.compare(self.elements[r], self.elements[peek]):
            peek = r
        
        if peek != idx:
            self.swap(peek, idx)
            self.heapify(peek)
        
    def build_heap(self) -> None:
        # bottom to top
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1
        self.heapify(self.parent(self.size - 1))


    def heappop(self) -> int:
        if len(self.elements) == 0:
            raise IndexError("The heap is empty!")
        peek = self.elements[0]
        self.elements[0] = self.elements[self.size - 1]
        self.heapify(0)
        self.size -= 1
        return peek

class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a < b:
            return True
        else:
            return False
    

class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a > b:
            return True
        else:
            return False
    


h = MinHeap([-1,-3,-5,15,23,1,2,3]) # The heap tree will be built during initialization
print(h)


# h.heappush(2)
# print(h)

# print(h.heappop())
# print(h)


h = MaxHeap([-1,-3,-5,15,23,1,2,3]) # The heap tree will be built during initialization
print(h)