import window

def main():
    gamewindow = window.Window(800, 600)
    cell1 = window.Cell(gamewindow)
    cell2 = window.Cell(gamewindow)
    cell3 = window.Cell(gamewindow)
    cell4 = window.Cell(gamewindow)
    cell1.draw(50, 50, 150, 150)
    cell2.draw(150, 50, 250, 150)
    cell3.draw(250, 50, 350, 150)
    cell4.draw(350, 50, 450, 150)
    gamewindow.wait_for_close()



if __name__ == "__main__":
    main()
