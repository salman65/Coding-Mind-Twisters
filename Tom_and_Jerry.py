import sys
import os
import copy

def queElem(pos, dist):
    return [pos, dist]

def queRemove(que):
    elem = que.pop(len(que)-1)
    return que, elem

def isVisited(maze, pos):
    maze[pos[1]][pos[0]] = 'v'
    return maze

def nextPos(maze, pos, que, dist):
    if(pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(maze[0]) and pos[1] < len(maze)):
        if(maze[pos[1]][pos[0]] != 'v' and maze[pos[1]][pos[0]] != 0):
            que.append(queElem(pos,dist))
            temp_maze = isVisited(maze, pos)
            return que, temp_maze
    return que, maze


def distCalc(toPos, iniPos, maze):
    to_visit = []
    temp_maze = copy.deepcopy(maze)
    dist = 0
    next_pos = iniPos
    to_visit.append(queElem(next_pos, dist))
    temp_maze = isVisited(temp_maze, next_pos)
    while(len(to_visit) > 0):
        to_visit, elem = queRemove(to_visit)
        if(elem[0] == toPos):
            return elem[1]
        else:
            next_pos = elem[0]
            dist = elem[1] + 1
            to_visit, temp_maze = nextPos(temp_maze, [next_pos[0]-1, next_pos[1]], to_visit, dist)
            to_visit, temp_maze = nextPos(temp_maze, [next_pos[0]+1, next_pos[1]], to_visit, dist)
            to_visit, temp_maze = nextPos(temp_maze, [next_pos[0], next_pos[1]-1], to_visit, dist)
            to_visit, temp_maze = nextPos(temp_maze, [next_pos[0], next_pos[1]+1], to_visit, dist)
    return -1

def nextMinPos(positions, ini_pos, maze):
    dist = []
    for pos in positions:
        calc = distCalc(pos, ini_pos, maze)
        if(calc == -1):
            return -1
        dist.append(calc)
    return positions[dist.index(min(dist))]

def findCheesePos(maze):
    ans = []
    x=0
    y=0
    for row in maze:
        if 2 in row:
            for col in row:
                if col == 2:
                    ans.append([x,y])
                x=x+1
        x=0
        y=y+1
    return ans

def minMoves(maze, x, y):
    distTrav = 0
    ini_pos = [0,0]
    cheesePos = findCheesePos(maze)
    while(len(cheesePos) > 0):
        minPos = nextMinPos(cheesePos, ini_pos, maze)
        if(minPos == -1):
            return -1
        cheesePos.remove(minPos)
        distTrav = distTrav + distCalc(minPos, ini_pos, maze)
        ini_pos = minPos
    distTrav = distTrav + distCalc([x,y], ini_pos, maze)
    return distTrav

if __name__ == "__main__":
    maze = [
        [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 0, 1, 0, 1, 2, 1, 0, 1, 1 ],
        [ 1, 2, 1, 0, 1, 1, 0, 1, 0, 1 ],
        [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [ 1, 1, 1, 0, 1, 1, 2, 0, 1, 0 ],
        [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
        [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]
    ];
    x=0
    y=7
    dist = minMoves(maze,x,y)
    print('distance: ', dist)
