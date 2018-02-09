from itertools import product
from util import letter_to_index_map, letter_list, OUTPUT_PATH
import time

class Game:

    rows, cols = 3, 5

    def __init__(self, initial_config):

        # 2D array representing the game board
        self.game_grid = self.init_game_board(initial_config)

        # holds the letter identifier of the empty tile
        self.empty_row, self.empty_col, self.empty_tile = self.init_empty_tile()
        self.move_list = []
        self.possible_moves = self.get_legal_moves()

    # creates a 2d array and fills the board
    def init_game_board(self, initial_config):
        board = [[None] * Game.cols for _ in range(Game.rows)]
        k = 0

        # iterate 3*5 times and fills each cell with the passed spaced string
        for i, j in product(range(Game.rows), range(Game.cols)):
            board[i][j] = initial_config[k]
            k += 1
        return board

    # returns an uppercase letter indicating the position of the empty tile
    def init_empty_tile(self):
        for i, j in product(range(Game.rows), range(Game.cols)):
            if(self.game_grid[i][j] == 'e'):
                return i, j, letter_list[i][j]

    # attempts to make a move
    def move(self, tile_letter):
        if tile_letter in self.possible_moves:
            # get row and col for the tile that needs to move
            tile_row = letter_to_index_map[tile_letter][0]
            tile_col = letter_to_index_map[tile_letter][1]

            # swap with empty tile
            self.game_grid[self.empty_row][self.empty_col] = self.game_grid[tile_row][tile_col]
            self.game_grid[tile_row][tile_col] = 'e'

            # update empty tile
            self.empty_row = tile_row
            self.empty_col = tile_col
            self.empty_tile = tile_letter

            # add move
            self.move_list.append(tile_letter)

            # update legal moves
            self.possible_moves = self.get_legal_moves()



    # checks for symmetry on first and last row
    def goal_state_reached(self):
        for i in range(self.cols):
            if(self.game_grid[0][i] != self.game_grid[2][i]):
                return False
        return True

    # write winning move list to file
    def write_win_to_file(self):
        time_stamp = time.strftime("%Y-%m-%d-%H:%M:%S")
        file_name = OUTPUT_PATH + "cc_" + time_stamp + ".txt"
        with open(file_name, 'w') as f:
            f.write("moves:\t" + "".join(self.move_list))

    def get_legal_moves(self):
        adj_list = []

        # check result of potential moves
        up = self.empty_row - 1 >= 0
        down = self.empty_row + 1 <= 2
        left = self.empty_col - 1 >= 0
        right = self.empty_col + 1 <= 4

        if up:
            adj_list.append(letter_list[self.empty_row - 1][self.empty_col])
        if down:
            adj_list.append(letter_list[self.empty_row + 1][self.empty_col])
        if left:
            adj_list.append(letter_list[self.empty_row][self.empty_col - 1])
        if right:
            adj_list.append(letter_list[self.empty_row][self.empty_col + 1])

        return adj_list

    def display_board(self):
        for e in self.game_grid:
            print(e)