


class Queue: 

    def __init__(self) -> None:
        self._items = [] 

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()
    
    def size(self):
        return len(self._items)
    
    def is_empty(self):
        return not bool(self._items)
    
    def __str__(self) -> str:
        return str(self._items)
    


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.size())
    q.enqueue(4)
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q)