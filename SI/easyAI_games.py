from easyAI import TwoPlayerGame, solve_with_iterative_deepening, Human_Player, AI_Player, Negamax

class LastCoin(TwoPlayerGame):
    def __init__(self, players = None):
        self.players = players
        self.current_player = 1
        self.num_coins = 25
        self.max_coins = 4

    def possible_moves(self):
        return [str(x) for x in range(1,self.max_coins+1)]

    def make_move(self, move):
        self.num_coins -= int(move)

    def is_over(self):
        return self.num_coins <= 0

    def scoring(self):
        return 100 if self.is_over() else 0

    def show(self):
        print(self.num_coins, 'monet pozostało na stosie')

    

if __name__ == "__main__":
    ai = Negamax(10)
    game = LastCoin([Human_Player(), AI_Player(ai)])
    history = game.play()
    for i in history:
        try:
            print(f"Pobrano ze stosu {i[1]} monet")
        except:
            print("Zostało 0 monet")