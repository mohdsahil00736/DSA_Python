from collections import deque

class graph:

    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_graph(self, src, dest):
        if(0<= src < self.size and  0<= dest < self.size):
            self.mat[src][dest] = 1   # for the Dericted graph only one way 
            self.mat[dest][src] = 1  # for the undericted graph both way 
        else: 
            print("invalid Graph")

    def printGraph(self):
        for row in self.mat:
            print(' '.join(map(str, row)))

    def BFS(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True

        while(queue):
            v = queue.popleft()
            print(v, end = "->")
            for i in range(self.size):
                if(self.mat[v][i] == 1 and visited[i] == False):
                    visited[i] = True
                    queue.append(i)

G = graph(8)

G.add_graph(0,1)
G.add_graph(0,3)
G.add_graph(3,4)
G.add_graph(3,5)
G.add_graph(4,6)
G.add_graph(6,2)
G.add_graph(6,7)

G.BFS(0)