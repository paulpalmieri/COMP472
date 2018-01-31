from itertools import product
from string import ascii_uppercase as alphabet

class Game:

    # 2D array of uppercase letters, same for all instances
    position_grid = [list(alphabet[0:5]), list(alphabet[5:10]), list(alphabet[10:15])]
    rows, cols = 3, 5

    def __init__(self, initial_config):
        # init game grid
        self.game_board = self.init_game_board(initial_config)

        # init empty tile coordinates
        self.empty_x, self.empty_y = self.init_empty_tile()
        self.move_list = []

    # gets game board as 2D array
    def init_game_board(self, initial_config):
        board = [[None] * Game.cols for _ in range(Game.rows)]
        k = 0
        for i, j in product(range(Game.rows), range(Game.cols)):
            board[i][j] = initial_config[k]
            k += 1
        return board

    # returns an uppercase letter indicating the position of the empty tile
    def init_empty_tile(self):
        for i, j in product(range(Game.rows), range(Game.cols)):
            if(self.game_board[i][j] == 'e'):
                return i, j

    # swaps the empty tile with an adjacent tile
    def move(self, x, y):
        self.game_board[self.empty_x][self.empty_y] = self.game_board[x][y]
        self.empty_x, self.empty_y = x, y
        self.game_board[x][y] = 'e'
        self.move_list.append(Game.position_grid[x][y])

    # checks for symmetry on first and last row
    def goal_state_reached(self):
        for i in range(self.cols):
            if(self.game_board[0][i] != self.game_board[2][i]):
                return False
        return True

    # checks adjacent tiles coordinates
    #todo: can make the list smaller if needed
    def get_adjacent_tiles(self):
        adj_list = []
        up = self.empty_x - 1 >= 0
        down = self.empty_x + 1 <= 2
        left = self.empty_y - 1 >= 0
        right = self.empty_y + 1 <= 4

        if up:
            node = [self.empty_x - 1, self.empty_y, 'UP']
            adj_list.append(node)
        if down:
            node = [self.empty_x + 1, self.empty_y, 'DOWN']
            adj_list.append(node)
        if left:
            node = [self.empty_x, self.empty_y - 1, 'LEFT']
            adj_list.append(node)
        if right:
            node = [self.empty_x, self.empty_y + 1, 'RIGHT']
            adj_list.append(node)

        return adj_list

    def display_board(self):
        for e in self.game_board:
            print(e)

    # NOT USED gets a list that maps a letter to a pair of indexes relevant to the game grid
    def get_position_dict(self):
        position_dict = {}
        k = 0
        for i, j in product(range(3), range(5)):
            position_dict[alphabet[k]] = [i, j]
            k += 1
        return position_dict