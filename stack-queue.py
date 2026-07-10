class ArrayStack:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)

    def top(self):

        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]
    
    def peop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()
    

def is_matched(expr):
    lefty='({['
    righty=']})'

    S=ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

expr='[(5+x)-(y+z)]'

print(is_matched(expr))