class Stack(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self) == 0

    def size(self):
        return len(self)
