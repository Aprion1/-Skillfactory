#Игра крестики-нолики
board_size = 3 #сколько клеток поле
#Доску решил разделить на 9 клеток, чтобы у каждой было число

board=[1,2,3,4,5,6,7,8,9]
def show_board():       #Функция отвечающая за показ игрового поля
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('', board[i*3], '|', board[1+ i*3], '|',board[2+ i*3], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index, symbol):    #Функция отвечающая за ход
    if (index > 9 or index < 1 or board[index - 1] in ('x', 'o')):
        return False

    board[index - 1] = symbol
    return True

def check_win():          #Функция проверяющая победу
    win = False

    victory_combination =(
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  #Горизонтальные победные комбинации
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  #Вертикальные победные комбинации
        (0, 4, 8), (2, 4, 6)              #Диагональные победные комбинации
    )

    for pos in victory_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():            #Функция старта игры
    current_player = 'x'
    step = 1
    show_board()

    while (step<10) and (check_win() == False):
      index = input('Ходит игрок ' + current_player + '. Введите номер поля (0-выход):')

      if (index == '0'):
        break

      if (game_step(int(index), current_player)):
         print('Ход завершён')

         if (current_player == 'x'):
             current_player = 'o'
         else:
             current_player = 'x'
         show_board()
         step+=1
      else:
        print('Неверный номер, повторите попытку')
    if (step == 10):
        print('Ничья, игра окончена!')
    print('Победил ' + check_win())

    step+= 1

print("Добро пожаловать в крестики-нолики")
start_game()