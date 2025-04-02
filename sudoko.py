board = [
    [0, 0, 8, 2, 0, 0, 9, 0, 3],
    [3, 4, 2, 0, 9, 5, 0, 0, 7],
    [1, 9, 7, 0, 0, 0, 0, 0, 4],
    [0, 0, 5, 3, 1, 2, 4, 7, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 7, 4, 5, 0, 0],
    [0, 2, 0, 0, 0, 1, 0, 0, 5],
    [0, 7, 0, 0, 0, 6, 8, 9, 1],
    [8, 0, 0, 4, 3, 0, 7, 0, 6]
]
def solve(bo):
    find=find_empty(bo)
    if not find:
        return True
    else:
        row,col=find

    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True
            bo[row][col]=0
    return False
def valid(bo,num,pos):
    #row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #cloumn
    for i in range(len(bo)):
        if bo[i][pos[1]]== num and pos[0]!=i:
            return False
    #box

    bx=pos[1]//3
    by=pos[0]//3

    for i in range(by*3,by*3+3):
        for j in range(bx*3,bx*3+3):
            if bo[i][j] == num and (i,j)!=pos:
                return False
    return True
def print_bo(bo):
    for row in board:
        print(" ".join(str(num) for num in row))
                   

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)
    return None
solve(board)                     
print_bo(board)                

