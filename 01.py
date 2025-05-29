class DirectedGraph:
    def __init__(self):
        self.graph = {}
    def __str__(self):
        return '\n'.join(f'{node} - > {sorted(self.graph[node])}' for node in sorted(self.graph))
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []
    def add_edge(self, a, b):
        if a not in self.graph: self.add_vertex(a)
        self.graph[a].append(b)

gr = DirectedGraph()
gr.add_edge('A', 'C')
gr.add_edge('A', 'B')
gr.add_edge('B', 'A')
gr.add_edge('B', 'C')
print(gr)