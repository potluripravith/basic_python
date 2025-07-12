class Stack:
    def __init__(self):
        self._items = [] #internal storage using list
        
    def push(self,item):
        self._items.append(item)
        
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()   
    
    