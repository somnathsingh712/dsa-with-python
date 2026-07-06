class Empty(Exception):
    pass
class arraystack:
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
                raise Empty("Stack is Empty")
            return self.data[-1]
        
        def pop(self):
            if self.is_empty():
                raise Empty("Stack is Empty")
            return self._data.pop()


jack=arraystack()
jack.top()
jack.push(10)
jack.push(20)
jack.push(30)
jack.pop()