class Stack:
    """
    Implementation of a stack
    """
    def __init__(self):
        """
        Class constructor

        @return: null
        """
        self.s = []

    def push(self, item):
        """
        Add an item to the stack

        @param item: item to push
        @return: null
        """
        self.s.append(item)

    def pop(self):
        """
        Remove an item from the stack

        @return: popped item
        """
        return self.s.pop()

    def peek(self):
        """
        Get what's on top of the stack

        @return: most recently pushed item
        """
        return self.s[-1]

    def size(self):
        """
        Get how many items are in the stack

        @return: length of stack
        """
        return len(self.s)

def main():
    stack = Stack()

    stack.push(1)
    stack.push(5)
    stack.push(10)

    print(stack.peek())
    stack.pop()
    print(stack.peek())
    
    print('size: {}'.format(stack.size()))

if __name__ == "__main__": 
    main()
