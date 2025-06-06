import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertEqual(
                    m1.get_cells()[row][col].visited,
                    False
                )
            
    def test_maze_create_cells2(self):
        num_cols = 4
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertEqual(
                    m1.get_cells()[row][col].visited,
                    False
                )
           
    
    def test_maze_create_cells3(self):
        num_cols = 100
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertEqual(
                    m1.get_cells()[row][col].visited,
                    False
                )
            
    
    
if __name__ == "__main__":
    unittest.main()