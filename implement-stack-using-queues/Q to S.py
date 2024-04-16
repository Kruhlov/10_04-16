class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def push(self,val):
        if self.front is None:
            self.front=Node(val)
            self.rear=self.front
        else:
            n=Node(val)
            self.rear.next=n
            self.rear=n
    def pop(self):
        if self.front is not None:
            val=self.front.value
            self.front=self.front.next
            return val
        return None
class MyStack:

    def __init__(self):
        self.queue1=Queue()
        self.queue2=Queue()        

    def push(self, x: int) -> None:
        self.queue1.push(x)

    def pop(self) -> int:
        if self.queue1.front is None:
            return None
        while self.queue1.rear!=self.queue1.front:
            self.queue2.push(self.queue1.pop())
        val=self.queue1.pop()
        while self.queue2.front is not None:
            self.queue1.push(self.queue2.pop())
        return val
        

    def top(self) -> int:
        if self.queue1.front is None:
            return None
        while self.queue1.rear!=self.queue1.front:
            self.queue2.push(self.queue1.pop())
        val=self.queue1.front.value
        self.queue2.push(self.queue1.pop())
        while self.queue2.front is not None:
            self.queue1.push(self.queue2.pop())
        return val

    def empty(self) -> bool:
        return self.queue1.front is None
