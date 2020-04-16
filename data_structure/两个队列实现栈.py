class Queue(object):
    def __init__(self):
        self.__db = []

    def put(self, item):
        self.__db.append(item)

    def pop(self):
        return self.__db.pop(0)

    def is_empty(self):
        return self.__db == []


# 1. q2永远为空，q1永远不为空
# 2.入栈的时候，所有元素都入到q2，将q1中所有的元素取出放入q2，并且交换q1与q2
# 3.出栈的时候，所有元素直接从q1中弹出即可
class Stack(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def put(self, item):
        self.q2.put(item)
        # 当q1不为空的时候，每次添加新的元素，都需要交换位置
        while not self.q1.is_empty():
            self.q2.put(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop()


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 10):
        stack.put(i)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
