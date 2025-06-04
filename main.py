from copy import deepcopy

def meets_constraints(grid: list, i,j, decision:int, n=9) -> bool:
        '''
        Validation potential entry choice
        :param grid:
        :param i: row index
        :param j: column index
        :param decision: potential entry
        :param n: size of grid
        :return: True or False
        '''
        grid[i][j] = decision # assigning the proposed value
        # Check row
        if grid[i].count(decision) > 1:
                return False

        # Check column
        for row in range(n):
                if row !=i and grid[row][j] == decision:
                        return False

        # Check 3*3 box
        box_start_row = int(i/3) *3
        box_start_col = int(j/3) *3
        for row in range(box_start_row, box_start_row+3):
                for col in range(box_start_col, box_start_col+3):
                        if (row != i or col != j) and grid[row][col] == decision:
                                return False

        return True


def find_solution(grid: list, i=-1, j=-1, n=9) -> tuple:
        '''
        A backtracking algorithm to find a solution
        :param grid: sudoku grid
        :param i: row index
        :param j: column index
        :param n: size of square grid
        :return: Either a solution or a backtracking instance
        '''
        while True:  # Finding the next mutable entry
                j = (j + 1) % n
                if j == 0:
                        i += 1

                # Base case (we terminate whenever the last mutable entry is out of range)
                if i == n:
                        return (grid, True)

                if grid[i][j] == 0:  # Mutable entry found
                        break

                elif not meets_constraints(grid=grid, i=i, j=j,
                                           decision=grid[i][j]):  # ensure non-mutable entries obey the rules
                        return (grid, False)

        for candidate in range(1, n + 1):

                if not meets_constraints(grid=grid, i=i, j=j, decision=candidate):  # Accept if adheres to constraints
                        continue

                grid[i][j] = candidate

                (new_grid, val) = find_solution(grid=grid, i=i, j=j)  # Recursive call

                if val:
                        return (new_grid, val)

        grid[i][j] = 0  # Re-initialising entry
        return (grid, False)

def print_board(grid:list):
        for row in grid:
                print(row)


if __name__ == '__main__':

        grid = [[0, 0, 0, 8, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 4, 3, 0],
                [5, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 7, 0, 8, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 2, 0, 0, 3, 0, 0, 0, 0],
                [6, 0, 0, 0, 0, 0, 0, 7, 5],
                [0, 0, 3, 4, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 6, 0, 0]]

        solved_grid, val = find_solution(grid=grid)

        print_board(grid=solved_grid) if val else print('Unsolvable')