from operator import index


class Edge:
    def __init__(self, weight, start_vertex, final_vertex):
        self.weight = weight 
        self.start_vertex = start_vertex
        self.final_vertex = final_vertex

    def __lt__(self,other):
        return self.weight < other.weight

class Node:
    def __init__(self,rank, node_id, parent=None):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent

class Vertex:
    def __init__(self, name):
        self.name = name
        self.node = None


class DisjointSets:
    def __init__(self,vertex_list):
        self.vertex_list = vertex_list
        # to carry the root node of disjoint sets, i.e representatives of root node 
        self.root_nodes =[]

        self.make_sets()


    def make_sets(self):
        for vertex in self.vertex_list:
            node = Node(0, len(self.root_nodes))
            vertex.node = node
            self.root_nodes.append(node)


    def find(self, node):
        current_node = node

        while current_node.parent is not None:
            current_node = current_node.parent

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root 
            current_node = temp

        return root.node_id

    def merge(self,node1, node2):
        # first find the root node of the disjoint set 
        index1 = self.find(node1)
        index2 = self.find(node2)

        # this means both nodes are same 
        if index1 == index2:
            return 

        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.rank < root2.rank:
            root1.parent = root2
        elif root1.rank > root2.rank:
            root2.parent = root1
        else:
            root1.parent = root2
            root2.rank += 1



class KruskalAlgo:

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def find_mst(self):
        disjoint_set = DisjointSets(self.vertex_list)
        mst = []

        # mst algorith
        self.edge_list.sort()

        for edge in self.edge_list:
            u = edge.start_vertex
            v = edge.final_vertex

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                disjoint_set.merge(u.node, v.node)
                mst.append(edge)

        for edge in mst:
            print(edge.start_vertex.name , "----", edge.weight, "----->", edge.final_vertex.name)



if __name__ == "__main__":

     

# vertices in the G(V,E)
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")

    # edges
    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    # have to create a list out of these edges and vertices
    vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]

    # let's run the algorithm
    algorithm = KruskalAlgo(vertices, edges)
    algorithm.find_mst()