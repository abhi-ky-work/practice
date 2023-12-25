

class TravellingSalesManProblem:

    def __init__(self,graph):
        self.graph = graph
        # number of vertices in graph G(V,E)
        self.n = len(graph)
        # weather we have visited the node 
        self.visited = [False for _ in range(self.n)]
        # we start with first index vertex
        self.visited[0] = True
        #collect the hamiltonian cycles and get min cycle 
        self.hamiltonian_cycle = []
        # tract what nodes are included in cycle 
        self.path = [0 for _ in range(self.n)]

    def is_valid(self, vertex, actual_position):

        if self.visited[vertex]:
            return False

        if self.graph[actual_position][vertex] == 0:
            return False

        return True

    def tsp(self, actual_position, counter, cost):
        # this eman the last node is connected to first vertex we started with
        if counter == self.n and self.graph[actual_position][0]:
            self.path.append(actual_position)            
            self.hamiltonian_cycle.append([self.path, cost + self.graph[actual_position][0]])
            self.path.pop()
            return

        #consider all nodes in G(V,E) graph ( we filter out )
        #taking the integer values of indexes
        for i in range(self.n):
            if self.is_valid(i, actual_position):
                self.visited[i] = True
                self.path[counter] = i 
                #we call the function recursively
                self.tsp(i, counter + 1, cost + self.graph[actual_position][i])
                self.visited[i] = False


if __name__ == '__main__':

    g = [[0, 1, 0, 2, 0],
         [1, 0, 1, 0, 2],
         [0, 1, 0, 3, 1],
         [2, 0, 3, 0, 1],
         [0, 2, 1, 1, 0]]

    tsp = TravellingSalesManProblem(g)
    tsp.tsp(0,1,0)
    print(min(tsp.hamiltonian_cycle))
    for cycle in tsp.hamiltonian_cycle:
        print(cycle[0], "cost : ", cycle[1])