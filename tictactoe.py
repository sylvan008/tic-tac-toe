import string
# write your code here


def print_game_grid(grid):
    horizontal_line = '---------'
    vertical_line = '|'
    print(horizontal_line)
    for line in grid:
        print(vertical_line, ' '.join(line), vertical_line)
    print(horizontal_line)


def check_end_game(grid):
    result_list = create_result_list(grid)
    checked_lines = result_to_bool(result_list)
    if not check_correct_moves(grid, checked_lines):
        print('Impossible')
        return True

    hase_empty_cell = check_empty_cells(grid)
    if any(checked_lines):
        winner = find_winner(result_list, checked_lines)
        print_winner(winner)
        return True
    if not hase_empty_cell:
        print('Draw')
        return True
    return False


def create_grid(input_list):
    return [input_list[i:i + 3] for i in range(0, 9, 3)]


def print_winner(winner):
    print(f"{winner} wins")


def check_empty_cells(grid):
    count = 0
    for line in grid:
        count += line.count('_')
    return count > 0


def is_three_equal(cell_1, cell_2, cell_3):
    return cell_1 == cell_2 == cell_3 and cell_1 != '_'


def create_result_list(grid):
    # horizontal = [string_cells[i:i+3] for i in range(0, 9, 3)]
    # vertical = [string_cells[0 + i:7 + i:3] for i in range(3)]
    # diagonal = [string_cells[0 + i:9 - i:4 - i] for i in range(0, 3, 2)]
    horizontal = [line for line in grid]
    vertical = [[grid[line][el] for line in range(3)] for el in range(3)]
    diagonal = [[grid[el][abs(el - i)] for el in range(0, 3)] for i in range(0, 3, 2)]
    return [*horizontal, *vertical, *diagonal]


def result_to_bool(result_):
    return [is_three_equal(*string_) for string_ in result_]


def find_winner(result_, bool_list):
    win_index = bool_list.index(True)
    return result_[win_index][0]


def count_moves(line, player):
    return line.count(player)


def check_correct_moves(grid, checked_lines):
    count_winners = sum([1 for cell in checked_lines if cell])
    x_moves = sum([count_moves(line, 'X') for line in grid])
    o_moves = sum([count_moves(line, 'O') for line in grid])
    return abs(x_moves - o_moves) < 2 and count_winners < 2


def enter_coordinates(grid):
    while True:
        print('Enter the coordinates:')
        coordinates = input().split()
        if all([val in string.digits for val in coordinates]):
            coordinates = tuple([int(val) - 1 for val in coordinates])
            if not check_input_interval(coordinates):
                print('Coordinates should be from 1 to 3!')
                continue
            if check_occupied_cell(grid, coordinates):
                print('This cell is occupied! Choose another one!')
                continue
            return coordinates
        else:
            print('You should enter numbers!')


def check_input_interval(coordinates):
    return all([0 <= val < 3 for val in coordinates])


def check_occupied_cell(grid, coordinates):
    x, y = coordinates
    return grid[x][y] != '_'


def update_grid(grid, coordinates, player):
    x, y = coordinates
    grid[x][y] = player
    return grid


def switch_player(player):
    return 'O' if player == 'X' else 'X'


def game():
    print('Enter cells:')
    # input_list = [*input()]
    empty_grid = [*'_________']
    player = 'X'
    grid = create_grid(empty_grid)

    game_end = check_end_game(grid)
    print_game_grid(grid)
    while not game_end:
        coordinates = enter_coordinates(grid)
        grid = update_grid(grid, coordinates, player)
        print_game_grid(grid)
        game_end = check_end_game(grid)
        player = switch_player(player)


game()
