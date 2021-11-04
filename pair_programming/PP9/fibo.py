"""
Coder : Yiting Han
Listener : Haoming Chen
"""

class FibonacciIterator:
    def __init__(self, fib_class):
        self._fibclass = fib_class
        self._index = 0

    def __next__(self):
        if self._index <len(self._fibclass._array):
            term = self._fibclass._array[self._index]
            self._index += 1
            return term
        else:
            raise StopIteration
        
    def __iter__(self):
        return self
    
      
class Fibonacci:   
    def __init__(self, n):
        self._array = list()
        first = 1
        second = 1 
        for i in range(n):
            self._array.append(second)
            first, second = second, first + second

    def __iter__(self):
        return FibonacciIterator(self)
      
# Test
fib = Fibonacci(10)
print(list(iter(fib)))


