from queue import Empty # Use this for exception
class LeakyStack():

    def __init__(self, max_size):
        self._data = [None] * max_size   # Static size
        self._size = 0    # Track current number of elements
        self._top = 0  # Use this variable to make the stack circular

    def push(self, e):  # O(1)
        """ push element e into top of the stack, with leaky feature. """
        self._size += 1
        if self._size > len(self._data):
            self._size -= 1
            self._data[self._top] = e
            self._top += 1
            self._top %= len(self._data)
            
        else:
            self._data[self._size - 1] = e
        print(self._data)

    def pop(self):      # O(1)
        """ pop and return the element stored at top of the stack. """
        if self.is_empty():
            raise Empty
        else:
            loc = (self._top + self._size - 1) % len(self._data)
            res = self._data[loc]
            self._data[loc] = None
            self._size -= 1
            return res
        
    def __len__(self):  # O(1)
        """ return the current stack size. """
        return self._size

    def is_empty(self): # O(1)
        """ return True if the stack is empty. """
        if len(self) == 0:
            return True
        return False

    def __str__(self):  # O(n) or O(1) up to you, not graded
        res = ''
        for i in range(len(self)):
            res += ' ' + self._data[(self._top + i) % len(self._data)]
        return res[::-1]


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.
def main():
    leakystack = LeakyStack(5)  # Max size = 5 stack.
    leakystack.push('a')
    leakystack.push('b')
    leakystack.push('c')
    #print(leakystack)   # top of stack --> c b a
    leakystack.push('d')
    leakystack.push('e')
    #print(leakystack)  # top of stack --> e d c b a 
    leakystack.push('f')
    ##################
    leakystack.push('g')
    leakystack.push('h')
    #print(leakystack)
    ###################

    #print(leakystack)   # top of stack --> f e d c b,   a is gone because it is the oldest.
    print(leakystack.pop())  # f popped
    print(leakystack.pop())  # e popped
    #######################
    print(leakystack.pop())
    #######################
    print(leakystack)   # top of stack --> d c b

if __name__ == '__main__':
    main()
'''