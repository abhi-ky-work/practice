import heapq


class Edge:

    def __init__(self, weight, sv, dv):
        self.weight = weight
        self.sv = sv
        self.dv = dv


class Node:

    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.min_dist = float("inf")
        self.visited = False
        self.adj_list = []

    def __lt__(self, other):
        return self.min_dist < other.min_dist


class DijkstraAlgo:

    def __init__(self):
        self.heap = []

    def calculate(self, start_node):

        start_node.min_dist = 0

        heapq.heappush(self.heap, start_node)

        while self.heap:

            actual_vertex = heapq.heappop(self.heap)
            # print("Popping and cheching for =>", actual_vertex.name)
            if actual_vertex.visited:
                continue

            for edge in actual_vertex.adj_list:
                u = edge.sv
                v = edge.dv

                new_distance = u.min_dist + edge.weight

                # there is shortest path
                if new_distance < v.min_dist:
                    v.min_dist = new_distance
                    v.predecesssor = u
                    # print("Updating shorted parth for vertex {} : with distnace {}".format(v.name, v.min_dist))
                    # update the heap - this is lazy implementation ( repetition of node with shorter distance in heap )
                    # cz is takes o(n) to find the element and o(logn) to heapfy so o(n) + o(logn) => logn
                    # so is why we use fibbonaci heap
                    heapq.heappush(self.heap, v)

            actual_vertex.visied = True

    @staticmethod
    def shorthest_path(node):

        print("Shortest distance to this vertex {} : {}".format(
            node.name, node.min_dist))
        actual_vertex = node
        while actual_vertex.predecessor is not None:
            print(actual_vertex.predecessor)
            actual_vertex = actual_vertex.predecessor


if __name__ == "__main__":
    # create the nodes
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    # make edges
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # define the neighbours

    node1.adj_list.append(edge1)
    node1.adj_list.append(edge2)
    node1.adj_list.append(edge3)
    node2.adj_list.append(edge4)
    node2.adj_list.append(edge5)
    node2.adj_list.append(edge6)
    node8.adj_list.append(edge7)
    node8.adj_list.append(edge8)
    node5.adj_list.append(edge9)
    node5.adj_list.append(edge10)
    node5.adj_list.append(edge11)
    node6.adj_list.append(edge12)
    node6.adj_list.append(edge13)
    node3.adj_list.append(edge14)
    node3.adj_list.append(edge15)
    node4.adj_list.append(edge16)

    elements = [
        node1,
        node2,
        node3,
        node4,
        node5,
        node6,
        node7,
        node8,
    ]
    # for i in elements:
    #     print("Name :", i.name)
    #     for j in i.adj_list:
    #         print(j.sv.name, " ======={}====>".format(j.weight), j.dv.name, "(", j.dv.min_dist , ")" )

    algorithm = DijkstraAlgo()

    algorithm.calculate(node1)

    algorithm.shorthest_path(node4)
