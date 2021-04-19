from ChessInterface import *
from HumanController import *
from AIController import *

class Driver:
    def __init__(self, play_mode: str = "PvP"):
        self.ci = ChessInterface()
        if play_mode not in ["PvP", "AIvP", "PvAI", "AIvAI"]:
            play_mode = "PvP"
            print("Play mode not recognized, defaulted to PvP")
        self.cont1 = HumanController() if play_mode[0] == "P" else AIController()
        self.cont2 = HumanController() if play_mode[-1] == "P" else AIController()
    
    def run_game(self):
        while self.ci.getResult() == "*":
            turn = self.ci.getTurn()
            print(f"\n{self.ci.board}\n{'white to move' if turn else 'black to move'}\n")
            try:
                if turn: #white to move
                    self.ci.move(self.cont1.getMove(self.ci.board, True))
                else:
                    self.ci.move(self.cont2.getMove(self.ci.board, False))
            except ValueError:
                print("Invalid move, try again\n")
        print(f"\n{self.ci.board}\n{'white to move' if turn else 'black to move'}\n")
        print(self.ci.getResult())