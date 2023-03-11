from queue import Queue


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)
        while self.q2.qsize() > 0:
            self.q1.put(self.q2.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q2.get()

    def top(self) -> int:
        return self.q2.queue[0]

    def empty(self) -> bool:
        return self.q2.empty()
