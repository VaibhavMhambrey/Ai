def dfs(adj, src):
    vis = set()

    def _dfs(node):
        vis.add(node)
        print(node, end=" ")

        for adjNode in adj[node]:
            if adjNode not in vis:
                _dfs(adjNode)

    _dfs(src)

def create_graph():
    # graph = {'1': ['2', '3', '4'], '2': ['1', '5', '6'], '3': ['1'], '4': ['1', '7', '8'], '5': ['2', '9', '10'], '6': ['2'], '9': ['5'], '10': ['5'], '7': ['4', '11', '12'], '8': ['4'], '11': ['7'], '12': ['7']}
    graph={}
    while True:
        try:
            edge_input = input("Enter an edge (or any non-string to stop), e.g., 'A B' for an edge from A to B: ")
            if not edge_input:
                break
            edge = edge_input.split()
            if len(edge) != 2:
                print("Invalid input. Please enter a valid edge.")
                continue
            u, v = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)  # Assuming an undirected graph
        except ValueError:
            break
    return graph

# Create the graph
adj = create_graph()
print("Graph:", adj)

# Take user input for the starting vertex
start_vertex = input("Enter the starting vertex for DFS traversal: ")

# Check if the starting vertex exists in the graph
if start_vertex not in adj:
    print("Starting vertex not found in the graph.")
else:
    print("DFS traversal starting from vertex", start_vertex, ":")
    dfs(adj, start_vertex)
