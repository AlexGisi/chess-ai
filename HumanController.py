import chess
class HumanController:
    def __init__(self):
        pass
    def getMove(self, board: chess.Board, player: bool) -> str:
        return str(input("Enter your move: "))