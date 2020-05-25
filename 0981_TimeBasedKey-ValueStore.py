class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((value, timestamp))
        else:
            self.dic[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        maxts = 0
        out = ""
        if key in self.dic:
            for value, ts in reversed(self.dic[key]):
                if ts <= timestamp:
                    maxts = ts
                    out = value
                    break
            return out
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
