
class Stack: 

    def __init__(self) -> None:
        self._list = []

    def is_empty(self):
        if len(self._list) == 0:
            return True
        return False 
    
    def push(self, item):
        self._list.append(item)

    def peek(self):
        return self._list[-1]
    
    def pop(self):
        return self._list.pop()
    
    def size(self):
        return len(self._list)

    def __str__(self):
        res = ""
        # if self.is_empty:
        #     res = "[]"
        if not self.is_empty():
            res += f"[{self._list[0]}]"

        for i in self._list[1:]:
            res += f"<-[{i}]"
        return res


# Test: 
# s = Stack()
# print(s.is_empty()) #true
# print(s.push(4))    #none
# print(s.push('7')) 
# print(s.push('8'))
# print(s)
# print(s.pop())
# print(s)