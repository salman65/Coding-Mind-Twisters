def print_puzzle(puzzle):
    CGREEN = '\033[32m'
    CEND = '\033[0m'
    for ind1, row in enumerate(puzzle):
        if ind1 % 3 == 0:
            print("=========================================")
        else:
            print("-----------------------------------------")
        for ind2, col in enumerate(row):
            num = col if col != '.' else ' '
            num = CGREEN + num + CEND
            if ind2 % 3 == 0:
                print("|| " + num, end=' ')
            elif ind2 == len(row) - 1:
                print("| " + num + " ||")
            else:
                print("| " + num, end=' ')

        if ind1 == len(puzzle) - 1:
            print("=========================================")


def checker(row, col, cell, num):
    if num in row or num in col or num in cell:
        return False
    return True


def get_row(lst, row):
    return lst[row]


def get_col(lst, col):
    return [x[col] for x in lst]


def get_cell(lst, row, col):
    cell_lst = []
    c_r_ind = int(row / 3)
    c_c_ind = int(col / 3)
    for x in range(c_r_ind * 3, (c_r_ind + 1) * 3):
        for y in range(c_c_ind * 3, (c_c_ind + 1) * 3):
            cell_lst += lst[x][y]
    return cell_lst


def row_checker(lst, row_lst, row, col, num):
    for ind, i in enumerate(row_lst):
        if i == '.' and ind != col:
            col_lst = get_col(lst, ind)
            cell_lst = get_cell(lst, row, ind)
            status = checker([], col_lst, cell_lst, num)
            if status:
                return False
    return True


def col_checker(lst, col_lst, row, col, num):
    for ind, i in enumerate(col_lst):
        if i == '.' and ind != row:
            row_lst = get_row(lst, ind)
            cell_lst = get_cell(lst, ind, col)
            status = checker(row_lst, [], cell_lst, num)
            if status:
                return False
    return True


def cell_checker(lst, cell_lst, row, col, num):
    cell_ind = row * 3 + col
    for ind, i in enumerate(cell_lst):
        if i == '.' and ind != cell_ind:
            row_lst = get_row(lst, row)
            col_lst = get_col(lst, col)
            status = checker(row_lst, col_lst, [], num)
            if status:
                return False
    return True


def val_check(lst, row, col):
    row_lst = get_row(lst, row)
    col_lst = get_col(lst, col)
    cell_lst = get_cell(lst, row, col)
    for i in range(1, 10):
        num_to_check = str(i)
        status = checker(row_lst, col_lst, cell_lst, num_to_check)
        if status:
            row_status = row_checker(lst, row_lst, row, col, num_to_check)
            if row_status:
                lst[row][col] = num_to_check
                return lst
            else:
                col_status = col_checker(lst, col_lst, row, col, num_to_check)
                if col_status:
                    lst[row][col] = num_to_check
                    return lst
                else:
                    cell_status = cell_checker(lst, cell_lst, row, col, num_to_check)
                    if cell_status:
                        lst[row][col] = num_to_check
                        return lst
    return lst


def end_check(lst):
    for x in lst:
        if '.' in x:
            return False
    return True


def guess_val(lst, guess_dict=None):
    if guess_dict:
        new_lst = [[y for y in x] for x in guess_dict['puzzle']]
    else:
        new_lst = [[y for y in x] for x in lst]
    for ind1, row in enumerate(new_lst):
        if guess_dict and ind1 < guess_dict['row']:
            continue
        for ind2, col in enumerate(row):
            if guess_dict and ind2 < guess_dict['col']:
                continue
            if col == '.':
                start_ind = 1 if not guess_dict else guess_dict['ind'] + 1
                if start_ind > 9:
                    guess_dict['ind'] = 0
                    if ind2 < 8:
                        guess_dict['col'] = ind2
                    else:
                        guess_dict['col'] = 0
                        guess_dict['row'] = ind1
                else:
                    row_lst = get_row(new_lst, ind1)
                    col_lst = get_col(new_lst, ind2)
                    cell_lst = get_cell(new_lst, ind1, ind2)
                    for i in range(start_ind, 10):
                        num_to_check = str(i)
                        status = checker(row_lst, col_lst, cell_lst, num_to_check)
                        if status:
                            guess_dict = {"ind": i, "puzzle": [[y for y in x] for x in new_lst], "row": ind1, "col": ind2}
                            new_lst[ind1][ind2] = num_to_check
                            return (new_lst, guess_dict)
    return (new_lst, guess_dict)


def solve_sudoku(lst, guess_dict=None):
    prev_lst = [[y for y in x] for x in lst]
    for ind1, row in enumerate(lst):
        for ind2, col in enumerate(row):
            if col == '.':
                lst = val_check(lst, ind1, ind2)
    end_status = end_check(lst)
    if prev_lst == lst:
        (lst, guess_dict) = guess_val(lst, guess_dict)
    if end_status:
        return lst
    else:
        return solve_sudoku(lst, guess_dict)


def is_valid(lst):
    for ind, row in enumerate(lst):
        for x in range(1, 10):
            if str(x) not in row:
                return False
    return True


puzzle = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]


class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans = solve_sudoku(board)
        for x in range(len(ans)):
            for y in range(len(ans[x])):
                board[x][y] = ans[x][y]


Solution().solveSudoku(puzzle)
puzzle = solve_sudoku(puzzle)
print(is_valid(puzzle))
print_puzzle(puzzle)
