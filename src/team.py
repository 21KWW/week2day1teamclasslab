class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player):
        return self.players.append(new_player)
    
    def has_player(self, new_player):
        for player in self.players:
            if player == new_player:
                return True
        return False

    def play_game(self, won_game):
        if won_game == True:
            self.points += 3
        