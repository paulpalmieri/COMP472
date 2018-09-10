from manual_solve.GameGUI import GameGUI
from manual_solve.Game import Game
from auto_solve.util import load_single_game
from auto_solve.heuristics import *
from auto_solve.automatic_solve import solve
import argparse

default_input = 'input/input.txt'

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-manual", "-m", help="start a single game in manual mode", action="store_true")
    parser.add_argument("-automatic", "-a", help="solves all grids in the input file", action="store_true")
    parser.add_argument("-file", "-f", help="path to the input file containing the grid(s) to solve")
    args = parser.parse_args()

    # auto play
    if args.automatic:
        print('Automatic mode has been selected.')

        if args.file:
            print('An input file has been specified: ' + args.file)
            file_name = args.file
        else:
            print('No input file has been specified, loading default input file for auto solver.')
            file_name = default_input

        heuristic = Strategy(local_manhattan)
        solve(file_name, heuristic)



    # manual play
    elif args.manual:
        print("Manual mode has been selected.")

        if args.file:
            print('A file has been specified.')
            grid = load_single_game(args.file)
        else:
            print('No file has been specified, loading default input file for manual play.')
            grid = load_single_game(default_input)

        game = Game(grid)
        gui = GameGUI(game)
        gui.root.mainloop()