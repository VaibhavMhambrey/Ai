from collections import deque

def Jug_BFS(jug1_capacity, jug2_capacity, size_req):
    queue = deque()
    visited = set()
    all_paths = []

    queue.append([(0, 0)])

    while queue:
        path = queue.popleft()
        curr = path[-1]

        if curr[0] == size_req:
            all_paths.append(path)

        succ = [(jug1_capacity, curr[1]), (curr[0], jug2_capacity), (0, curr[1]), (curr[0], 0)]

        sp_l = jug1_capacity - curr[0]
        if sp_l >= curr[1]:
            succ.append((curr[0] + curr[1], 0))
        else:
            succ.append((jug1_capacity, curr[1] - sp_l))

        sp_r = jug2_capacity - curr[1]
        if sp_r >= curr[0]:
            succ.append((0, curr[0] + curr[1]))
        else:
            succ.append((curr[0] - sp_r, jug2_capacity))

        for s in succ:
            if s not in visited:
                new_path = list(path)
                new_path.append(s)
                queue.append(new_path)
                visited.add(s)

    return all_paths

# Take user input for jug capacities
jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
size_req = int(input("Enter the desired amount of water in gallons: "))

# Run BFS
all_paths = Jug_BFS(jug1_capacity, jug2_capacity, size_req)

# Display all paths
for path in all_paths:
    print(path)
