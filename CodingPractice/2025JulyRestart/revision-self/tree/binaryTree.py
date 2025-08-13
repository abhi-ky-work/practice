class Node:
    def __init__(self, data,parent ):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):  
        if data < node.data:
            if node.left:
                self.insert_node(self, data, node)
            else:
                node.left = Node(data, node)
        if data >= node.data:
            if node.right:
                self.insert_node(self, data, node)
            else:
                node.right = Node(data, node)

    