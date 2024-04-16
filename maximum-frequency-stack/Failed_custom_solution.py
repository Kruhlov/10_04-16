class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class FreqStack:

    def __init__(self):
        self.head=None

    def push(self, val: int) -> None:
        if self.head is None:
            self.head=Node(val)
        else:
            node=Node(val)
            node.next=self.head
            self.head=node

    def search_count(self,val):
        count=0
        i=self.head
        while i is not None:
            if i.value==val:
                count+=1
            i=i.next
        return count

    def pop(self) -> int:
        if self.head:
            val=self.head.value
            i=self.head.next
            num=self.search_count(val)
            while i is not None:
                cou=self.search_count(i.value)
                if num<cou:
                    num=cou
                    val=i.value
                i=i.next
            if self.head.value==val:
                self.head=self.head.next
            else:
                j=self.head
                while j.next.value!=val:
                    j=j.next
                j.next=j.next.next
            return val
        return None
