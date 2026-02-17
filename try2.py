field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def battle_scenario():
    print("", *field[0], "\n", *field[1], "\n", *field[2])

battle_scenario()

player_move = 'x'
while True:
    print(f"Ход игрока {player_move} ")
    if player_move == "x":
        player_move = "0"
    else:
        player_move = "x"