class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictlog = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.dictlog.get(message) is None:
            self.dictlog[message] = timestamp
            return True

        lasttime = self.dictlog[message]
        if lasttime + 10 <= timestamp:
            self.dictlog[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
