import pygame
import random

pygame.init()

class mazeGenration():
    def __init__(self):
        self.start = 5
        self.maze = [["e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]]
        self.current_pos = [self.start, 0] ## (y, x)
        self.dir = 'd'
        self.row = self.start
        self.col = 1
        self.valid_dir = ['u', 'd', 'l', 'r']

    def set_empty_maze(self):
        for i in range(0, 10):
            self.maze.append(["e", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "e"])
        
        self.maze.append(["e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e"])
        
        self.maze[self.start][1] = 1
        self.maze[self.start][0] = 1
    
    def print_maze(self):
        # use for debugging
        for row in self.maze:
            print(row)

    def generate_maze(self):
        # check going up
        

        if len(self.valid_dir) != 0:
            self.dir = self.get_dir()
            if self.dir == 'u':
                try:
                    if (self.maze[self.row- 1][self.col] == 0) and (self.maze[self.row - 2][self.col] == 0):
                        print("valid path")
                        self.row -= 1
                        self.maze[self.row][self.col] = 1
                        self.valid_dir = ['u', 'd', 'l', 'r'] # reset valid_dir list

                    elif self.maze[self.row - 1][self.col] == "e":
                        return False
                    else:
                        self.valid_dir.remove(self.dir)
                except IndexError:
                    print("not valid path")
            
            # check going down
            if self.dir == 'd':
                try:
                    if (self.maze[self.row + 1][self.col] == 0) and (self.maze[self.row + 2][self.col] == 0):
                        print("valid path")
                        self.row += 1
                        self.maze[self.row][self.col] = 1
                        self.valid_dir = ['u', 'd', 'l', 'r']
                    elif self.maze[self.row + 1][self.col] == "e":
                        return False
                    else:
                        self.valid_dir.remove(self.dir)
                except IndexError:
                    print("not valid path")
            
            # check going left
            if self.dir == 'l':
                try:
                    if (self.maze[self.row][self.col - 1] == 0) and (self.maze[self.row][self.col - 2] == 0):
                        print("valid path")
                        
                        self.col -= 1
                        self.maze[self.row][self.col] = 1
                        self.valid_dir = ['u', 'd', 'l', 'r']
                    elif self.maze[self.row][self.col - 1] == "e":
                        return False
                    else:
                        self.valid_dir.remove(self.dir)
                except IndexError:
                    print("not valid path")

            # check going right
            if self.dir == 'r':
                try:
                    if (self.maze[self.row][self.col + 1] == 0) and (self.maze[self.row][self.col + 2] == 0):
                        print("valid path")
                        self.col += 1
                        self.maze[self.row][self.col] = 1
                        self.valid_dir = ['u', 'd', 'l', 'r']
                    elif self.maze[self.row][self.col + 1] == "e":
                        return False
                    else:
                        self.valid_dir.remove(self.dir)
                except IndexError:
                    print("not valid path")
            
            return True
        else:
            return False
    
    def get_dir(self):
        return random.choice(self.valid_dir)


    


myMaze = mazeGenration()
myMaze.set_empty_maze()
print()
i = 0
go = True
i = 0
while go and i <=10000:
    go = myMaze.generate_maze()

    i += 1
print(i)
print(go)
myMaze.print_maze()
