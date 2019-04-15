from flask import Flask, request
from about.about import About
from utils.utils import Utils
from trees.binary import get_inorder as binary_inorder, get_preorder as binary_preorder, get_postorder as binary_postorder

import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # TODO, make better docs here below
    return 'Python tree helper API: \n Routes: \n \t - GET: "/about" See what trees you can get information about \n \t - GET: "/about/:tree"  Get information about specific tree \n \t - POST: "/tree/:tree/:order"  Create a tree with body {"numbers": [1, 2, 3]} and receive it in respected order'


@app.route('/about',  methods=['GET'])
def about():
    '''
    Handler for the about route.
    '''
    possibleRoutes = ['binary', 'red-black', 'avl']
    tmp = ''
    for route in possibleRoutes:
        tmp = route + ', ' + tmp
    return 'Possible routes: ' + tmp


@app.route('/about/<name>',  methods=['GET'])
def about_tree(name):
    '''
    Handler for the about route.
    Returns about information about various things.
    '''
    try:
        getInfo = About.trees[name].get('info')
        return str(getInfo)
    except:
        return Utils.res('invalid-route', '/about/' + name)


@app.route('/tree/<tree>/<order>', methods=['POST'])
def createTree(tree, order):
    '''
    We create and order trees
    '''

    if (tree == 'binary'):

        data = json.loads(request.data)
        if (order == 'inorder'):
            return str(binary_inorder(data))
        elif (order == 'preorder'):
            return str(binary_preorder(data))
        elif (order == 'postorder'):
            return str(binary_postorder(data))
        else:
            return Utils.res('invalid-route', '/trees/' + tree)

    else:
        return Utils.res('invalid-route', '/trees/' + tree)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    '''
    Handler for all routes that fall through.
    '''
    return Utils.res('', 'This route or the HTTP call on this route was not recognized. Please see route "/" for help.')
