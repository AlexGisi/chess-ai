import chess
import numpy as np
from time import time

class AIController:
    PIECE_MAP = {
        'P': 1,     # White Pawn
        'p': -1,    # Black Pawn
        'N': 3,     # White Knight
        'n': -3,    # Black Knight
        'B': 3,     # White Bishop
        'b': -3,    # Black Bishop
        'R': 5,     # White Rook
        'r': -5,    # Black Rook
        'Q': 9,     # White Queen
        'q': -9,    # Black Queen
        'K': 10,    # White King
        'k': -10    # Black King
    }
    def __init__(self, depth: int = 3) -> None:
        self.depth = depth
        self.leavesCalculated = 0

    def heuristic(self, board: chess.Board) -> float:
        return np.sum([AIController.PIECE_MAP[char] if char in AIController.PIECE_MAP else 0 for char in board.board_fen()])

    def minimax(self, board: chess.Board, depth: int, maximizingPlayer: bool) -> float:
        #brd = board.copy()
        #print(depth)
        if depth == 0 or board.is_game_over():
            return self.heuristic(board)
        if maximizingPlayer:
            value = -AIController.PIECE_MAP['K'] * 16  # lower bound
            for move in board.legal_moves:
                child = self.make_child(board, move)
                value = max(value, self.minimax(child, depth-1, False))
            return value  # returns best move
        else:  # minimizing player
            value = AIController.PIECE_MAP['K'] * 16  # upper bound
            for move in board.legal_moves:
                child = self.make_child(board, move)
                value = min(value, self.minimax(child, depth-1, True))
            self.leavesCalculated += 1
            return value

    def make_child(self, board: chess.Board, move: str) -> chess.Board:
        child = board.copy()
        child.push(move)
        return child

    def getMove(self, board: chess.Board, player: bool) -> str:
        self.leavesCalculated = 0
        timer = time()
        legal_moves = list(board.legal_moves)
        move_costs = [self.minimax(self.make_child(board, move), self.depth, player) for move in legal_moves]
        
        if player:
            move = board.san(legal_moves[np.argmax(move_costs)])
            print("Move taken has a value of: ", max(move_costs))
        else:
            move = board.san(legal_moves[np.argmin(move_costs)])
            print("Move taken has a value of: ", min(move_costs))

        elapsed = time() - timer
        print(f"Move: {move}, Time Taken: {round(elapsed, 3)} seconds, Leaves Reached: {self.leavesCalculated}.")
        return move