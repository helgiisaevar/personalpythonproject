
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


class binary_tree():
    def __init__(self):
        self.root = None

    def populate_tree(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._populate_tree(self.root, value)

    def _populate_tree(self, node, value):
        if value < node.data:
            if node.left != None:
                self._populate_tree(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right != None:
                self._populate_tree(node.right, value)
            else:
                node.right = Node(value)

    def print_inorder(self):
        if self.root != None:
            self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node == None:
            return
        self._print_inorder(node.left)
        print('{}'.format(node.data))
        self._print_inorder(node.right)

    def get_inorder(self):
        bag = []
        if self.root != None:
            self._get_inorder(self.root, bag)
        return bag

    def _get_inorder(self, node, bag):
        if node == None:
            return
        self._get_inorder(node.left, bag)
        bag.append(('{}'.format(node.data)))
        self._get_inorder(node.right, bag)

    def get_preorder(self):
        bag = []
        self._get_preorder(self.root, bag)
        return bag

    def _get_preorder(self, node, bag):
        if node == None:
            return
        bag.append(('{}'.format(node.data)))
        self._get_preorder(node.left, bag)
        self._get_preorder(node.right, bag)

    def print_preorder(self):
        self._print_preorder(self.root)

    def _print_preorder(self, node):
        if node == None:
            return
        return '{}'.format(node.data)
        self._print_preorder(node.left)
        self._print_preorder(node.right)

    def get_postorder(self):
        bag = []
        self._get_postorder(self.root, bag)
        return bag

    def _get_postorder(self, node, bag):
        if node == None:
            return
        self._get_postorder(node.left, bag)
        self._get_postorder(node.right, bag)
        bag.append(('{}'.format(node.data)))

    def print_postorder(self):
        self._print_postorder(self.root)

    def _print_postorder(self, node):
        if node == None:
            return
        self._print_postorder(node.left)
        self._print_postorder(node.right)
        print('{}'.format(node.data))

    def __str__(self):
        self.print_inorder()
        return ''


def get_tree(data):
    tree = binary_tree()

    for i in data['numbers']:
        tree.populate_tree(i)
    
    return tree

def get_inorder(data):
    return get_tree(data).get_inorder()

def get_preorder(data):
    return get_tree(data).get_preorder()

def get_postorder(data):
    return get_tree(data).get_postorder()
    
