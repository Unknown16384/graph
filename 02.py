def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            [queue.append(a) for a in graph[vertex] if a not in visited]

'''кстати, в такого рода задачах в интернете обычно используют класс deque, но я как-то не понимаю особого в этом смысла. он работает быстрее, чем обычный список, или что?'''