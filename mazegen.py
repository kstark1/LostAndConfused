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
        
    
    def set_start(self, player_pos = [2, 3]):
        if len(player_pos) != 0:
            self.connections.append(player_pos)
        else:
            self.connections.append([random.randrange(self.dim), 0])
            self.row = self.connections[0][0]
    
    def set_end(self):
        self.connections.append([random.randrange(self.dim), 19])
    
    def new_connection(self):
        for i in range(0, self.n):
            self.connections.append([random.randrange(0,self.dim), random.randrange(0, self.dim-1)])
    
    def set_dead_connects(self, player_pos = [4, 5]):
        for i in range(self.num_dead):
            self.dead_connects.append([])
            for j in range(0, random.randrange(3, 5)):
                self.dead_connects[i].append([random.randrange(1,self.dim)-2, random.randrange(1, self.dim-2)])
            self.dead_connects[i].append(random.choice(self.connections[1:-1]))
    
    def get_endpoint(self):
        return self.connections[-1]

        
    
    def connect_points(self):
        # generates the correct path
        self.maze[self.connections[0][0]][0] = 1
        
        for j in range(0, len(self.connections)):
            # picking randomly which direction to travel
            direction = random.randrange(0, 2)

            if direction == 0:
                self.vertical(j)
                self.horizontal(j)
            
            else:
                self.horizontal(j)
                self.vertical(j)

    
    def vertical(self, j):
        diff_row = self.connections[j][0] - self.row
        if diff_row <= 0:
            for i in range(0, diff_row*-1):
                self.row -= 1
                self.maze[self.row][self.col] = 1
        if diff_row > 0:
            for i in range(0, diff_row):
                self.row += 1
                self.maze[self.row][self.col] = 1
    
    def horizontal(self, j):
        diff_col = self.connections[j][1] - self.col
        if diff_col < 0:
            for i in range(0, diff_col*-1):
                self.col -= 1
                self.maze[self.row][self.col] = 1
            
        if diff_col >=0:
            for i in range(0, diff_col):
                self.col += 1
                self.maze[self.row][self.col] = 1


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
                # randomly picking weather to move in the horizontal direction
                # first of the vertical direction
                direction = random.randrange(0, 2)

                if direction == 0:
                    self.dead_vertical(h, j)
                    self.dead_horizontal(h, j)
                else:
                    self.dead_horizontal(h, j)
                    self.dead_vertical(h, j)
                

    def dead_vertical(self, h, j):
        diff_row = self.dead_connects[h][j][0] - self.row
        if diff_row <= 0:
            for i in range(0, diff_row*-1):
                self.row -= 1
                self.maze[self.row][self.col] = 1
            if diff_row > 0:
                for i in range(0, diff_row):
                    self.row += 1
                    self.maze[self.row][self.col] = 1

    def dead_horizontal(self, h, j):
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

