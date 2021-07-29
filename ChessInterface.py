import chess


class ChessInterface:
    def __init__(self):
        self.board = chess.Board()

    def move(self, move: str):
        move = self.board.parse_san(move)
        if move in self.get_legal_moves():
            self.board.push(move)
        else:
            raise Exception("Illegal Move.")

    def get_legal_moves(self):
        return self.board.legal_moves

    def get_result(self):
        return self.board.result()

    def get_turn(self):
        return self.board.turn

    def show(self):
        print(self.board)
