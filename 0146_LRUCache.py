class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.values = []

    def get(self, key: int) -> int:
        if key in self.keys:
            v = self.values[self.keys.index(key)]
            self.put(key,v)
            return v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.values.pop(self.keys.index(key))
            self.keys.remove(key)
        if len(self.keys) >= self.capacity:
            self.keys.pop(0)
            self.values.pop(0)
        self.keys.append(key)
        self.values.append(value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
