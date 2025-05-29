class Graph:
    def __init__(self, *edges):
        self.size = 2
        self.matrix = [[0, 0], [0, 0]]
        [self.add_edge(*edge) for edge in edges]
    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])
    def add_edge(self, a, b):
        if self.size <= max(a, b): self.resize(max(a, b))
        self.matrix[a][b] = 1
    def resize(self, size):
        while self.size <= size:
            [self.matrix[row].append(0) for row in range(self.size)]
            self.matrix.append([0]*(self.size+1))
            self.size += 1

graph = Graph((0, 1), (1, 0), (2, 1))
graph.add_edge(3, 2)
print(graph)
'''задания, конечно, можно и поточнее было сформировать. надеюсь, это соответствует требованиям'''