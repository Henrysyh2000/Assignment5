from queue import Empty # Use this for exception
class LeakyStack():

    def __init__(self, max_size):
        self._data = [None] * max_size   # Static size
        self._size = 0    # Track current number of elements
        self._top = 0  # Use this variable to make the stack circular

    def push(self, e):  # O(1)
        """ push element e into top of the stack, with leaky feature. """
        pass

    def pop(self):      # O(1)
        """ pop and return the element stored at top of the stack. """
        pass

    def __len__(self):  # O(1)
        """ return the current stack size. """
        pass

    def is_empty(self): # O(1)
        """ return True if the stack is empty. """
        pass

    def __str__(self):  # O(n) or O(1) up to you, not graded
        pass


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''
def main():
    leakystack = LeakyStack(5)  # Max size = 5 stack.
    leakystack.push('a')
    leakystack.push('b')
    leakystack.push('c')
    print(leakystack)   # top of stack --> c b a
    leakystack.push('d')
    leakystack.push('e')
    print(leakystack)  # top of stack --> e d c b a 
    leakystack.push('f')
    print(leakystack)   # top of stack --> f e d c b,   a is gone because it is the oldest.
    print(leakystack.pop())  # f popped
    print(leakystack.pop())  # e popped
    print(leakystack)   # top of stack --> d c b

if __name__ == '__main__':
    main()
