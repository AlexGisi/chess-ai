class HumanController:
    def __init__(self):
        pass

    @staticmethod
    def get_move() -> str:
        return str(input("Enter your move: "))
