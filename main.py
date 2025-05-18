import window
import maze

def main():
    gamewindow = window.Window(800, 600)
    x1 = 40
    y1 = 40
    num_rows = 14
    num_cols = 18
    cell_size_x = 40
    cell_size_y = 40
    gamemaze = maze.Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, gamewindow)
    gamewindow.wait_for_close()



if __name__ == "__main__":
    main()
