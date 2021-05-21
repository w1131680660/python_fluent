
class CQueue:
    # 队列特征 ： 先进先出
    # 栈的特征：先进后出
    def __init__(self):
        self.stock_1 = [] #存储的栈
        self.stock_2 = []
    def appendTail(self, value: int) -> None:
        while self.stock_1:
            self.stock_2.append(self.stock_1.pop())
        self.stock_1.append(value)
        while self.stock_2:
            self.stock_1.append(self.stock_2.pop())
        return self.stock_1


    def deleteHead(self) -> int:
        if not self.stock_1:
            return -1
        return self.stock_1.pop()