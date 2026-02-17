default_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_scenario = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # По горизонтали
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # По вертикали
    (0, 4, 8), (2, 4, 6)             # По диагонали
]

player_sigh = "x" # Переменная для смены игрока, по правилам первым ходят "Крестики"

def battle_scenario():
    print("", field[:3], "\n", field[3:6], "\n", field[6:]) # Визуальная отрисовка поля игры

print("Правила игры: Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики)." "\n" "Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает. ""\n" "Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, горизонтали или большой диагонали нет трёх одинаковых знаков, ""\n" "партия считается закончившейся вничью. Первый ход делает игрок, ставящий крестики. ")
battle_scenario() # Предварительный показ поля

while True:
    player_input = input(f"Игрок {player_sigh} ходит: ") # Уведомление о том, какой игрок начинает ходить

    if not player_input.isdigit(): # Проверка что на ввод принимает только числа
        print("!! Ошибка: Введи только цифру от 1 до 9 !!")
        continue

    move = int(player_input)
    index = move - 1

    if index < 0 or index > 8:
        print("!! К вводу доступны только значения от 1 до 9 !!")
        continue

    if isinstance(field[index], str):
        print("!! Ошибка: Эта клетка уже занята !!")
        continue

    field[index] = player_sigh

    victory = False
    for a, b, c in win_scenario:
        if field[a] == field[b] == field[c]:
            battle_scenario()
            print(f"ПОЗДРАВЛЯЕМ! Игрок '{player_sigh}' победил!")
            victory = True
            break

    if victory:
        break

    if not any(isinstance(x, int) for x in field):
        battle_scenario()
        print("НИЧЬЯ! Свободных клеток больше нет.")
        break

    if player_sigh == "x":
        player_sigh = "0"
        battle_scenario()
    else:
        player_sigh = "x"
        battle_scenario()

