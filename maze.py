from window import *
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if seed is not None:
            self.seed = random.seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def get_cells(self):
        return self.__cells

    def __create_cells(self):
        for row in range(self.num_rows):
            self.__cells.append([])
            for col in range(self.num_cols):
                cell = Cell(self.win)
                self.__cells[row].append(cell)
                self.__draw_cell(row, col)
    
    def __draw_cell(self, row, col):
        x1 = self.x1 + col * self.cell_size_x
        y1 = self.y1 + row * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[row][col].draw(x1, y1, x2, y2)
        self.__animate()
    
    def __animate(self):
        if self.win is not None:
            self.win.redraw()
        time.sleep(0.005)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.num_rows - 1, self.num_cols - 1)
        
    def __break_walls_r(self, row, col):
        self.__cells[row][col].visited = True
        while True:
            unvisited = []
            if row > 0 and not self.__cells[row - 1][col].visited:
                unvisited.append("up")
            if row < self.num_rows - 1 and not self.__cells[row + 1][col].visited:
                unvisited.append("down")
            if col > 0 and not self.__cells[row][col - 1].visited:
                unvisited.append("left")
            if col < self.num_cols - 1 and not self.__cells[row][col + 1].visited:
                unvisited.append("right")
            if len(unvisited) == 0:
                self.__draw_cell(row, col)
                return
            direction = random.choice(unvisited)
            if direction == "up":
                self.__cells[row][col].has_top_wall = False
                self.__draw_cell(row, col)
                self.__break_walls_r(row - 1, col)
            elif direction == "down":
                self.__cells[row][col].has_bottom_wall = False
                self.__draw_cell(row, col)
                self.__break_walls_r(row + 1, col)
            elif direction == "left":
                self.__cells[row][col].has_left_wall = False
                self.__draw_cell(row, col)
                self.__break_walls_r(row, col - 1)
            elif direction == "right":
                self.__cells[row][col].has_right_wall = False
                self.__draw_cell(row, col)
                self.__break_walls_r(row, col + 1)