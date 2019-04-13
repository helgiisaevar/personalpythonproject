from flask import Flask, request
from .trees.binary import main#,lets_print_preorder,lets_print_postorder
import json

# import hello from binaryTree

app = Flask(__name__)
# @app.route('/about_tree')
# def hello():
#     print(request.args)
#     return 'In computer science, a binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. A recursive definition using just set theory notions is that a (non-empty) binary tree is a tuple (L, S, R), where L and R are binary trees or the empty set and S is a singleton set. Some authors allow the binary tree to be the empty set as well.'


@app.route('/tree/binary', methods=['POST'])
def handler():
    data = json.loads(request.data)
    tree = main(data)
    print(tree)
    return 'tree'

# @app.route('/tree/preorder', methods=['POST'])
# def handler2():
#     data  = json.loads(request.data)
#     tree = lets_print_preorder(data)
#     print(tree)
#     return 'tree'

# @app.route('/tree/postorder', methods=['POST'])
# def handler3():
#     data  = json.loads(request.data)
#     tree = lets_print_postorder(data)
#     print(tree)
#     return 'tree'

@app.route('/tree/binary/<name>', methods=['GET', 'POST'])
def handler(name):
    if request.method == 'POST':
        return data
    else:
        try:
            info = trees[name]
        except:
            info = 'This is not a recognised tree'
        return info
