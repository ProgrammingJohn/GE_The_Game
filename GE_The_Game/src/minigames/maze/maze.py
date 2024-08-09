

import time
from maze_generator import MazeGenerator


class Maze():

    def __init__(self, callback, size: tuple = (5, 5)):

        self.callback = callback
        self.size = size
        self.width = size[0]
        self.height = size[1]
        # self.maze = self.generate_maze()
        self.maze = [
            ['w', 'c', 'w', 'w', 'w',],
            ['w', 'c', 'w', 'w', 'w',],
            ['w', 'c', 'c', 'w', 'w',],
            ['w', 'w', 'c', 'c', 'w',],
            ['w', 'w', 'w', 'c', 'w',],
        ]

        self.maze[0][1] = "P"
        self.player_row = 0
        self.player_col = 1

    def print_maze(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'w'):
                    print(str("#"), end=" ")
                elif (self.maze[i][j] == 'c'):
                    print(str(" "), end=" ")
                else:
                    print(str("P"), end=" ")

            print('\n')

    def generate_maze(self):
        maze_generator = MazeGenerator()
        return maze_generator.generate_maze(self.size)

    def clicked_key(self, key_selection: str):
        if key_selection == "w" or key_selection == "UP_ARROW":  # change to IO!! need IO class
            self.player_move_up()
        if key_selection == "a" or key_selection == "LEFT_ARROW":  # change to IO!! need IO class
            self.player_move_left()
        if key_selection == "s" or key_selection == "DOWN_ARROW":  # change to IO!! need IO class
            self.player_move_down()
        if key_selection == "d" or key_selection == "RIGHT_ARROW":  # change to IO!! need IO class
            self.player_move_right()

    def get_neighbors(self) -> list[str]:
        neighbors = [None, None, None, None]

        if self.player_row != 0:  # y != 0
            neighbors[0] = self.maze[self.player_row - 1][self.player_col]

        if self.player_col != 0:  # x != 0
            neighbors[1] = self.maze[self.player_row][self.player_col - 1]

        if self.player_row != self.height - 1:  # y != 4
            neighbors[2] = self.maze[self.player_row + 1][self.player_col]

        if self.player_col != self.width - 1:  # x != 4
            neighbors[3] = self.maze[self.player_row][self.player_col + 1]

        return neighbors

    def player_move_up(self):
        neighbors = self.get_neighbors()

        if neighbors[0] == "c":
            self.maze[self.player_row][self.player_col] = "c"
            self.player_row -= 1
            self.maze[self.player_row][self.player_col] = "P"

        self.check_end()

    def player_move_left(self):
        neighbors = self.get_neighbors()

        if neighbors[1] == "c":
            self.maze[self.player_row][self.player_col] = "c"
            self.player_col -= 1
            self.maze[self.player_row][self.player_col] = "P"

        self.check_end()

    def player_move_down(self):
        neighbors = self.get_neighbors()
        print(neighbors)

        if neighbors[2] == "c":
            self.maze[self.player_row][self.player_col] = "c"
            self.player_row += 1
            self.maze[self.player_row][self.player_col] = "P"

        self.check_end()

    def player_move_right(self):
        neighbors = self.get_neighbors()

        if neighbors[3] == "c":
            self.maze[self.player_row][self.player_col] = "c"
            self.player_col += 1
            self.maze[self.player_row][self.player_col] = "P"

        self.check_end()

    def check_end(self):
        if self.player_col == self.width - 2 and self.player_row == self.height - 1:
            self.callback()


test_grid = [
    ['w', 'c', 'w', 'w', 'w',],
    ['w', 'c', 'w', 'w', 'w',],
    ['w', 'c', 'c', 'w', 'w',],
    ['w', 'w', 'c', 'c', 'w',],
    ['w', 'w', 'w', 'c', 'w',],
]


def on_win():
    print("win")


if __name__ == "__main__":
    maze = Maze(on_win)
    maze.generate_maze()
    maze.print_maze()
    print("=================")
    print(maze.player_row, maze.player_col)
    maze.clicked_key("s")
    maze.clicked_key("s")
    maze.clicked_key("s")
    maze.clicked_key("d")
    maze.clicked_key("s")
    maze.clicked_key("d")
    maze.clicked_key("s")
    print(maze.player_row, maze.player_col)
    maze.print_maze()
