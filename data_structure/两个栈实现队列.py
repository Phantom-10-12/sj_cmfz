class Stack(object):
    def __init__(self):
        self.__db = []

    def put(self, item):
        self.__db.append(item)

    def pop(self):
        return self.__db.pop()

    def is_empty(self):
        return self.__db == []  # 为空返回的True


# 1. 所有元素在入队列的时候都入stack2
# 2. 所有元素在出列队的时候都从stack1出
# 3. 当stack1中元素空的时候，将stack2中的元素移入stack1

class Queue(object):

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def put(self, item):
        self.s2.put(item)

    def pop(self):
        # 当s1空的时候，将s2元素移入s1
        if self.s1.is_empty():
            while not self.s2.is_empty():
                self.s1.put(self.s2.pop())

        return self.s1.pop()


if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 10):
        queue.put(i)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
