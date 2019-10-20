class SharedMemoryStack():
    '''
    Design two stacks that share the same Python list, self._data.
    Both stacks can grow independently;

    no new item can be pushed in either stack when self._data is full.
    '''

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * SharedMemoryStack.DEFAULT_CAPACITY
        self.stack1_size = 0
        self.stack2_size = 0

    def pushStack1(self, e):
        """ push element e into stack1 """
        pass

    def pushStack2(self, e):
        """ push element e into stack2 """
        pass

    def popStack1(self):
        """ pop and return the value stored at top of the stack1 """
        pass

    def popStack2(self):
        """ pop and return the value stored at top of the stack2 """
        pass

    def is_full(self):
        """return True stack1 size + stack2 size == SharedMemoryStack.DEFAULT_CAPACITY"""
        pass

    def is_empty1(self):
        """return True if stack1 is empty"""
        pass

    def is_empty2(self):
        """return True if stack2 is empty"""
        pass

    def peekStack1(self):
        """return the value stored at top of stack1"""
        pass

    def peekStack2(self):
        """return the value stored at top of stack2"""
        pass

    def __str__(self):   # Not graded.
        result = []
        result.append("Stack 1: ")
        # Your code 1 to show stack 1
        result.append("Stack 2: ")
        # Your code 2 to show stack 2

        return "".join(result)


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''

def main():
    stack = SharedMemoryStack()
    stack.pushStack1(1)
    stack.pushStack1(2)
    stack.pushStack1(3)
    stack.pushStack1(4)
    stack.pushStack2(5)
    stack.pushStack2(6)
    stack.pushStack2(7)
    stack.pushStack2(8)
    stack.pushStack2(9)
    stack.pushStack2(10)
    print(stack)  # Stack 1: 1, 2, 3, 4; Stack 2: 5, 6, 7, 8, 9, 10
    print("Popping: ", stack.popStack1())  # popped 4
    stack.pushStack2(11) # Stack 1: 1, 2, 3; Stack 2: 5, 6, 7, 8, 9, 10, 11
    print(stack)

if __name__ == '__main__':
    main()






