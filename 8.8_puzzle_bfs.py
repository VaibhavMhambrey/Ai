def drawstate(state):
    dash =13*"-"
    for i in range(3):
        print(dash)
        print("| ",end ="")
        for j in range(3):
            if state[i][j] !=0:
                print(state[i][j],end = " | ")
            else:
                print("_",end=" | ")    
        print()
    print(dash)
def heuristic(state,goal):
    count =0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=goal[i][j]:
                count+=1
    return count
def find_misplaced(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j
def movegen(state,goal):
    X,Y = find_misplaced(state)
    templist = [(X+1,Y),(X-1,Y),(X,Y+1),(X,Y-1)]
    templist = [x for x in templist if 0<=x[0]<3 and 0<=x[1]<3]
    newstate=[]
    for x in templist:
        new = [row[:] for row in state]
        new[X][Y] = state[x[0]][x[1]]
        new[x[0]][x[1]] = 0
        newstate.append((new,heuristic(new,goal))) 
    return newstate



def BestFirstSearch(start,goal):
    count = 0
    open = [(start,heuristic(start,goal))]
    closed = []
    closed.append(open)
    traversal = []
    par={}
    templist = []
    while open:
        a = open.pop(0)
        count+=1
        print(f"Step {count}: ")
        drawstate(a[0])
        traversal.append(a)
        if a[1] == 0:
            print("Goal state reached!!")
            break
        templist = movegen(a[0],goal)
        templist = [x for x in templist if x not in closed]
        
        open+=templist
        closed.extend(templist)
        open.sort(key = lambda x:x[1])
        print(open)

def eightpuzzle():
    start =[[2,8,3],
            [1,6,4],
            [7,0,5]]
    
    goal = [[1,2,3],
            [8,0,4],
            [7,6,5]]
    print("Initial state: ")
    drawstate(start)
    print("Goal state: ")
    drawstate(goal)
    BestFirstSearch(start,goal)

eightpuzzle()