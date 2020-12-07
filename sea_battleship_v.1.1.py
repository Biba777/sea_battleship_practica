from random import randint


class Ship:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length


class Board:
    def __init__(self, ships):
        f = []
        for j in range(6):
            f.append([])
            for c in range(6):
                f[j].append('O')
        self.field = f
        for ship in ships:
            for i in range(ship.length):
                self.field[ship.y][ship.x + i] = '■'

    def show_player_field(self):
        for row in self.field:
            print(*row)

    def show_ai_field(self):
        for row in self.field:
            print(*row)

    def shot_player(self):
        '''это кусок кода, если хотите нажимать на кнопки сами'''
        print("Игрок 1 выбери куда стрелять")
        while True:
            try:
                string = int(input("Введите номер строки: "))
                column = int(input("Введите номер столбца: "))
            except ValueError:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if string < 1 or string > 6 or column < 1 or column > 6 or self.field[string - 1][column - 1] == 'T' or \
                    self.field[string - 1][column - 1] == 'X':
                print("Вы уже сюда стреляли!")
                continue
            elif self.field[string - 1][column - 1] == 'O':
                self.field[string - 1][column - 1] = 'T'
                print('Ты промазал !')
                break
            else:
                print('Ты попал в цель !')
                self.field[string - 1][column - 1] = "X"
                break
        # print("Компьютер 1 выбирает куда стрелять")
        # string = randint(1, 6)
        # column = randint(1, 6)

        # while True:
        #     if self.field[string - 1][column - 1] == 'O':
        #         self.field[string - 1][column - 1] = 'T'
        #         print('Компьютер 1 промазал !')
        #         break
        #     elif self.field[string - 1][column - 1] == 'T' or self.field[string - 1][column - 1] == 'X':
        #         string = randint(1, 6)
        #         column = randint(1, 6)

        #     else:
        #         self.field[string - 1][column - 1] = "X"
        #         print('Компьютер 1 попал !')
        #         break

    def shot_ai(self):
        print("Компьютер 2 выбирает куда стрелять")
        string = randint(1, 6)
        column = randint(1, 6)

        while True:
            if self.field[string - 1][column - 1] == 'O':
                self.field[string - 1][column - 1] = 'T'
                print('Компьютер 2 промазал !')
                break
            elif self.field[string - 1][column - 1] == 'T' or self.field[string - 1][column - 1] == 'X':
                string = randint(1, 6)
                column = randint(1, 6)

            else:
                self.field[string - 1][column - 1] = "X"
                print('Компьютер 2 попал !')
                break


ships = [Ship(0, 0, 3), Ship(0, 2, 2), Ship(3, 2, 2), Ship(5, 0, 1), Ship(0, 5, 1), Ship(2, 4, 1), Ship(5, 4, 1)]
ai = Board(ships)
plr = Board(ships)
cw = Board(ships)
counter_plr = 0
counter_ai = 0
valid = True
while valid:
    print('***доска игрока')
    print('+MOVE_PLR', counter_plr)
    plr.shot_player()
    plr.show_player_field()
    counter_plr += 1
    if counter_plr > 11:
        if '■' not in plr.field[0] and '■' not in plr.field[1] and '■' not in plr.field[2] and '■' not in plr.field[3] and '■' not in plr.field[4] and '■' not in plr.field[5]:
            print('ИГРОК 1 ПОБЕДИЛ')
            valid = False
            break
    print('**доска компьютера')
    print('+MOVE_AI', counter_ai)
    ai.shot_ai()
    ai.show_ai_field()
    counter_ai += 1
    if counter_ai > 11:
        if counter_ai > 11:
            if '■' not in ai.field[0] and '■' not in ai.field[1] and '■' not in ai.field[2] and '■' not in ai.field[3] and '■' not in ai.field[4] and '■' not in ai.field[5]:
                print('ИГРОК 2 ПОБЕДИЛ')
                valid = False
                break
