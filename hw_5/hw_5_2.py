# 2. Создайте программу
# для игры в ""Крестики-нолики"".
# (в консоли происходит
# выбор позиции)


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1, 10))


# рисуем доску
def draw_board(board):
    # по горизонтали -
    print("-" * 13)
    for i in range(3):
      # по вертикали |
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

# ввод данных с определением занятой клетки, плюс проверка корректности ввода


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод, повторите")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята, повторите ввод")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

#функция проверки выйгрышных комбинаций на поле
def check_win(board):
    #комбинации
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

#мейн функция игры
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

input("Нажмите Enter для выхода!")
