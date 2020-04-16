class Queue(object):
    def __init__(self):
        self.__db = []

    def put(self, item):
        self.__db.append(item)

    def pop(self):
        return self.__db.pop(0)


if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 10):
        queue.put(i)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
