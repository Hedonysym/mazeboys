from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y,
            fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.win is None:
            return
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black")
        else:
            self.win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "white")
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black")
        else:
            self.win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "white")
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black")
        else:
            self.win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "white")
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black")
        else:
            self.win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "white")

    def center(self):
        return Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2)

    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
        if undo:
            self.win.draw_line(Line(self.center(), to_cell.center()), "gray")
        else:
            self.win.draw_line(Line(self.center(), to_cell.center()), "red")
