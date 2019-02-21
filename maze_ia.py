#!/usr/bin/env python3

import sys
import copy

def store_maze(source):
    f= open("map.txt","w+")
    f.write(source)
    f.close()

def get_maze():
    maze = ""
    receive = input()
    while "MAZE" not in receive:
        receive = input()
    while len(receive):
        receive = input()
        maze += receive + "\n"
    return maze

def maze_to_matrix():
    list = [[] for _ in range(1000)]
    index = 0

    #OPEN FILE
    f= open("map.txt","rU")
    for lines in f:
        index +=1
        for character in lines:
            if character != "\n":
                list[index].append(character)
                continue
    list = [e for e in list if e]
    result = open("result.txt","w+")
    result.write(str(list))
    return list

def scan_player(matrix):
    playerName = "A"
    for i in range(len(matrix)):
        if playerName in matrix[i]:
            start_position = [i, matrix[i].index(playerName)]
    return start_position
    # print(start_position)

def BFS_algorithm(matrix, start_position):
    current_position = start_position
    data = []
    step = []
    while True:
        step = []
        for current_position in data:
            x = current_position[0] + 1
            y = current_position[1]
            if maze[x][y] is " ":
                step.append([x, y])
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

            x = current_position[0] - 1
            y = current_position[1]
            if maze[x][y] is " ":
                step.append([x, y])
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

            x = current_position[0]
            y = current_position[1] + 1
            if maze[x][y] is " ":
                step.append([x, y])
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

            x = current_position[0]
            y = current_position[1] - 1
            if maze[x][y] is " ":
                step.append([x, y])
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

        data.append(step)

def find_path(destination, data):
    


def checking_point(maze, x, y):
    step = []
    if maze[x][y] is " ":
        step.append([x, y])
        maze[x][y] = "."
    elif (maze[x][y] is "o") or (maze[x][y] is "!"):
        return (x, y), data

def vm_bridge():
    inp = input()
    print("I AM A\n")
    inp = input()
    print("OK\n")



def main():
    # vm_bridge()
    # maze = get_maze()
    # store_maze(maze)

    matrix = maze_to_matrix()
    print(matrix)

    # f= open("guru99.txt","w+")
    # f.write(str(g))
    # f.write(str(maze_to_matrix(get_maze())))

    #
    # matrix = maze_to_matrix()
    # print(matrix)
    #
    # scan_player(maze_to_matrix())

    # scan_matrix(matrix)

if __name__ == "__main__":
    main()
