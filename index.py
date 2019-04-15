from flask import Flask, request
from about.about import About
from utils.utils import Utils
from trees.binary import main as binaryTree

import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # TODO tell here about this pojects and tell about the endpoints possible and what they do. make it look nice when you make requests
    # Say again here all the endpoints you say in readme
    return 'Python tree helper api \n /about_tree to get about tree. use /tree to do this and that'


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


@app.route('/trees/<tree>', methods=['POST'])
def createTree(tree):
    '''
    We create trees
    '''
    if (tree == 'binary_tree'):
        data = json.loads(request.data)
        tree = binaryTree(data)
        print(str(tree))
        return str({"tree": str(tree)})
    else:
        return Utils.res('invalid-route', '/trees/' + tree)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    '''
    Handler for all routes that fall through.
    '''
    return Utils.res('invalid-route', "/" + path)


''' @app.route('/tree/preorder', methods=['POST'])
def preorder():
    data = json.loads(request.data)
    tree = get_preorder(data)
    return 'tree'


@app.route('/tree/postorder', methods=['POST'])
def postorder():
    data = json.loads(request.data)
    tree = get_postorder(data)
    return 'tree'


@app.route('/tree/binary/<name>', methods=['GET', 'POST'])
def indexff(name):
    if request.method == 'POST':
        return data
    else:
        try:
            info = trees[name]
        except:
            info = 'This is not a recognised tree'
        return info
 '''
