class Stack:

    class _Node:
        def __init__(self):
            self.item = None
            self.next = None

    def __init__(self):
        self._front = None
        self._size  = 0

    #//push
    def push(self,item):
        old_front = self._front
        self._front = self._Node()
        self._front.item = item
        self._front.next = old_front
        self._size += 1

    #//pop
    def pop(self):
        if self.isempty() : raise Exception("Stack Overflow")
        item = self._front.item
        self._front = self._front.next
        self._size -= 1
        return item


    #//empty
    def isempty(self):
        if self._size == 0 :
            return True
        else:
            return False

    #//size
    def size(self):
        return self._size

stack = Stack()
stack.push(10)
stack.push(120)
print(stack.pop())