import pygame
import random

pygame.init()



class MazeGen():
    def __init__(self, player_pos = []):
        self.maze = []
        self.n = random.randrange(5, 8)
        self.connections = []
        self.row = 2
        self.col = 0
        self.dim = 20
        self.num_dead = random.randrange(5, 8)
        self.dead_connects = []
    
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
    
    def set_dead_connects(self):
        for i in range(self.num_dead):
            self.dead_connects.append([])
            for j in range(0, random.randrange(2, 4)):
                self.dead_connects[i].append([random.randrange(0,self.dim)-2, random.randrange(0, self.dim-2)])
    
    def connect_points(self):
        # generates the correct path
        self.maze[self.connections[0][0]][0] = 1
        
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
                    
            # horizontal movement
            diff_col = self.connections[j][1] - self.col
            if diff_col < 0:
                for i in range(0, diff_col*-1):
                    self.col -= 1
                    self.maze[self.row][self.col] = 1
            
            if diff_col >=0:
                for i in range(0, diff_col):
                    self.col += 1
                    self.maze[self.row][self.col] = 1
                
            # horizontal movement

    def print_maze(self):
        # use for debugging
        for row in self.maze:
            print(row)

    def get_maze(self):
        return self.maze
    
    def dead_end_points(self):
        for h in range(len(self.dead_connects)):
            self.row = self.dead_connects[h][0][0]
            self.col = self.dead_connects[h][0][1]

            for j in range(0, len(self.dead_connects[h])):
                # vertical movement
                diff_row = self.dead_connects[h][j][0] - self.row
                if diff_row <= 0:
                    for i in range(0, diff_row*-1):
                        self.row -= 1
                        self.maze[self.row][self.col] = 1
                if diff_row > 0:
                    for i in range(0, diff_row):
                        self.row += 1
                        self.maze[self.row][self.col] = 1
                        
                # horizontal movement
                diff_col = self.dead_connects[h][j][1] - self.col
                if diff_col < 0:
                    for i in range(0, diff_col*-1):
                        self.col -= 1
                        self.maze[self.row][self.col] = 1
                
                if diff_col >=0:
                    for i in range(0, diff_col):
                        self.col += 1
                        self.maze[self.row][self.col] = 1
                    


obj = MazeGen()
obj.empty_maze()
obj.set_start()
obj.new_connection()
obj.set_end()
obj.connect_points()

obj.set_dead_connects()
obj.dead_end_points()
obj.print_maze()

