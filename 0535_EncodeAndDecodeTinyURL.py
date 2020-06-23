class Codec:
    def __init__(self):
        self.state = [0,0,0,0,0,0]
        self.endic = {}
        self.dedic = {}
        self.chlist = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.endic:
            return self.endic[longUrl]
        else:
            tinystr = ''
            for i in range(6):
                tinystr += self.chlist[self.state[i]]
            for i in range(5, 0,-1):
                self.state[i] += 1
                if self.state[i] == 62:
                    self.state[i] = 0
                    self.state[i+1] += 1
            self.endic[longUrl] = "http://tinyurl.com/" + tinystr
            self.dedic[self.endic[longUrl]] = longUrl
            return self.endic[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.dedic:
            return self.dedic[shortUrl]
        else:
            return ''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
