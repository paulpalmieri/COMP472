import tkinter as tk
from auto_solve.util import TYPES, KEY_SET
from itertools import product


class GameGUI:

    # takes a game instance and a tk.TopLevel obj
    def __init__(self, game):

        # init game
        self.game = game

        # init gui tool
        self.root = tk.Tk()

        # create game holder
        self.game_frame = tk.Frame(self.root, padx=2, pady=2)
        self.game_frame.pack(side='left', fill='both')

        # create side panel holder
        self.side_frame = tk.Frame(self.root, width=250, padx=2, pady=2)
        self.side_frame.pack(side='left', fill='both')

        # prevent sizing issues
        self.game_frame.pack_propagate(False)
        self.side_frame.pack_propagate(False)

        # init text variables for side panel
        self.possible_moves_text = tk.StringVar()
        self.last_move_text = tk.StringVar()
        self.warning_text = tk.StringVar()
        self.win_text = tk.StringVar()

        # init game board and side panel
        self.init_side_panel(self.side_frame)
        self.game_grid = self.init_game_grid(self.game_frame)

        # bind key presses to the handler function
        self.root.bind('<Key>', self.on_key_press)

    def init_game_grid(self, frame):
        # create empty game board
        board = [[None] * 5 for _ in range(3)]

        # creates a label for each piece and positions them in a grid
        for i, j in product(range(3), range(5)):
            piece_type = self.game.game_grid[i][j]
            board[i][j] = L = tk.Label(frame, text=piece_type, bg=TYPES[piece_type], height=2, width=4,
                                       font=("Arial", 40))
            L.grid(row=i, column=j, padx=2, pady=2)
        return board

    def init_side_panel(self, frame):

        # last move
        last_move_label = tk.Label(frame, text='Last move: ', font='Helvetica 14 bold')
        last_move_text = tk.Label(frame, textvariable=self.last_move_text)
        last_move_label.pack()
        last_move_text.pack()

        # possible moves
        possible_move_label = tk.Label(frame, text='Possible moves: ', font='Helvetica 14 bold')
        possible_move_text = tk.Label(frame, textvariable=self.possible_moves_text)
        possible_move_label.pack()
        possible_move_text.pack()

        win_label = tk.Label(frame, textvariable=self.win_text, fg='green', font='Helvetica 28 bold')
        win_label.pack(side=tk.BOTTOM)

        # warning
        warning_label = tk.Label(frame, textvariable=self.warning_text, fg='red', font='Helvetica 14 bold')
        warning_label.pack(side=tk.BOTTOM)

        # set side panel text
        self.update_possible_moves()
        self.last_move_text.set('Make your first move')
        self.warning_text.set('')
        self.win_text.set('')

    def update_game_panel(self):
        print('updating gp')
        for i,j in product(range(3), range(5)):
            if self.game_grid[i][j].cget('text') != self.game.game_grid[i][j]:
                self.game_grid[i][j].config(text=self.game.game_grid[i][j])
                self.game_grid[i][j].config(bg=TYPES[self.game.game_grid[i][j]])

    def update_side_panel(self):
        self.update_possible_moves()
        self.update_last_move()

    def update_possible_moves(self):
        move_text = ''
        for e in self.game.possible_moves:
            move_text += e + '\n'
        self.possible_moves_text.set(move_text.rstrip())

    def update_last_move(self):
        last_move = self.game.move_list[-1]
        self.last_move_text.set(last_move)

    def start(self):
        self.root.mainloop()

    # event handler
    def on_key_press(self, event):

        # get keycode from event
        key_code = event.keysym_num
        print('User input keycode: ' + str(key_code))

        # check valid input
        if key_code in KEY_SET:

            # fetch move with table
            move = KEY_SET[key_code]
            print('User input move: ' + move)
            if move in self.game.possible_moves:
                self.game.move(move)
                self.update_game_panel()
                self.update_side_panel()
                self.warning_text.set('')

                if self.game.goal_state_reached():
                    self.game.write_win_to_file()
                    self.root.unbind('<Key>')
                    self.win_text.set("You won!")

                return

            self.warning_text.set('Illegal move, try again.')

        else:
            self.warning_text.set('Invalid keyboard input.\nPlease input letters from A to O')
