class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)
        while timestamp - self.hits[0] > 300:
            self.hits.pop(0)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        hitcount = len(self.hits)
        idx = 0
        if hitcount > 0:
            while self.hits[idx] + 300 <= timestamp:
                hitcount -= 1
                idx += 1
                if idx >= len(self.hits):
                    break
        
        return hitcount


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
