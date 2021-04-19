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
    UPPER_BOUND = PIECE_MAP['K'] * 16
    LOWER_BOUND = -PIECE_MAP['K'] * 16
    RESULT_MAP = {
        '1-0': UPPER_BOUND,
        '0-1': LOWER_BOUND,
        '1/2-1/2': 0
    }
    def __init__(self, depth: int = 4) -> None:
        self.depth = depth
        self.positionsEvaluated = 0

    def heuristic(self, board: chess.Board) -> float:
        result = board.result()
        return AIController.RESULT_MAP[result] if result in AIController.RESULT_MAP \
            else np.sum([AIController.PIECE_MAP[char] if char in AIController.PIECE_MAP else 0 for char in board.board_fen()])

    def minimax(self, board: chess.Board, depth: int, maximizingPlayer: bool,
        alpha: float, beta: float) -> float:
        self.positionsEvaluated += 1
        if depth == 0 or board.is_game_over():
            return self.heuristic(board)
        if maximizingPlayer:
            value = AIController.LOWER_BOUND # lower bound
            for move in board.legal_moves:
                board.push(move)
                value = max(value, self.minimax(board, depth-1, False, alpha, beta))
                board.pop()
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value  # returns best move
        else:  # minimizing player
            value = AIController.UPPER_BOUND # upper bound
            for move in board.legal_moves:
                board.push(move)
                value = min(value, self.minimax(board, depth-1, True, alpha, beta))
                board.pop()
                beta = min(beta, value)
                if beta <= alpha:
                    break
            
            return value

    def make_child(self, board: chess.Board, move: str) -> chess.Board:
        child = board.copy()
        child.push(move)
        return child

    def getMove(self, board: chess.Board, player: bool) -> str:
        self.positionsEvaluated = 0
        timer = time()
        legal_moves = list(board.legal_moves)
        
        move_costs = np.array([self.minimax(self.make_child(board, move), self.depth, player, \
            AIController.LOWER_BOUND, AIController.UPPER_BOUND) \
                for move in legal_moves])
        
        if player:
            move = board.san(legal_moves[np.random.choice(np.flatnonzero(move_costs == move_costs.max()))])
            #print("Move taken has a value of: ", max(move_costs))
        else:
            move = board.san(legal_moves[np.random.choice(np.flatnonzero(move_costs == move_costs.min()))])
            #print("Move taken has a value of: ", min(move_costs))

        elapsed = time() - timer
        print(f"Move: {move}, Time Taken: {round(elapsed, 3)} seconds, Positions Evaluated: {self.positionsEvaluated}.")
        return move