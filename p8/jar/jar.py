class Jar:
    def __init__(self, capacity=12):
        if capacity<=0:
            raise ValueError
        self._capacity = capacity
        self._size=0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self.size+=n

    def withdraw(self, n):
        if n>self.size:
            raise ValueError
        self._size-=n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity<=0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if size>self.capacity:
            raise ValueError
        self._size=size
if __name__ == "__main__":
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)
