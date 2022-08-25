class Game:
    def __init__(self):
        self.wins = 0
        self.losses = 0
    def won_level(self):
        self.wins += 1
    def lost_level(self):
        self.losses += 1
    @property
    def score(self):
        return self.wins - self.losses

g1 = Game()
g1.lost_level()
print(g1.losses)
g1.won_level()
print(g1.wins)
print(g1.score)