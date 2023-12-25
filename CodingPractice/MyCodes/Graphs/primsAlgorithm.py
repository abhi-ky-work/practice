import heapq
class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj_list = []

class Edge:
    def __init__(self,weight, start_vertex, final_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.final_vertex = final_vertex

    def __lt__(self, other):
        return self.weight < other.weight


# class Vertex:
#     def __init__(self,name,parent=None):
#         self.name = name
#         self.parent = parent

class PrimsAlgo:

    def __init__(self,unvisited_list):
        # check if the list of unvisited list is 0
        self.unvisited_list = unvisited_list
        self.mst = []
        self.total_cost = 0
        self.heap = []

    def find_spanning_tree(self, starting_vertex):

        self.unvisited_list.remove(starting_vertex)
        actual_vertex = starting_vertex

        while self.unvisited_list:
            for edge in actual_vertex.adj_list:
                if edge.final_vertex in self.unvisited_list:
                    heapq.heappush(self.heap, edge)

            min_edge = heapq.heappop(self.heap)

            # check if the final vertex of this 
            if min_edge.final_vertex in self.unvisited_list:
                self.mst.append(edge)
                print(min_edge.start_vertex.name , "--->", min_edge.final_vertex.name, " : ", min_edge.weight)
                self.total_cost += min_edge.weight
                actual_vertex = min_edge.final_vertex
                self.unvisited_list.remove(actual_vertex)

    def total_cost(self):
        return self.total_cost

    def get_mst(self):
        return self.mst


if __name__ == '__main__':

    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")

    # dealing with undirected edges
    # undirected edge = directed edge (u,v) + directed edge (v,u)
    edgeAB = Edge(2, vertexA, vertexB)
    edgeBA = Edge(2, vertexB, vertexA)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeEA = Edge(5, vertexE, vertexA)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeCA = Edge(6, vertexC, vertexA)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeFA = Edge(10, vertexF, vertexA)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeEB = Edge(3, vertexE, vertexB)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeDB = Edge(3, vertexD, vertexB)
    edgeCD = Edge(1, vertexC, vertexD)
    edgeDC = Edge(1, vertexD, vertexC)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeFC = Edge(2, vertexF, vertexC)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeED = Edge(4, vertexE, vertexD)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeGD = Edge(5, vertexG, vertexD)
    edgeFG = Edge(5, vertexF, vertexG)
    edgeGF = Edge(5, vertexG, vertexF)

    unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG]

    vertexA.adj_list.append(edgeAB)
    vertexA.adj_list.append(edgeAC)
    vertexA.adj_list.append(edgeAE)
    vertexA.adj_list.append(edgeAF)
    vertexB.adj_list.append(edgeBA)
    vertexB.adj_list.append(edgeBD)
    vertexB.adj_list.append(edgeBE)
    vertexC.adj_list.append(edgeCA)
    vertexC.adj_list.append(edgeCD)
    vertexC.adj_list.append(edgeCF)
    vertexD.adj_list.append(edgeDB)
    vertexD.adj_list.append(edgeDC)
    vertexD.adj_list.append(edgeDE)
    vertexD.adj_list.append(edgeDG)
    vertexE.adj_list.append(edgeEA)
    vertexE.adj_list.append(edgeEB)
    vertexE.adj_list.append(edgeED)
    vertexF.adj_list.append(edgeFA)
    vertexF.adj_list.append(edgeFC)
    vertexF.adj_list.append(edgeFG)
    vertexG.adj_list.append(edgeGD)
    vertexG.adj_list.append(edgeGF)

    # run the algorithm
    algorithm = PrimsAlgo(unvisited_list)
    algorithm.find_spanning_tree(vertexD)
    # print(algorithm.get_total_cost())
    # print(algorithm.get_mst())
    print("Total Cost : ", algorithm.total_cost)

    