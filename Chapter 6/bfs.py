def bfs(letter, target):
    search_queue = []
    search_queue += my_graph[letter]
    visited = []

    while search_queue:
        node = search_queue.pop(0)

        if node not in visited:
            if node == target:
                print(f"found the target -> {target}")
                return True
            else:
                print(f"{node} is not the target {target}")
                search_queue += my_graph[node]
                visited.append(node)

    return False


my_graph = {}

my_graph['A'] = ['B', 'E']
my_graph['B'] = ['D', 'E']
my_graph['C'] = ['A']
my_graph['D'] = ['B', 'C']
my_graph['E'] = []

bfs('A', 'C')
