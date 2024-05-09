import random
def generate_random_state():
    return [random.randint(0, 7) for _ in range(8)]

def conflicts(state, row, col):
    # count the number of conflicts
    count = 0
    for i in range(len(state)):
        if i != row: # makes sure we are not checking conflicts int he same row
            if state[i] == col or abs(i - row) == abs(
            state[i] - col
            ): # horiz, vert, diag
                count += 1
    return count

def heuristic(state):
    # number of conflicts in the current state
    total_conflicts = 0
    for i in range(len(state)):
        total_conflicts += conflicts(state, i, state[i])
    return total_conflicts

def print_board(state):
    for i in range(8):
        for j in range(8):
            if state[i] == j:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()
    print()

def min_conflicts(state, max_iter=10):
    for _ in range(max_iter):
        if heuristic(state) == 0: # no conflicts
            return state
        row = min_conflict_row(state)
        col = min_conflict_col(state, row)
        state[row] = col
        print_board(state)
    return None

def min_conflict_row(state):
    min_conflicts = float("inf")
    min_row = -1
    for i in range(8):
        for j in range(8):                
            if j != state[i]:
                state_copy = state[:]
                state_copy[i] = j
                conflicts_count = heuristic(state_copy)
                if conflicts_count < min_conflicts:
                    min_conflicts = conflicts_count
                    min_row = i
    return min_row

def min_conflict_col(state, row):
    #Find the column with the minimum conflicts for a queen in a given row."""
    min_conflicts = float("inf")
    min_col = -1
    for col in range(8):
        conflict_count = conflicts(state, row, col)
        if conflict_count < min_conflicts:
            min_conflicts = conflict_count
            min_col = col
    return min_col

# MAIN
initial_state = generate_random_state()
# initial_state = [0, 1, 2, 3, 4, 5, 6, 7]
for x in initial_state:
    print(x + 1, end=" ")
print()
print("Initial State")
print_board(initial_state)

solution = min_conflicts(initial_state)

# Print the solution
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found within the maximum number of iterations.")
    