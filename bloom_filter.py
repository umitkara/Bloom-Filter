import hashlib
import base64


class BloomFilter:
    def __init__(self, m, k):
        """Bloom Filter constructor. As hash functions, md5 and sha2 are used.

        Args:
            m (int): The number of bits in the Bloom Filter.
            k (int): The number of hash functions used in the Bloom Filter. Must be 1 or 2.
        """
        self.m = m
        self.k = k
        # For sake of simplicity, the Bloom Filter is implemented as a list of 0s and 1s.
        self.data = [0] * m
        self.n = 0

    @property
    def size(self):
        return self.m

    def insert(self, element: str):
        if self.k == 1:
            hash1 = h1(element) % self.m
            self.data[hash1] = 1
        elif self.k == 2:
            hash1 = h1(element) % self.m
            hash2 = h2(element) % self.m
            self.data[hash1] = 1
            self.data[hash2] = 1
        else:
            raise ValueError("k must be 1 or 2")
        self.n += 1

    def search(self, element: str):
        if self.k == 1:
            hash1 = h1(element) % self.m
            if self.data[hash1] == 0:
                return "Not in Bloom Filter"
        elif self.k == 2:
            hash1 = h1(element) % self.m
            hash2 = h2(element) % self.m
            if self.data[hash1] == 0 or self.data[hash2] == 0:
                return "Not in Bloom Filter"
        prob = (1.0 - ((1.0 - 1.0/self.m)**(self.k*self.n))) ** self.k
        percent = (1-prob)*100
        return f"'{element}' might be on the Bloom Filter with a {percent:.2f}% chance."

    def __str__(self):
        return f"Bloom Filter with {str(self.n)} elements."


def h1(w: str):
    h = hashlib.md5(w.encode('utf-8'))
    return hash(base64.b64encode(h.digest())[:6]) % 10


def h2(w: str):
    h = hashlib.sha256(w.encode('utf-8'))
    return hash(base64.b64encode(h.digest())[:6]) % 10


if __name__ == "__main__":
    b = BloomFilter(10, 2)
    b.insert("hello")
    b.insert("World")
    print(b.search("world"))
