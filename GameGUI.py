import tkinter as tk
from itertools import product
import random
import time

class GameGUI():

    # candy types and colors
    types = {
        'r': 'orange',
        'b': 'pink',
        'w': 'sienna',
        'y': 'blue',
        'g': 'yellow',
        'p': 'green',
        'e': 'gray17'
    }

    # keycodes for user input
    key_codes = {
        65362: 'UP',
        65361: 'LEFT',
        65363: 'RIGHT',
        65364: 'DOWN'
    }

    inverse_key_codes = {
        'UP':65362,
        'LEFT':65361,
        'RIGHT':65363,
        'DOWN':65364
    }

    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()

        # create game holder
        self.game_frame = tk.Frame(self.root, padx=5, pady=5)
        self.game_frame.pack(side='left', fill='both')

        # create side panel
        self.side_frame = tk.Frame(self.root, width=200, padx=5, pady=5)
        self.side_frame.pack(side='left', fill='both')

        self.game_frame.pack_propagate(False)
        self.side_frame.pack_propagate(False)

        # init game and side panel
        self.side_panel = self.init_side_panel(self.side_frame)
        self.game_grid = self.init_game_grid(self.game_frame)

        self.root.bind('<Key>', self.on_key_press)

    def init_game_grid(self, frame):
        # create empty game board
        board = [[None] * 5 for _ in range(3)]

        # creates a label for each piece and positions them in a grid
        for i, j in product(range(3), range(5)):
            piece_type = self.game.game_board[i][j]
            board[i][j] = L = tk.Label(frame, text=piece_type, bg=GameGUI.types[piece_type], height=2, width=4,
                                       font=("Arial", 40))
            L.grid(row=i, column=j, padx=2, pady=2)
        return board

    # todo: replace displayed text by a global var
    def init_side_panel(self, frame):
        info_list = []

        # possible moves
        possible_move_label = tk.Label(frame, text='Possible moves: ', font='Helvetica 14 bold')
        possible_move_text = tk.Label(frame, text='null')
        possible_move_label.pack()
        possible_move_text.pack()

        # space
        space_label = tk.Label(frame)
        space_label.pack(side='left')

        # last move
        last_move_label = tk.Label(frame, text='Last move: ', font='Helvetica 14 bold')
        last_move_text = tk.Label(frame, text='null')
        last_move_label.pack()
        last_move_text.pack()

        solve_button = tk.Button(frame, text='button')
        solve_button.pack()

        info_list.append(possible_move_text)
        info_list.append(last_move_text)

        return info_list

    # event handler
    def on_key_press(self, event):
        key_code = event.keysym_num

        if key_code in GameGUI.key_codes:
            move = GameGUI.key_codes[key_code]
            print('Valid keyboard input ' + str(move))

            valid = False
            # checks if move is allowed
            for position in self.game.get_adjacent_tiles():
                if position[2] is move:
                    self.update_game_panel(self.game.empty_x, self.game.empty_y, position[0], position[1])
                    self.game.move(position[3])
                    self.update_side_panel()
                    print(self.game.move_list)
                    valid = True

            if not valid:
                print('Cannot move here')


        else:
            print('Invalid keyboard input')

    # updates game grid
    def update_game_panel(self, empty_x, empty_y, new_x, new_y):
        # get 2 relevant cells
        empty_cell = self.game_grid[empty_x][empty_y]
        new_cell = self.game_grid[new_x][new_y]

        # get attributes
        color = new_cell.cget('bg')
        text = new_cell.cget('text')

        # swap cells
        empty_cell.config(bg=color, text=text)
        new_cell.config(bg='gray17', text='e')

    # updates side panel
    def update_side_panel(self):
        possible_moves = [e[2] for e in self.game.get_adjacent_tiles()]
        self.side_panel[0].config(text=possible_moves)

        last_move = self.game.move_list[-1]
        self.side_panel[1].config(text=last_move)





    def start(self):
        self.root.mainloop()
