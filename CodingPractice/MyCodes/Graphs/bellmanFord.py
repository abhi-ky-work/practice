class Node:
    def __init__(self,name):
        self.name = name
        self.adj_list = []
        self.predecessor = None
        self.min_distance = float("inf")

class Edge:
    def __init__(self,weight,start_vertex,final_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.final_vertex = final_vertex


class BellmanFordAlgo:
    def __init__(self,vertex_list, edge_list, start_vertex):
        self.start_vertex = start_vertex
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.has_cycle = False
        self.yen_optimise = False

    def calculate(self):

        self.start_vertex.min_distance = 0

        for _ in range(len(self.vertex_list) - 1 ):
            any_min_dist_optimised = False
            if self.yen_optimise > 1:
                print("Terminating Bellman-Ford with Yen Optimisation")
                continue

            for edge in self.edge_list:
                u = edge.start_vertex
                v = edge.final_vertex

                if u.min_distance + edge.weight < v.min_distance: 
                    v.min_distance = u.min_distance + edge.weight
                    v.predecessor = u
                    any_min_dist_optimised = True
                    if self.yen_optimise == 1:
                        self.yen_optimise = 0
                
            for edge in self.edge_list:
                if self.check_cycle(edge):
                    print("Negative cycle detected")
                    return

            if not any_min_dist_optimised:
                self.yen_optimise += 1
                print("No Edge Optimised")


    def check_cycle(self,edge):
        u = edge.start_vertex
        v = edge.final_vertex
        if u.min_distance + edge.weight < v.min_distance: 
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortestPath(self,node):
        current_node = node
        while current_node is not None:
            if not self.has_cycle:
                print("Shortest Distance found for node : ", current_node.name, "Idist: {}".format(current_node.min_distance))
                current_node = current_node.predecessor
            else:
                print("Negative Cycle found: ")


if __name__ == "__main__":

     # we have to create the vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    # let's create the edges
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(6, node7, node3)

    # handle the adjacency lists
    node1.adj_list.append(edge1)
    node1.adj_list.append(edge2)
    node2.adj_list.append(edge3)
    node2.adj_list.append(edge4)
    node2.adj_list.append(edge5)
    node3.adj_list.append(edge6)
    node3.adj_list.append(edge7)
    node4.adj_list.append(edge8)
    node5.adj_list.append(edge9)
    node5.adj_list.append(edge10)
    node6.adj_list.append(edge11)
    node7.adj_list.append(edge12)

    # run the algorithm
    vertices = (node1, node2, node3, node4, node5, node6, node7)
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)

    algorithm = BellmanFordAlgo(vertices, edges, node1)
    algorithm.calculate()
    algorithm.get_shortestPath(node7)