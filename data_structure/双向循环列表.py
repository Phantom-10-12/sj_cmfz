class Node(object):
    def __init__(self, item):
        self.item = item  # 值域
        self.next = None  # 后指针
        self.prev = None  # 前指针   （previous）


class LianBiao(object):
    def __init__(self):
        # 头结点
        self.root = None

    # 添加节点
    def add(self, node):
        # 判断头结点是否为空，为空，挂上，结束
        if not self.root:
            self.root = node
            node.prev = node
            node.next = node
            return

        # 不为空，找当前节点的下一个节点  将根节点变为当前节点
        cur_node = self.root
        node.next = cur_node
        node.prev = cur_node.prev
        cur_node.prev.next = node
        cur_node.prev = node
        cur_node = node



    def bianli(self):  # 打印列表
        cur_node = self.root
        put_list=[]
        while cur_node and cur_node not in put_list:
            print(cur_node.item)
            print(cur_node.prev)
            print(cur_node.next)
            put_list.append(cur_node)
            cur_node = cur_node.next


if __name__ == '__main__':
    l = LianBiao()
    for i in range(1, 10):
        node = Node(i)
        l.add(node)

    l.bianli()
