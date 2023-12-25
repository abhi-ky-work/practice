import sys

class DijkstraAlgo:
    # vertexes are the of the for 0 1 2 3 4 i.e they will be behaivng like interger value not as node object
    def __init__(self, adj_matrix, start_vertex):
            self.adj_matrix = adj_matrix
            self.start_matrix = start_vertex
            self.v = len(adj_matrix)
            self.visited = [False for _ in range(self.v)]
            self.distance = [float("inf") for _ in range(self.v)]
            self.distance[start_vertex] = 0


    def get_min(self):

        min_value = sys.maxsize
        min_index = 0

        # doing a linear search here, we should have used heap here for logV instead V
        for index in range(self.v):
            if not self.visited[index] and self.distance[index] < min_value:
                min_index = index
                min_value = self.distance[index]

        return min_index

    def calculate(self):
        
        for vertex in range(self.v):
            actual_vertex = self.get_min()
            self.visited[actual_vertex] = True

            print("Considering vertex : ", actual_vertex)

            for other_vertex in range(self.v):
                if self.adj_matrix[actual_vertex][other_vertex] > 0:
                    if not self.visited[other_vertex]:
                        if self.distance[other_vertex] > self.distance[actual_vertex] + self.adj_matrix[actual_vertex][other_vertex]:
                            self.distance[other_vertex] = self.distance[actual_vertex] + self.adj_matrix[actual_vertex][other_vertex]

    def print_distances(self):
        print(self.distance)

if __name__ == "__main__":
    adj_mat = m =  [[0, 7,  5,  2,  0, 0],
                    [7, 0,  0,  0,  3, 8],
                    [5, 0,  0, 10,  4, 0],
                    [2, 0, 10,  0,  0, 2],
                    [0, 3,  4,  0,  0, 6],
                    [0, 8,  0,  2,  6, 8]]

    algorithm = DijkstraAlgo(adj_mat, 1)
    algorithm.calculate()
    algorithm.print_distances()