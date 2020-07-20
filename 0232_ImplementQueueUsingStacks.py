class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qmain = []
        self.qsub = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.qmain.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.qsub) == 0:
            while len(self.qmain) > 0:
                self.qsub.append(self.qmain[-1])
                self.qmain.pop(-1)
        val = self.qsub[-1]
        self.qsub.pop(-1)
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.qsub) == 0:
            while len(self.qmain) > 0:
                self.qsub.append(self.qmain[-1])
                self.qmain.pop(-1)
        return self.qsub[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.qmain) + len(self.qsub) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
