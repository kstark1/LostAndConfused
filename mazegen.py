import pygame
import random

pygame.init()



class MazeGen():
    def __init__(self):
        self.maze = []
        self.n = random.randrange(5, 8)
        self.connections = []
        self.row = 2
        self.col = 0
        self.dim = 20
    
    def empty_maze(self):
        for i in range(0, self.dim):
            self.maze.append([0]*self.dim)
        
    
    def set_start(self):
        self.connections.append([random.randrange(self.dim), 0])
        self.row = self.connections[0][0]
    
    def set_end(self):
        self.connections.append([random.randrange(self.dim), 19])
    
    def new_connection(self):
        for i in range(0, self.n):
            self.connections.append([random.randrange(0,self.dim), random.randrange(0, self.dim-1)])
    
    def connect_points(self):
        self.maze[self.connections[0][0]][0] = 1
        print(self.row, self.col)
        for j in range(0, len(self.connections)):
            # vertical movement
            diff_row = self.connections[j][0] - self.row
            if diff_row <= 0:
                for i in range(0, diff_row*-1):
                    self.row -= 1
                    self.maze[self.row][self.col] = 1
            if diff_row > 0:
                for i in range(0, diff_row):
                    self.row += 1
                    self.maze[self.row][self.col] = 1
                    
            print(self.row, self.col)
            # horizontal movement
            print(j)
            print("test", self.connections[j][1], self.col)
            diff_col = self.connections[j][1] - self.col
            if diff_col < 0:
                for i in range(0, diff_col*-1):
                    self.col -= 1
                    self.maze[self.row][self.col] = 1
            
            if diff_col >=0:
                for i in range(0, diff_col):
                    self.col += 1
                    self.maze[self.row][self.col] = 1
                
            print(self.row, self.col)
            # horizontal movement

    def print_maze(self):
        # use for debugging
        for row in self.maze:
            print(row)

    def get_maze(self):
        return self.maze



obj = MazeGen()
obj.empty_maze()
obj.set_start()
obj.new_connection()
obj.set_end()
obj.connect_points()
obj.print_maze()
print(obj.connections)

