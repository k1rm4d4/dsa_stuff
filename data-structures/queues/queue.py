

class Queue:
    def __init__(self) -> None:
        self._items = []

    
    def is_empty(self):
        return self._items == [] 
    

    def enqueue(self, item):
        self._items.append(item)
    

    def dequeue(self):
        if not self.is_empty():
            return self._items.pop(0)
    

    def size(self):
        return len(self._items)


    def __str__(self) -> str:
        q = ""
        index = 0
        while index < len(self._items):
            q += f"{self._items[index]}->"
            index += 1
        return q


# if __name__ == "__main__":
#     q = Queue()
#     print(q.is_empty())
#     q.enqueue(1)
#     q.enqueue(2)
#     q.enqueue(3)
#     print(q.size())
#     q.enqueue(4)
#     print(q)
#     print(q.dequeue())
#     print(q.dequeue())
#     print(q)