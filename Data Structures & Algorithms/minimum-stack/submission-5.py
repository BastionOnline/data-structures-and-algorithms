class MinStack:

    def __init__(self):
        self.array = []
        self.minArray = []

    def push(self, val: int) -> None:
        self.array.append(val)
        val = min(val, self.minArray[-1] if self.minArray else val)
        self.minArray.append(val)

    def pop(self) -> None:
        self.array.pop()
        self.minArray.pop()
        

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minArray[-1]
