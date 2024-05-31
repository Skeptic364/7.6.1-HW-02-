n = 1 #счётчик ходов


#----------Приветствие----------
def begin():
    print("-------------------")
    print("Приветствуем в игре")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print("-------------------")
begin()

#----------Создание поля и вывод----------
field = [[" "]*3 for i in range(3)]
#print(field)

def show():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
show()

#----------Ввод координат----------

def ND():#Вывод о неверных данных
    print("-------------------------")
    print("Введите верные координаты")
    print("-------------------------")
def ask():
    global n
    a = (input("Введите координаты: "))
    print("-------------------------")
    if a[1] != " " or len(a) != 3:#проверка правильности ввода
        ND()
        show()
        return ask()
    a = a.split()
    if a[0].isdigit() and a[1].isdigit:#проверка правильности ввода2
        x = int(a[0])
        y = int(a[1])
    else:
        ND()
        show()
        return ask()
    if (0 <= x <= 2) and (0 <= y <= 2):#проверка диапозона
        if (field[x][y] == " "):#проверка свободного поля
            if n % 2 == 1:
                field[x][y] = "X"
                n += 1
                show()
                win()
            else:
                field[x][y] = "0"
                n += 1
                show()
                win()
            return x, y
        else:
            print("-------------")
            print("Клетка занята")
            print("-------------")
            show()
            return ask()
    else:
        ND()
        show()
        return ask()

#----------чей ход?----------
def move():
    global n
    while True:
        if n == 10:
            print("Победила дружба")
            break
        if n % 2 == 1:
            print("-------------------------")
            print("Ходят крестики  ")
            ask()
        else:
            print("-------------------------")
            print("Ходят нолики  ")
            ask()
        return


#----------Победные комбинации----------
def win():
    global n
    win_comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for i in win_comb:
        a = i[0]
        b = i[1]
        c = i[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f'Победили "{field[a[0]][a[1]]}"')
            n = 100
            return
    else:
        return move()



win()



