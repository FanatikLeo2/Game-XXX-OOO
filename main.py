import time

spaces_playing_board = range(1, 10)
X, O, empty = 'X', 'O', ' '


def main():
    print('\nИгра началась!')
    game_board = get_empty_board()
    main_player, next_player = X, O
    while True:
        time.sleep(1)
        print(get_board_paint(game_board))
        move = None
        while not (move in spaces_playing_board and game_board[move] == empty):
            print(f'\nНа какое место ставим -{main_player}- ? (1-9)')
            try:
                move = int(input('> '))
            finally:
                continue
        game_board[move] = main_player
        if check_board(game_board, main_player):
            time.sleep(1)
            print(get_board_paint(game_board))
            print(f'\nИгрок с символом {main_player} победил!')
            break
        elif board_full(game_board):
            time.sleep(1)
            print(get_board_paint(game_board))
            print('\nНичья!')
            break
        else:
            main_player, next_player = next_player, main_player
    print('\nИгра окончена!')
    input()


def get_empty_board():
    board = {}
    for space in spaces_playing_board:
        board[space] = empty
    return board


def get_board_paint(board):
    return f'\n {board[1]} | {board[2]} | {board[3]}          1   2   3\n' \
           f'---+---+---\n ' \
           f'{board[4]} | {board[5]} | {board[6]}          4   5   6\n' \
           f'---+---+---\n ' \
           f'{board[7]} | {board[8]} | {board[9]}          7   8   9'


def check_board(board, player):
    b, p = board, player
    return ((b[1] == b[2] == b[3] == p) or
            (b[4] == b[5] == b[6] == p) or
            (b[7] == b[8] == b[9] == p) or
            (b[1] == b[4] == b[7] == p) or
            (b[2] == b[5] == b[8] == p) or
            (b[3] == b[6] == b[9] == p) or
            (b[3] == b[5] == b[7] == p) or
            (b[1] == b[5] == b[9] == p))


def board_full(board):
    for space in spaces_playing_board:
        if board[space] == empty:
            return False
    return True


main()