class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    stack = []

    def push(self, x):
        # write your code here
        self.stack.append(x)

    """
    @return: nothing
    """

    def pop(self):
        # write your code here
        self.stack = self.stack[:-1]

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        return self.stack[-1]

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        # write your code here
        if len(self.stack) == 0:
            return True
        else:
            return False