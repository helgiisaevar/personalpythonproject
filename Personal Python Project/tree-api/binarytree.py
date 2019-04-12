
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
            self._populate_tree(self.root,value)

    def _populate_tree(self,node, value):
        if value < node.data:
            if node.left != None:
                self._populate_tree(node.left,value)
            else:
                node.left = Node(value)         
        else:
            if node.right != None:
                self._populate_tree(node.right,value)
            else:
                node.right = Node(value)

    def print_inorder(self):
        if self.root !=None:
            self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node == None:
            return
        self._print_inorder(node.left)
        print('{}'.format(node.data)) 
        self._print_inorder(node.right)

    def print_preorder(self):
        self._print_preorder(self.root)

    def _print_preorder(self, node):
        if node == None:
            return
        return '{}'.format(node.data)
        self._print_preorder(node.left)
        self._print_preorder(node.right)

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

def main(data):
    e = binary_tree()
    for i in data['numbers']:
        e.populate_tree(i)
    e.print_inorder()
    return e

# def lets_print_preorder(data):
#     e = binary_tree()
#     for i in data['numbers']:
#         e.populate_tree(i)
#     e.print_preorder()
#     return e
    
# def lets_print_postorder(data):
#     e = binary_tree()
#     for i in data['numbers']:
#         e.populate_tree(i)
#     e.print_postorder()
#     return e