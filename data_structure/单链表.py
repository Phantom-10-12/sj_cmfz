# 节点类
class Node(object):
    def __init__(self, item):
        self.item = item  # 值域
        self.next = None  # 指针


# 链表类
class LianBiao(object):
    def __init__(self):
        # 头结点
        self.root = None

    # 添加节点
    def add(self, node):
        # 判断头结点是否为空，为空，挂上，结束
        if not self.root:
            self.root = node
            return

        # 不为空，找当前节点的下一个节点  将根节点变为当前节点
        cur_node = self.root
        while cur_node:
            if not cur_node.next:
                cur_node.next = node
                return
            # 将当前节点的下一个节点重新赋值给当前节点 循环执行
            cur_node = cur_node.next

    def bianli(self):
        cur_node = self.root
        while cur_node:
            print(cur_node.item)
            cur_node = cur_node.next


if __name__ == '__main__':
    l = LianBiao()
    for i in range(1, 10):
        node = Node(i)
        l.add(node)

    l.bianli()
