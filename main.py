from copy import deepcopy

# starting with a solvable sudoku puzzle
grid= [[0, 0, 0, 8, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 3, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0]]

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

def mutability_recall(grid: list) -> list:
    mut_grid = deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                mut_grid[i][j] = False
            else:
                mut_grid[i][j] = True

    return mut_grid


def find_solution(grid: list, mut_grid: list, i=0, j=0, n=9) -> tuple:
        '''
        A backtracking algorithm to find a solution
        :param grid:
        :param mut_grid: list of boolean values containing a bool value on the mutability of each entry
        :param i: row index
        :param j: column index
        :param n: size of square grid
        :return: Either a solution or a backtracking instance
        '''
        for candidate in range(1, n + 1):  # Accept if adheres to constraints

                if not meets_constraints(grid=grid, i=i, j=j, decision=candidate):
                        continue

                grid[i][j] = candidate

                while True:  # Finding the next mutable entry
                        j = (j + 1) % n
                        if j == 0:
                                i += 1

                        # Base case (we terminate whenever the last mutable entry is out of range)
                        if i == n:
                                return (grid, True)

                        if mut_grid[i][j]:
                                break

                (grid, val) = find_solution(grid=grid, mut_grid=mut_grid, i=i, j=j)  # Recursive call
                # print(grid, val)
                if val:
                        return (grid, val)

        return (grid, False)


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

        mut_grid = mutability_recall(grid)
        print(find_solution(grid=grid, mut_grid=mut_grid))