class Stack(object):
    def __init__(self):
        self.__db = []

    def put(self, item):
        self.__db.append(item)

    def pop(self):
        return self.__db.pop()


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 10):
        stack.put(i)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
