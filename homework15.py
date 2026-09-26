class FootballTeam:
    team_name = 'tsnoris milani'
    coach = 'gurandukht'
    players = []

    def add_player(self):
        player = {
            "name": input('Enter player name: '),
            "number": int(input('Enter player number: ')),
            "position": input('Enter player position: '),
            "age": int(input('Enter player age: ')),
            "nationality": input('Enter player nationality: ')
        }

        self.players.append(player)
        print("Player added.")

    def delete_player(self, number):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                print("Player removed.")
                return

        print("Player not found.")

    def update_player(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value
                print("Player updated.")
                return

        print("Player not found.")

    def club_info(self):
        print("Team:", self.team_name)
        print("Coach:", self.coach)
        print("Players:")

        for player in self.players:
            print(player)

    def show_player_info(self, number):
        for player in self.players:
            if player["number"] == number:
                print(player)
                return

        print("Player not found.")

        