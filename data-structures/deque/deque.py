class Deque:

    def __init__(self) -> None:
        self._items = []

    def is_empty(self):
        return not self._items
    
    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self): 
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)
    
    def size(self):
        return len(self._items)
    
    def __repr__(self) -> str:
        return str(self._items) 
    

if __name__ == "__main__":
    d = Deque()
    d.add_front("a")
    d.add_rear("1")
    d.add_front("b")
    print(d)
    print(d.remove_front())
    print(d)
    print(d.remove_rear())
    print(d)