class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 100000
        self.array = []
        for _ in range(self.N):
            self.array.append([])

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.array[key % self.N].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            h = key % self.N
            for i,value in enumerate(self.array[h]):
                if key == value:
                    self.array[h].pop(i)
                    break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h = key % self.N
        for value in self.array[h]:
            if key == value:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
