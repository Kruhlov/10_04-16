class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
    def push(self,val):
        if self.head:
            n=Node(val)
            n.next=self.head
            self.head=n
        else:
            self.head=Node(val)
    def pop(self):
        if self.head:
            n=self.head
            self.head=n.next
            return n.value

class MyQueue:

    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack1.head is None:
            return None
        while self.stack1.head is not None:
            self.stack2.push(self.stack1.pop())
        val=self.stack2.pop()
        while self.stack2.head is not None:
            self.stack1.push(self.stack2.pop())
        return val

    def peek(self) -> int:
        if self.stack1.head is None:
            return None
        while self.stack1.head is not None:
            self.stack2.push(self.stack1.pop())
        val=self.stack2.head.value
        while self.stack2.head is not None:
            self.stack1.push(self.stack2.pop())
        return val

    def empty(self) -> bool:
        return self.stack1.head is None
