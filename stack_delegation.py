class Stack:
    def __init__(self):
        # Stack hat eine Liste (keine Vererbung)
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)
