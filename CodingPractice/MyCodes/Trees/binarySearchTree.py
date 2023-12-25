class Node:
    def __init__(self,data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # going to left sub treee
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild )
            else:
                node.leftChild = Node(data, node)
        # going to right sub tree
        else:
            if node.rightChild:
                self.insert_node( data , node.rightChild )
            else:
                node.rightChild = Node(data, node)
    
    def in_order_traversal(self,  root ):
        if root is None:
            print( "Tree is empty")
        else:
            self.in_order_traversal(root.leftChild)
            print(root.data)
            self.in_order_traversal(root.rightChild)

    def pre_order_traversal(self, root):
        if root is None:
            print( "Tree is empty")

        else:
            print(root.data)
            self.pre_order_traversal(root.leftChild)
            self.pre_order_traversal(root.rightChild)

    def post_order_traversal(self, root):
        if root is None:
            print("Tree is empty")
        else:
            self.post_order_traversal(root.leftChild)
            self.post_order_traversal(root.rightChild)
            print(root.data)

    def get_max_val(self):
        if self.root:
            return self.get_max(self.root.rightChild)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        
        return node.data
        

class compareTree:
    def compare(self, node1, node2):

        if not node1 or not node2:
            return node1 == node2
        
        if node1.data is not node2.data:
            return False

        return self.compare( node1.leftChild , node2.leftChild ) and self.compare( node1.rightChild, node2.rightChild )
        


bst = BinarySearchTree()
bst1 = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(3)
bst.insert(50)
bst.insert(15)
bst.insert(222)
bst.insert(25)
bst.insert(35)

bst1.insert(20)
bst1.insert(10)
bst1.insert(3)
bst1.insert(50)
bst1.insert(15)
bst1.insert(222)
bst1.insert(25)
bst1.insert(35)

print("In Order Traversal :")
bst.in_order_traversal( bst.root )
print("Pre Order Traversal :")
bst.pre_order_traversal( bst.root )
print("Post Order Traversal")
bst.post_order_traversal( bst.root )

# print("Empty tree scenario")
# bst1.in_order_traversal(bst1.root)

print("Max element of the tree : " , bst.get_max( bst.root ))
print("Max Val element of the tree : " , bst.get_max_val())

compare_tree = compareTree()
print("Tree Comparison test : ", compare_tree.compare(bst.root, bst1.root) )