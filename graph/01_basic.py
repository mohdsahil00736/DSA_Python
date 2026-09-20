class graph:
# what the problem 
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_graph(self, src, dest):
        if(0<= src < self.size and  0<= dest < self.size):
            self.mat[src][dest] = 1   # for the Dericted graph only one way 
            # self.mat[dest][src] = 1  # for the undericted graph both way 
            # self.mat[src][dest] = weight     # for the weighted graph
        else: 
            print("invalid Graph")

    def printGraph(self):
        for row in self.mat:
            print(' '.join(map(str, row)))


G = graph(3)
G.add_graph(0,1)
G.add_graph(0,2)
# G.add_graph(2,1)
G.add_graph(2,3)


G.printGraph()
