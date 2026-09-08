class MinStack:

    def __init__(self):
        self.lst = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.lst.append(val)

        if self.minstack and self.minstack[-1] < val:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.lst.pop()
        self.minstack.pop()        

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
