class Graph :

    # the all working only for the undirected graph

    def __init__(self):
        self.adjlist = {}   # it creates a dictionary to store the adjacency list representation of the graph   

    def add_vertex(self, vertex):
        if vertex  not in self.adjlist:
            self.adjlist[vertex] = []

    def add_Edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)

    # print the graph , only for the undirected graph
    def printgraph(self):
        for vertex in self.adjlist:
            print(vertex, " --> ", self.adjlist[vertex] , end = "\n")

g = Graph()
g.add_Edge(1,2)
g.add_Edge(2,3)
g.add_Edge(3,4)
g.add_Edge(4,1)
g.add_Edge(2,4)
g.add_Edge(3,5)
g.add_Edge(4,5)

g.printgraph()