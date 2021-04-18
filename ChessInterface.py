import chess
from HumanController import HumanController
from AIController import AIController

class ChessInterface():
    def __init__(self, play_mode: str = "PvP"):
        self.board = chess.Board()

    def move(self, move: str):
        move = self.board.parse_san(move)
        if move in self.getLegalMoves():
            self.board.push(move)
        else:
            raise Exception("Illegal Move.")

    def getLegalMoves(self):
        return self.board.legal_moves

    def getResult(self):
        return self.board.result()

    def getTurn(self):
        return self.board.turn
    
    def show(self):
        print(self.board)