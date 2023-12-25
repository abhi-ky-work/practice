class Node:

    def __init__(self, vertex):
        self.vertex = vertex
        self.visited = False
        self.adjacency_list = []


def BFS(start_node):

    queue = [start_node]
    print("---------BFS FOR GRAPH----------")
    while queue:
        actual_node = queue.pop(0)
        if  not actual_node.visited:
            print(actual_node.vertex)
        actual_node.visited = True
        
        for adj_node in actual_node.adjacency_list:
            if not adj_node.visited:
                queue.append(adj_node)

def DFS(start_node):

    stack = [start_node]
    print("---------DFS FOR GRAPH----------")
    while stack:
        actual_node = stack.pop()
        if  not actual_node.visited:
            print(actual_node.vertex)
        actual_node.visited = True
        
        for adj_node in actual_node.adjacency_list:
            if not adj_node.visited:
                stack.append(adj_node)

def DFS_recursion(start_node):

    stack = [start_node]
    # print("---------DFS FOR GRAPH----------")
    if  not start_node.visited:
        print(start_node.vertex)
    start_node.visited = True
    
    for adj_node in start_node.adjacency_list:
        if not adj_node.visited:
            DFS_recursion(adj_node)


def graph1():
    nodeA= Node("A")
    nodeB= Node("B")
    nodeC= Node("C")
    nodeD= Node("D")
    nodeF= Node("F") 
    nodeE= Node("E") 

    nodeA.adjacency_list.append(nodeC)
    nodeA.adjacency_list.append(nodeB)

    nodeB.adjacency_list.append(nodeA)
    nodeB.adjacency_list.append(nodeD)
    nodeB.adjacency_list.append(nodeF)
    nodeB.adjacency_list.append(nodeE)


    nodeF.adjacency_list.append(nodeB)
    nodeF.adjacency_list.append(nodeD)

    nodeD.adjacency_list.append(nodeC)
    nodeD.adjacency_list.append(nodeB)
    nodeD.adjacency_list.append(nodeF)

    nodeC.adjacency_list.append(nodeA)
    nodeC.adjacency_list.append(nodeD)
    nodeC.adjacency_list.append(nodeE)

    nodeE.adjacency_list.append(nodeB)
    nodeE.adjacency_list.append(nodeC)
    return nodeA

def graph2():
    node1= Node("A")
    node2= Node("B")
    node3= Node("C")
    node4= Node("D")  
    node5= Node("E")  

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    return node1
    

# BFS(nodeA)

# A
# C
# B
# D
# E
# F
# DFS(nodeA)
# A
# B
# E
# C
# D
# F
# DFS_recursion(graph2() )
# A
# C
# D
# B
# F
# E

# BFS( graph2() )
# A
# B
# C
# D
# E
# DFS( graph2() )
# A
# C
# B
# D
# E
# DFS_recursion(graph2() )
# A
# B
# D
# E
# C



# Given a tree, you need to select a leaf and remove it, 
# and repeat this process until all the nodes are removed. 
# Return the removal sequence.

class RemoveLeafNodes:
  def __init__(self, root):
    self.root = root
    self.node_removed = []
    
  def remove_leaf_nodes(self,root):
    actual_node = root
    if len(actual_node.adjacency_list) == 0:
      return
    for node, index in actual_node.adjacency_list:#n
      if len(node.adjacency_list) == 0:
        # this is a leaf node
        self.node_removed.append(node)
        #actual_node.adjacency_list.pop(index) #adjacency_list
        
      self.remove_leaf_nodes(node)
      
# o(n*n_adj_node)

tree = RemoveLeafNodes(graph1())
tree.remove_leaf_nodes(tree.root)
print(tree.node_removed)