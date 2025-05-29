class DirectedGraph:
    def __init__(self):
        self.graph = {}
    def __str__(self):
        return '\n'.join(f'{node} - > {sorted(self.graph[node])}' for node in sorted(self.graph))
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []
    def add_edge(self, a, b):
        if a not in self.graph: self.add_vertex(a)
        if b not in self.graph: self.add_vertex(b)
        self.graph[a].append(b)
        self.graph[b].append(a)
def edges_list(*edges):
    graph = DirectedGraph()
    [graph.add_edge(*edge) for edge in edges]
    return graph

gr = edges_list((0, 1),(2, 3))
gr.add_edge(1, 2)
print(gr)