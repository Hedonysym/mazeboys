import window

def main():
    gamewindow = window.Window(800, 600)
    x1 = 100
    y1 = 100
    num_rows = 40
    num_cols = 40
    cell_size_x = 40
    cell_size_y = 40
    maze = window.Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, gamewindow)
    gamewindow.wait_for_close()



if __name__ == "__main__":
    main()
