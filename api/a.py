class operations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addn(self):
        d = self.a + self.b
        return d

    def sqr(self, a, b):
        return a* b

if __name__ == "__main__":
    a = 1
    b = 3
    op = operations(a,b)
    x = op.addn()
    print(x)
    y = op.sqr(a,b) # operations.sqr(os, 3)
    print(y)

