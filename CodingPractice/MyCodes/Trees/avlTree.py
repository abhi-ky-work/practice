class Node:

    def __init__(self, data, parent):
        self.data = data
        self.right_node = None
        self.left_node = None
        self.height = 0
        self.parent = parent


class AvlTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root )

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node )
            else:
                node.left_node = Node(data, node)
                node.height = max(self.cal_height(node.left_node), self.cal_height(node.right_node)) + 1
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.cal_height(node.left_node), self.cal_height(node.right_node)) + 1

        # handle_violation
        # balance = self.cal_height(node.left_node) - self.cal_height(node.right)
        # if balance > 1:
        #     if self.cal_height(node.left_node.left_node) >= self.cal_height(node.left_node.right_node)

        self.handle_violation(node)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # if node is leaf node
            if node.left_node is None and node.right_node is None:
                #  not check if the node is rc or lc 
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:  # ir parent is root to be removed
                    self.root = None

                del node
                self.handle_violation()
            # if the node has single child with right child
            elif node.left_node is None and node.right_node is not None:
                print("Removing node which has single right child", node.data)
                parent = node.parent

                if parent is not None:# ir parent is not root
                    # no check if node to delete is parents lc or rc 
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    # parent is none i.e the node is the root which we are deleting 
                    self.root = node.right_node

                node.right_node.parent = parent
                del node
                self.handle_violation()
            elif node.right_node is None and node.left_node is not None:
                print("Removing the node with single left child")
                parent = node.parent

                if parent is not None:
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                else:
                    self.root = node.left_node
                
                node.left_node.parent = parent 

                del node
                self.handle_violation()
            # if node to remove has 2 children
            elif node.right_node is not None and node.left_node is not None:
                print("Removing the node with two children")
                parent = node.parent
                # we find for the predecesssor i.e largest element in the left subtree
                # or find the successor i.e the smallest element in the right sub tree
                successor_node = self.get_predecessor(node.left_node)

                tmp = successor_node.data
                successor_node.data = node.data
                node.data = tmp

                self.remove_node( data, successor_node )
                self.handle_violation()

    def in_order_traversal(self, node):
        if node is None:
            return "tree is empty"
        else:
            self.in_order_traversal(node.left_node)
            print(node.data)
            self.in_order_traversal(node.right_node)

    # solve this challange to get the node which you want to retrieve
    def get_node(self, data, node):
        if node is None:
            return "tree is empty"
        # else:
        #     print("in get node ", node.data)
        #     if node.data == data and node is not None:
        #         print( node.left_node.data, "-", node.data, "-", node.right_node.data)
        #         # print( node.left_node, "-", node.data, "-", node.right_node)
        #         return node
        #     if node.left_node is not None:
        #         return self.get_node(data, node.left_node)
        #     if node.right_node is not None:
        #         return self.get_node(data, node.right_node)
        if node.data == data:
            return node
        else:
            self.get_node(data, node.left_node )
        
    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node )
        
        return node
        
    def get_successor(self, node):
        if node.left_node:
            return self.get_successor(node)

        return node

    def cal_height(self, node):
        if node is None:
            return -1
        return node.height


    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.cal_height(node.left_node) - self.cal_height(node.right_node)


    #checks weather the subtree is balanced with node = root node
    def voilation_helper(self, node):

        balance = self.calculate_balance(node)

        # if balcne > 1 its a left heavy situation ie. can be left-left heavy or leaf-right heavy situation
        if balance > 1:
            # left-right heavy situation ie. left rotation on parent and right rotation on grand parent
            if self.calculate_balance(node.left_node) < 0: 
                self.rotate_left(node.left_node)
            # this is right rotation on grandparent( ie. right rotation on left-left heavy situation )
            self.rotate_right(node)
        
        # its a right havy situation ie. it can be right-left heavy situation or right-right heavy situation
        if balance < -1:
            # its is a right-left heavy situation right-rotation on parent left rotation on grandparent
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node) 
            # this is left rotation on grandparent ( ie. right right heavy situation)
            self.rotate_left(node)  
    
    def handle_violation(self,node):#this node is the parent node
        # check all the nodes from the node we added till the root node.
        while node is not None:
            node.height = max(self.cal_height(node.left_node) , self.cal_height(node.right_node)) + 1
            self.voilation_helper(node)
            #whenever we settle a voilation it may happen that it 
            #violate the AVL properties in other section of tree
            node = node.parent

    # node is the grandparent 
    def rotate_right(self,node):
        print("Rotating the grandparent to right.....", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.cal_height(node.left_node), self.cal_height(node.right_node)) + 1
        temp_left_node.height = max(self.cal_height(temp_left_node.left_node), self.cal_height(temp_left_node.right_node)) + 1

    def rotate_left(self, node):
        print("Rotating the node left .....", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t


        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if t is not None:
            t.parent = node

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node


        node.height = max( self.cal_height(node.left_node), self.cal_height(node.right_node)) + 1
        temp_right_node.height = max(self.cal_height(temp_right_node.left_node), self.cal_height(temp_right_node.right_node)) + 1


    def traverse(self,node):
        if node is not None:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node is None :
            return
        else:
            self.in_order_traversal(node.left_node)
            left_data = "X"
            right_data = "X"
            if node.left_node :
                left_data = node.left_node.data
            if node.right_node:
                right_data = node.right_node.data
            print( "{} ----- {}({},{}) ---- {}".format( left_data, node.data,node.height,self.calculate_balance(node), right_data))
            self.in_order_traversal(node.right_node)
            



if __name__ == "__main__":


    avl = AvlTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(10)
    avl.insert(2)
    avl.insert(4)
    avl.insert(15)
    avl.insert(26)


    avl.traverse(avl.root)
    print("Rooot :", avl.root.data)









# avlt = AvlTree()
# avlt.insert(100)
# avlt.insert(80)
# avlt.insert(200)
# avlt.insert(70)
# avlt.insert(90)
# avlt.insert(150)
# avlt.insert(300)
# avlt.insert(140)
# avlt.insert(160)
# avlt.insert(400)
# avlt.insert(350)
# avlt.insert(410)
# avlt.insert(50)
# avlt.insert(40)
# avlt.insert(60)

# print("In order traversal of AVL Tress: ")
# avlt.in_order_traversal(avlt.root)

# node_to_delete = 200
# print("Removing node : ", node_to_delete)
# print("Node Before delete", avlt.get_node(node_to_delete, avlt.root))
# print("Success which will be choosen")
# avlt.remove_node(node_to_delete, avlt.root )
# print("In order traversal of AVL Tress after removing node with two children: ")
# avlt.in_order_traversal( avlt.root )