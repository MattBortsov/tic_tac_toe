from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a') as file:
        file.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'{current_player} makes the move')

        while True:
            try:
                row = int(input('Enter the line N in the range: 0 - 2: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Enter the column N in the range: 0 - 2: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'The value must be non-negative and less than '
                    f'{game.field_size}.'
                )
                print('Reenter the row and column values.')
                continue
            except ValueError:
                print('Letters cannot be entered. Only numbers.')
                print('Reenter the row and column values.')
                continue
            except CellOccupiedError:
                print('Cell is occupied')
                print('Enter other coordinates.')
                continue
            except Exception as e:
                print(f'An error occurred: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            result = f'Won: {current_player}!'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Draw!'
            print(result)
            save_result(result)
            running = False

        current_player = '0' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
