class Node(object):
    def __init__(self, item):
        self.item = item  # 值域
        self.left = None  # 左子树
        self.right = None  # 右子树


class Tree(object):

    def __init__(self):
        self.root = None  # 根节点

    def add(self, item):
        node = Node(item)
        # 1.先判断头结点是否为空，为空将元素挂上，结束
        if not self.root:
            self.root = node
            return
        # 2.根节点不为空，将根节点放入队列中
        q = [self.root]
        # 3.从队列中取出一个节点作为当前节点
        while True:
            cur_node = q.pop(0)
            # 4.判断当前节点的左子树是否为空，为空，挂上，结束
            if not cur_node.left:
                cur_node.left = node
                return
            # 5.不为空，将左子树放入队列中
            q.append(cur_node.left)
            # 6.判断当前节点的右子树是否为空，为空，挂上，结束
            if not cur_node.right:
                cur_node.right = node
                return
            # 7.不为空，将右子树放入访问队列中
            q.append(cur_node.right)
        # 8.重复执行3 - 7，直到元素挂上为止

    # 先序 根左右
    def per_order(self, node):
        # 当节点为空的时候，不再进行遍历，返回空列表
        if not node:
            return []

        result = []

        result.append(node.item)  # 访问根节点
        left = self.per_order(node.left)  # 以先序的形式访问左子树
        right = self.per_order(node.right)  # 以先序的形式访问右子树

        return result + left + right

    # 中序 左根右
    def mid_order(self, node):
        # 当节点为空的时候，不再进行遍历，返回空列表
        if not node:
            return []

        result = []

        result.append(node.item)  # 访问根节点
        left = self.mid_order(node.left)  # 以中序的形式访问左子树
        right = self.mid_order(node.right)  # 以中序的形式访问右子树

        return left + result + right

    # 后序 左右根
    def order(self, node):
        # 当节点为空的时候，不再进行遍历，返回空列表
        if not node:
            return []

        result = []

        result.append(node.item)  # 访问根节点
        left = self.order(node.left)  # 以后序的形式访问左子树
        right = self.order(node.right)  # 以后序的形式访问右子树

        return left + right + result

    # 层次遍历
    def level(self):
        # 1.定义一个访问结果列表
        result = []  #（一个储存访问结果的列表）
        # 2.将根节点放入待访问列表
        q = [self.root]   #（一个储存访问顺序的列表）
        # 3.从待访问列表中取出一个节点作为当前节点
        while q:
            cur_node = q.pop(0)
            # 4.取出当前节点的值放入结果列表中
            result.append(cur_node.item)
            # 5.将当前节点的(非空)左右子树访问待访问列表中
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        # 6.重复执行3 - 5步，直到待访问列表为空，则终止循环
        # 7.返回结果列表
        return result

    #交换左右子树
    def change_left_right(self,node):
        if not node:
            return []

        result = []

        result.append(node.item)  # 访问根节点
        left = self.per_order(node.left)  # 以先序的形式访问左子树
        right = self.per_order(node.right)  # 以先序的形式访问右子树

        return result  + right  +left

if __name__ == '__main__':

    tree = Tree()
    for i in range(1, 10):
        tree.add(i)

    result = tree.per_order(tree.root)
    print(result)

    order = tree.mid_order(tree.root)
    print(order)

    order = tree.order(tree.root)
    print(order)

    level = tree.level()
    print(level)

    change_left_rigjt = tree.change_left_right(tree.root)
    print(change_left_rigjt)