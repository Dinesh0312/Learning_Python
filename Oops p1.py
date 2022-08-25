class Phone:

    def make_call(self):
        print("Making a call")

    def play_game(self):
        print("Playing a game")

    def set_color(self,color):
        self.color = color

    def set_cost(self,cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost


p1 = Phone()

p1.make_call()
p1.play_game()


p2 = Phone()

p2.set_color("Blue")
p2.set_cost(15000)

print(p2.show_color())
print(p2.show_cost())