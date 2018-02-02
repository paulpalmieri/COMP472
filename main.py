from GameGUI import GameGUI
from Game import Game

if __name__ == '__main__':
    game_board = ['e', 'r', 'p', 'w', 'y', 'g', 'p', 'r', 'r', 'w', 'y', 'g', 'p', 'r', 'p']
    game = Game(game_board)
    gui = GameGUI(game)
    gui.start()

